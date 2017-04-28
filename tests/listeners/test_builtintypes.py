import unittest

from FlowType.flowtype.listeners.builtintypes import print_type_format


class TestBuiltInTypes(unittest.TestCase):
    """Test case for builtin types."""

    def test_trigger_same_as_content(self):
        """Return an tuple where trigger text is same than context."""
        trigger = "boolean"
        description = "Flow boolean type"
        expected = ("boolean\tFlow boolean type", "boolean,")
        actual = print_type_format(trigger, description=description)

        self.assertEqual(actual, expected)

    def test_trigger_different_from_content(self):
        """Return an tuple where trigger text is different than context."""
        trigger = "boolean"
        content = "\$SpecialBoolean"
        description = "Flow boolean type"
        expected = ("boolean\tFlow boolean type", "\$SpecialBoolean,")
        actual = print_type_format(trigger, content, description)

        self.assertEqual(actual, expected)
