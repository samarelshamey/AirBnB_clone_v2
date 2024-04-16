#!/usr/bin/python3
"""unittest for state model"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """test class for test state"""

    def __init__(self, *args, **kwargs):
        """initiate test"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """test name3"""
        new = self.value()
        self.assertEqual(type(new.name), str)
