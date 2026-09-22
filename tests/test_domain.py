import unittest
from pathlib import Path
from domain_context.loader import load_domain

class DomainContextTest(unittest.TestCase):
    def test_public_context_is_complete(self):
        value = load_domain(Path("fixtures/domain.json"))
        self.assertEqual(value["domain"], "nuclear-generator-qualification")
        self.assertGreaterEqual(len(value["facts"]), 3)

if __name__ == "__main__":
    unittest.main()
