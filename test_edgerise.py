# test_edgerise.py
"""
Tests for EdgeRise module.
"""

import unittest
from edgerise import EdgeRise

class TestEdgeRise(unittest.TestCase):
    """Test cases for EdgeRise class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EdgeRise()
        self.assertIsInstance(instance, EdgeRise)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EdgeRise()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
