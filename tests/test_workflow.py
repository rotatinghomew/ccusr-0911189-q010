import copy
import json
from pathlib import Path
import subprocess
import sys
import unittest

from observatory.workflow import report


class WorkflowTest(unittest.TestCase):
    def setUp(self):
        self.path = Path(__file__).resolve().parents[1] / 'data' / 'sample.json'
        self.data = json.loads(self.path.read_text(encoding='utf-8'))

    def test_entry(self):
        result = subprocess.run([sys.executable, '-m', 'observatory', 'quarter', str(self.path)],
                                check=True, capture_output=True, text=True)
        self.assertEqual(json.loads(result.stdout), report(self.data))

    def test_missing_is_separate_from_unmatched(self):
        output = report(self.data)
        self.assertEqual(output['raw']['Q1'],{'eligible':3,'scanned':2,'hits':1})
        self.assertEqual(output['proof'],{'targeted':1,'random':1})

    def test_definition_changes_matching_and_reusable_review(self):
        self.data['edition'] = 'new'
        output = report(self.data)
        self.assertEqual(output['raw']['Q1']['hits'],2)
        self.assertEqual(output['proof'],{'random':1})
