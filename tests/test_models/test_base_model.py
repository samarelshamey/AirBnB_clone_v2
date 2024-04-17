#!/usr/bin/python3
"""unittest for basemodel"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """test class for basemodel"""

    def __init__(self, *args, **kwargs):
        """initiate test"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """setup"""
        pass

    def tearDown(self):
        """teardown method"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """check if an instance of basemodel is created"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """test key word arg"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """check typeerror"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """check str"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """test to dict"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """test none"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """test id"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """test created at"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """test updated_at attributes"""
        new = self.value()
        new.created_at = new.created_at - datetime.timedelta(seconds=1)
        new.save()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        self.assertNotEqual(new.created_at, new.updated_at)
