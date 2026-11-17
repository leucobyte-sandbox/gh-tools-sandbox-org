import unittest


class TestAlwaysFails(unittest.TestCase):
    def test_fails_on_purpose(self):
        self.assertEqual(1 + 1, 3, "this branch exists to produce a failing CI run")
