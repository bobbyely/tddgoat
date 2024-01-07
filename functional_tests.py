from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_todo_list(self):
        # Open localhost on port 8000
        self.browser.get("http://localhost:8000")

        self.assertIn("To-Do", self.browser.title)

        self.fail("Finish the test!")


if __name__ == "__main__":
    unittest.main()