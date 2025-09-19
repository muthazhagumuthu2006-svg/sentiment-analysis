# tests/test_preprocess.py

import unittest
from src.preprocess import clean_text

class TestPreprocess(unittest.TestCase):

    def test_remove_urls(self):
        text = "Check this out http://example.com"
        self.assertNotIn("http", clean_text(text))

    def test_remove_mentions(self):
        text = "Hello @user!"
        self.assertNotIn("@user", clean_text(text))

    def test_remove_hashtags(self):
        text = "Loving this! #awesome"
        self.assertNotIn("#awesome", clean_text(text))

    def test_convert_emojis(self):
        text = "I love it 😍"
        cleaned = clean_text(text)
        self.assertIn("smiling_face_with_heart_eyes", cleaned)

    def test_keep_letters_numbers(self):
        text = "Python3 is cool!"
        cleaned = clean_text(text)
        self.assertIn("Python3", cleaned)

if __name__ == "__main__":
    unittest.main()
