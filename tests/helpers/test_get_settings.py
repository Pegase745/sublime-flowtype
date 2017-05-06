import unittest
from unittest.mock import patch

from FlowType.flowtype.helpers import get_settings

fake_settings = {
    'fake_key': 'fake_value',
}


@patch(
    'sublime.load_settings',
    return_value=fake_settings
)
class TestGetSettings(unittest.TestCase):
    """Test case for `get_settings` function."""

    def test_key(self, *_):
        """Check that it returns the value for an existing key."""
        value = get_settings('fake_key')

        self.assertEqual(value, 'fake_value')

    def test_no_key(self, *_):
        """Check that it returns None for a non existing key."""
        value = get_settings('non_existing')

        self.assertIsNone(value)
