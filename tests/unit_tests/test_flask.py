import unittest
from unittest.mock import patch
from flask_app import app


class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index_route(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

    @patch("flask_app.svm_classifier")
    @patch("flask_app.vectorizer")
    def test_classify_route(self, mock_vectorizer, mock_classifier):
        mock_vectorizer.transform.return_value = "vectorized_email"
        mock_classifier.predict.return_value = [1]

        response = self.app.post("/classify", data={"email_text": "spam email"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["result"], "Email is spam!")


if __name__ == "__main__":
    unittest.main()
