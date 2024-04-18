import unittest
from unittest.mock import patch
import tkinter as tk
from tkinter import messagebox
from tkinter_app import SpamClassifierApp


class TestSpamClassifierInit(unittest.TestCase):

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

    @classmethod
    def setUpClass(cls):
        cls.root = tk.Tk()

    @classmethod
    def tearDownClass(cls):
        cls.root.destroy()

    def setUp(self):
        self.app = SpamClassifierApp(self.root)

    def tearDown(self):
        self.app = None

    def test_classification_spam(self):
        self.app.text_input.insert(tk.END, self.SPAM_MAIL)

        with patch.object(messagebox, "showinfo") as mock_showinfo:
            self.app.classify_email()

            mock_showinfo.assert_called_once_with(
                "Classification result", "The email is spam!"
            )

    def test_classification_not_spam(self):
        self.app.text_input.insert(tk.END, self.NO_SPAM_MAIL)

        with patch.object(messagebox, "showinfo") as mock_showinfo:
            self.app.classify_email()

            mock_showinfo.assert_called_once_with(
                "Classification result", "Email is not spam."
            )

    def test_classification_no_text(self):
        self.app.text_input.insert(1.0, "")

        with patch.object(messagebox, "showwarning") as mock_showwarning:
            self.app.classify_email()

            mock_showwarning.assert_called_once_with(
                "Classification result", "Please enter your email text."
            )


if __name__ == "__main__":
    unittest.main()
