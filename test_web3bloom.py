# test_web3bloom.py
"""
Tests for Web3Bloom module.
"""

import unittest
from web3bloom import Web3Bloom

class TestWeb3Bloom(unittest.TestCase):
    """Test cases for Web3Bloom class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = Web3Bloom()
        self.assertIsInstance(instance, Web3Bloom)

    def test_run_method(self):
        """Test the run method."""
        instance = Web3Bloom()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
