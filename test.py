import unittest
from app import create_app

class StravaLiteTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_register_user(self):
        res = self.app.post("/user", json={"name": "Alice", "age": 30})
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIn("id", data)
        self.assertEqual(data["name"], "Alice")
        self.assertEqual(data["age"], 30)

    def test_missing_name_register(self):
        res = self.app.post("/user", json={"age": 25})
        self.assertEqual(res.status_code, 400)  # Missing required 'name'

if __name__ == "__main__":
    unittest.main()
