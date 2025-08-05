# test_fujipeak.py
"""
Tests for FujiPeak module.
"""

import unittest
from fujipeak import FujiPeak

class TestFujiPeak(unittest.TestCase):
    """Test cases for FujiPeak class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FujiPeak()
        self.assertIsInstance(instance, FujiPeak)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FujiPeak()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
