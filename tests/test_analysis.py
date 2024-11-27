import unittest
from src.analysis import run_analysis
from src.utils import calculate_statistics
import pandas as pd

class TestAnalysis(unittest.TestCase):
    def test_run_analysis(self):
        # Sample mock data
        data = pd.DataFrame({'value': [10, 20, 30, 40, 50]})
        stats = calculate_statistics(data, 'value')

        self.assertEqual(stats['mean'], 30)
        self.assertEqual(stats['median'], 30)
        self.assertAlmostEqual(stats['std_dev'], 15.811, places=3)

if __name__ == '__main__':
    unittest.main()
