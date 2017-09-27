import unittest
from flask import Flask
from app import views

#Functions to carry out TDD(Test-Driven-Development)

class FirstTest(unittest.TestCase):

    def test_created_users(self):
        result = {"ogutu":['ogutu@ogutu.com', '121212']}
        message = views.create_user('ogutu', 'ogutu@ogutu.com', '12112')
        self.assertEqual(message, result)



if __name__ == '__main__':
    unittest.main()