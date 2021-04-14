import string
import random


def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	return ip


def random_key():
	all_digits = list(string.digits)
	random_key = ""
	return random_key.join(random.sample(all_digits, 10))
