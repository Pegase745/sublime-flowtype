import unittest

from FlowType.flowtype.helpers import singleton


class TestSingleton(unittest.TestCase):
    """Test case for `singleton` function."""

    def tearDown(self):
        """Clear instances."""
        singleton._instances = {}

    def test_same_instance(self):
        """Return true if it's the same instance."""
        @singleton
        class Fake(object):
            pass

        instance_a = Fake()
        instance_b = Fake()

        self.assertEqual(instance_a, instance_b)
