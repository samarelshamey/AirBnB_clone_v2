#!/usr/bin/python3
"""unit test for amenoty class"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """test class for amenity model"""

    def __init__(self, *args, **kwargs):
        """initiate the test"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ Test case to check the data type of the 'name' attribute.
        Creates a new instance of the Amenity class and asserts that
        the type of the 'name' attribute is a string
        """
        new = self.value()
        new.name = "Test Amenity Name"
        self.assertEqual(type(new.name), str)
