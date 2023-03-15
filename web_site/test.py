import unittest
import requests


class TestAPI(unittest.TestCase):

    def test1(self):
        response = requests.get('http://127.0.0.1:8000/news')
        self.assertEqual(response.status_code, 200)
        print("test1: OK")

    def test2(self):
        response = requests.get('http://127.0.0.1:8000/about')
        self.assertEqual(response.status_code, 200)
        print("test2: OK")

    def test3(self):
        response = requests.get('http://127.0.0.1:8000/contacts')
        self.assertEqual(response.status_code, 200)
        print("test3: OK")


if __name__ == '__main__':
    tester = TestAPI()
    tester.test1()
    tester.test2()
    tester.test3()
