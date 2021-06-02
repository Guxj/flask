# -*- coding:utf-8 -*-
# @Title: test_user_model.py
# @Package flask
# @Description: TODO
# @author 陈子康
# @Date 2021/5/22 22:23
import unittest

from flask import url_for
from wtforms import ValidationError

from app.auth.forms import RegistrationForm
from app.models import User, Role
from app import create_app, db


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        user = User(email="chenzikangyoder@gmail.com", username="as")
        db.session.add(user)
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register(self):
        response = self.client.post(url_for('auth.register'), data={
            'email': 'chenzikangyoder@gmail.com',
            'username': 'as',
            'password': 'as'
        })
        self.assertTrue(response.status_code == 200)

    def test_login(self):
        response = self.client.post(url_for('auth.login'), data={
            'email': 'chenzikangyoder@gmail.com',
            'password': 'as'
        })
        self.assertTrue(response.status_code == 200)

    def test_validata_email(self):
        with self.app.test_request_context():
            form = RegistrationForm()
            with self.assertRaises(ValidationError):
                form.email.data = "chenzikangyoder@gmail.com"
                form.validate_email(form.email)

    def test_validata_username(self):
        with self.app.test_request_context():
            form = RegistrationForm()
            with self.assertRaises(ValidationError):
                form.username.data = "as"
                form.validate_username(form.username)

    def test_password_setter(self):
        u = User(password='cat')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password='cat')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password='cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('dog'))

    def test_password_salts_are_random(self):
        u = User(password='cat')
        u2 = User(password='cat')
        self.assertTrue(u.password_hash != u2.password_hash)
