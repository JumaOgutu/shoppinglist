import unittest
from flask import Flask
from app import views

#Functions to carry out TDD(Test-Driven-Development)
#This test will help me establish whether the details of a user are matching

class FirstTest(unittest.TestCase):

    def test_created_users(self):
        result = {"ogutu":['ogutu@ogutu.com', '12112']} #dict that has ogutu as the key and the email and password as the values
        message = views.create_user('ogutu', 'ogutu@ogutu.com', '12112')
        self.assertEqual(message, result) #checks whether the result and method are equal



if __name__ == '__main__':
    unittest.main()