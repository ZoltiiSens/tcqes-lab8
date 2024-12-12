import unittest
from main import client, parser

class TestIperfClient(unittest.TestCase):
    def test_valid_default_ip(self):
        output, error = client()
        self.assertTrue(error is None or error == "")
        self.assertTrue("connected" in output)

    def test_invalid_ip(self):
        _, error = client("invalid_ip")
        self.assertIsNotNone(error)

    def test_parsing(self):
        sample_output = "[  1] 0.0000-1.0000 sec  3.50 GBytes  30.0 Gbits/sec"
        parsed = parser(sample_output)
        self.assertEqual(len(parsed), 1)
        self.assertEqual(parsed[0]["Transfer"], 3.5)
