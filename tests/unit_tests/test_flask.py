import unittest
from unittest.mock import patch
from flask_app import app


class TestFlaskApp(unittest.TestCase):

    SPAM_MAIL = (
        "Dear Homeowner,\n\n \n\nInterest Rates are at their lowest point in 40 years!\n\n\n\nWe help you "
        "find the best rate for your situation by\n\nmatching your needs with hundreds of lenders!\n\n\n\n"
        "Home Improvement, Refinance, Second Mortgage,\n\nHome Equity Loans, and More! Even with less than"
        "\n\nperfect credit!\n\n\n\nThis service is 100% FREE to home owners and new\n\nhome buyers without "
        "any obligation. \n\n\n\nJust fill out a quick, simple form and jump-start\n\nyour future plans "
        "today!\n\n\n\n\n\nVisit http://61.145.116.186/user0201/index.asp?Afft=QM10\n\n\n\n\n\n\n\n\n\n\n\n"
        "\n\nTo unsubscribe, please visit:\n\n\n\nhttp://61.145.116.186/light/watch.asp\n"
    )
    NO_SPAM_MAIL = (
        "Hi Alex\n\nI would like to write to you because I like you and I can`t wait to see you!\n\n"
        "Regards\nMateusz Szewczyk\n"
    )

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

        response = self.app.post("/classify", data={"email_text": self.SPAM_MAIL})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["result"], "Email is spam!")


if __name__ == "__main__":
    unittest.main()
