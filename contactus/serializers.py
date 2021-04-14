from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contact
		fields = (
			"key", "name", "email", "subject", "text", "phone_number", "address",
			"datetime", "ip", "is_readed")
