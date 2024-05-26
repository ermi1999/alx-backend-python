#!/usr/bin/env python3
"""This module tests utils module."""
from parameterized import parameterized
import unittest
from utils import access_nested_map, get_json, memoize
from unittest import mock


class TestAccessNestedMap(unittest.TestCase):
    """Test case for utils module."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test for test_access_nested_map function."""
        self.assertEqual(access_nested_map(nested_map, path), expected)
    
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """tests access_nested_map function with an exception."""
        with self.assertRaises(KeyError, msg=path[-1]):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test case for get_json method."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @mock.patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test case for get_json method."""
        mock_response = mock.Mock()
        mock_response.json.return_value = test_payload

        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test case for memoize decorator."""
    class TestClass:
        def a_method(self):
            return 42
        
        @memoize
        def a_property(self):
            return self.a_method()
    def test_memoize(self):
        """test case for memoize decorator."""
        with mock.patch.object(self.TestClass, 'a_method', return_value=42) as mocked_method:
            test_class = self.TestClass()
            result1 = test_class.a_property
            result2 = test_class.a_property
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mocked_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()