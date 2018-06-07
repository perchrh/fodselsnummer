"""Tests for `orgnr.py`."""

import unittest
import orgnr

class OrganisasjonsnummerTestCase(unittest.TestCase):
    """Tests for the orgnr functions`."""

    def test_valid_orgnr_is_valid(self):
        """Is the valid orgnr valid?"""
        valid_orgnr = '981617517'
        self.assertTrue(orgnr.check_orgnr(valid_orgnr))

    def test_valid_orgnr_with_pre_garbage(self):
        valid_orgnr = 'garbage9816175178'
        self.assertFalse(orgnr.check_orgnr(valid_orgnr))

    def test_valid_orgnr_with_post_garbage(self):
        valid_orgnr = '981617517garbage'
        self.assertFalse(orgnr.check_orgnr(valid_orgnr))

    def test_valid_orgnr_invalid_length(self):
        valid_orgnr = '9816175172'
        self.assertFalse(orgnr.check_orgnr(valid_orgnr))

    def test_invalid_orgnr_is_invalid(self):
        """Is the invalid orgnr invalid?"""
        invalid_orgnr = '981617516'
        self.assertFalse(orgnr.check_orgnr(invalid_orgnr))

if __name__ == '__main__':
    unittest.main()
