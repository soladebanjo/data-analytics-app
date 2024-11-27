import sys
import os
import unittest
import pandas as pd

# Ensure the src directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from utils import calculate_statistics  # Adjusted import based on the corrected path

class TestAnalysis(unittest.TestCase):
    def test_calculate_statistics(self):
        data = pd.DataFrame({"value": [10, 20, 30, 40, 50]})
        stats = calculate_statistics(data, "value")
        
        self.assertEqual(stats["mean"], 30)
        self.assertEqual(stats["median"], 30)
        self.assertAlmostEqual(stats["std_dev"], 15.811, places=3)

if __name__ == "__main__":
    unittest.main()
