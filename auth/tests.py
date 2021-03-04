from rest_framework.test import APITestCase
from django.urls import reverse
import json
from django.contrib.auth.models import User
from rest_framework.test import APIClient
import sys

class InvalidUserRegistrationApiViewTest(APITestCase):
	url = reverse('auth:auth_register')
	def test_invalid_password(self):
		user_data = {
			"username": 'testuser',
			'email': 'test@example.com',
			'password1': 'itsstrongpassword',
			'password2': 'anotherpassword',
			'first_name': 'test',
			'last_name': 'test'
		}
		response = self.client.post(self.url, user_data)
		self.assertEqual(400, response.status_code)
		self.assertTrue("password1" in json.loads(response.content))

	def test_username_exist(self):
		user_data1 = {
			"username": 'testuser',
			'email': 'test@example.com',
			'password1': 'itsstrongpassword',
			'password2': 'itsstrongpassword',
			'first_name': 'test',
			'last_name': 'test'
		}
		response = self.client.post(self.url, user_data1)
		self.assertEqual(201, response.status_code)
		user_data2 = {
			"username": 'testuser',
			'email': 'test@example.com',
			'password1': 'itsstrongpassword',
			'password2': 'itsstrongpassword',
			'first_name': 'test',
			'last_name': 'test'
		}
		response = self.client.post(self.url, user_data2)
		self.assertEqual(400, response.status_code)

	def test_common_password(self):
		user_data = {
			"username": 'testuser',
			'email': 'test@example.com',
			'password1': 'password',
			'password2': 'password',
			'first_name': 'test',
			'last_name': 'test'
		}
		response = self.client.post(self.url, user_data)
		self.assertEqual(400, response.status_code)
# TODO: this dont apply the middlewares
	# def test_personal_like_password(self):
	# 	user_data = {
	# 		"username": 'testuser',
	# 		'email': 'test@example.com',
	# 		'password1': 'testuser',
	# 		'password2': 'testuser',
	# 		'first_name': 'test',
	# 		'last_name': 'test'
	# 	}
	# 	response = self.client.post(self.url, user_data)
	# 	self.assertEqual(400, response.status_code)

	def test_length_less_than_8(self):
		user_data = {
			"username": 'testuser',
			'email': 'test@example.com',
			'password1': 'testus',
			'password2': 'testus',
			'first_name': 'test',
			'last_name': 'test'
		}
		response = self.client.post(self.url, user_data)
		self.assertEqual(400, response.status_code)



	def test_empty_first_name(self):
		user_data = {
			"username": 'testuser',
			'email': 'test@example.com',
			'password1': 'testus',
			'password2': 'testus',
			'first_name': "",
			'last_name': 'test'
		}
		response = self.client.post(self.url, user_data)
		self.assertEqual(400, response.status_code)
	
	def test_empty_last_name(self):
		user_data = {
			"username": 'testuser',
			'email': 'test@example.com',
			'password1': 'testus',
			'password2': 'testus',
			'first_name': "test",
			'last_name': ''
		}
		response = self.client.post(self.url, user_data)
		self.assertEqual(400, response.status_code)
	def test_empty_username(self):
		user_data = {
			"username": '',
			'email': 'test@example.com',
			'password1': 'testus',
			'password2': 'testus',
			'first_name': "",
			'last_name': 'test'
		}
		response = self.client.post(self.url, user_data)
		self.assertEqual(400, response.status_code)
	def test_empty_password(self):
		user_data = {
			"username": 'testuser',
			'email': 'test@example.com',
			'password1': '',
			'password2': '',
			'first_name': "test",
			'last_name': 'test'
		}
		response = self.client.post(self.url, user_data)
		self.assertEqual(400, response.status_code)

	def test_empty_email(self):
		user_data = {
			"username": 'testuser',
			'email': '',
			'password1': 'testuser',
			'password2': 'testuser',
			'first_name': "test",
			'last_name': 'test'
		}
		response = self.client.post(self.url, user_data)
		self.assertEqual(400, response.status_code)


class UserLoginApiViewTest(APITestCase):
	url = reverse('auth:auth_login')

	def setUp(self):
		self.username = 'test'
		self.email = 'test@example.com'
		self.password = 'password'
		self.user = User.objects.create_user(self.username, self.email, self.password)
	
	def test_login_without_password(self):
		response = self.client.post(self.url, {"username": self.username})
		self.assertEqual(400, response.status_code)

	def test_login_with_wrong_password(self):
		response = self.client.post(self.url, {"username": self.username, 'password': "test"})
		self.assertEqual(401, response.status_code)

	def test_login_with_valid_data(self):
		response = self.client.post(self.url, {"username": self.username, "password": self.password})
		self.assertEqual(200, response.status_code)
		self.assertTrue("access" in json.loads(response.content))


class ChangePasswordApiViewTest(APITestCase):
	login_url = reverse("auth:auth_login")
	def url(self, pk):
		change_password_url = reverse('auth:auth_change_password', kwargs={'pk': pk})
		return change_password_url
	def setUp(self):
		self.username = 'test'
		self.email = 'test@example.com'
		self.password = 'password'
		self.user = User.objects.create_user(self.username, self.email, self.password)
		response = self.client.post(self.login_url, {"username": self.username, "password": self.password})
		self.access = json.loads(response.content)['access']

	def test_change_password(self):
		data = {
			"old_password": self.password,
			"password1": "itsafuckingnewpassword",
			"password2": "itsafuckingnewpassword"
		}
		self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access)
		response = self.client.put(self.url(self.user.pk), data=data)
		# sys.stderr.write(repr(response.content) + '\n')
		self.assertEqual(200, response.status_code)

	def test_change_password_no_token(self):
		data = {
			"old_password": self.password,
			"password1": "itsafuckingnewpassword",
			"password2": "itsafuckingnewpassword"
		}
		response = self.client.put(self.url(self.user.pk), data=data)
		self.assertEqual(401, response.status_code)

	def test_change_password_invalid_old_password(self):
		data = {
			"old_password": 'notvalidpassword',
			"password1": "itsafuckingnewpassword",
			"password2": "itsafuckingnewpassword"
		}
		self.client.credentials(HTTP_AUTHORIZATION='Bearer '+ self.access)
		response = self.client.put(self.url(self.user.pk), data=data)
		self.assertEqual(400, response.status_code)

	def test_change_password_password_dont_match(self):
		data = {
			"old_password": self.password,
			"password1": "itsafuckingnewpassword",
			"password2": "itsafuckingned45wpassword"
		}
		self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access)
		response = self.client.put(self.url(self.user.pk), data=data)
		self.assertEqual(400, response.status_code)

	


