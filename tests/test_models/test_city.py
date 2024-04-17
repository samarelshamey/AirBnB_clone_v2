#!/usr/bin/python3
"""unittest for city model"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """test class for city model"""

    def __init__(self, *args, **kwargs):
        """initiate test"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_str(self):
        """Test the string representation of a City instance"""
        new = self.value()
        new.id = "test_id"
        new.created_at = "test_created_at"
        new.updated_at = "test_updated_at"
        actual_str = str(new)
        expected_str = f"[{new.__class__.__name__}] ({new.id}) {{'id': '{new.id}', 'created_at': '{new.created_at}', 'updated_at': '{new.updated_at}'}}"
        self.assertIn(expected_str, actual_str)
