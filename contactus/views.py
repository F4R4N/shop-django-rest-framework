from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Contact, MassEmail
from .utils import get_client_ip
from .serializers import ContactSerializer


class CreateForm(APIView):
	permission_classes = (permissions.AllowAny, )

	def post(self, request, format=None):
		required_fields = ["name", "email", "text"]
		for field in required_fields:
			if field not in request.data:
				return Response(
					status=status.HTTP_400_BAD_REQUEST,
					data={"detail": "{} is required".format(field)})

		ip = get_client_ip(request)
		contact = Contact.objects.create(
			name=request.data["name"],
			email=request.data["email"],
			text=request.data["text"]
		)
		contact.ip = ip
		if "subject" in request.data:
			contact.subject = request.data["subject"]
		if "phone_number" in request.data:
			contact.phone_number = request.data["phone_number"]
		if "address" in request.data:
			contact.address = request.data["address"]

		contact.save()
		admin_name = list(User.objects.filter(is_superuser=True, is_staff=True).values_list("first_name", flat=True))[0]
		mail_subject = "{0} Contact Us ".format(settings.APP_NAME)
		message = "dear '{0}',\n we got your email. we will response as soon as possible.\n\nBest Regards '{1}'".format(contact.name, admin_name)
		to_email = contact.email
		EmailMessage(mail_subject, message, to=[to_email]).send()

		return Response(status=status.HTTP_200_OK, data={"detail": "form created."})


class AdminContactReader(APIView):
	permission_classes = (permissions.IsAdminUser, )

	def get(self, request, year=None, month=None, format=None):
		contacts = Contact.objects.all()
		if all([year, month]):
			contacts = Contact.objects.filter(datetime__year=year, datetime__month=month)
		serializer = ContactSerializer(instance=contacts, many=True)
		return Response(status=status.HTTP_200_OK, data=serializer.data)


class AdminEditIsReaded(APIView):
	permission_classes = (permissions.IsAdminUser, )

	def put(self, request, key, format=None):
		contact = get_object_or_404(Contact, key=key)
		if "is_readed" not in request.data:
			return Response(
				status=status.HTTP_400_BAD_REQUEST,
				data={"detail": "'is_readed' field not provided."})

		contact.is_readed = request.data["is_readed"]
		contact.save()
		return Response(status=status.HTTP_200_OK, data={"detail": "updated"})


class AdminSendMassEmail(APIView):
	permission_classes = (permissions.IsAdminUser, )

	def post(self, request, format=None):
		fields = ["subject", "text"]
		for field in fields:
			if field not in request:
				return Response(
					status=status.HTTP_400_BAD_REQUEST,
					data={"detail": "field '{0}' not provided.".format(field)})

		email = MassEmail.objects.create(subject=request.data["subject"], text=request.data["text"])
		if "name" in request.data:
			email.name = request.data["name"]
		email.save()
		mail_subject = request.data["subject"]
		message = request.data["text"]
		all_emails = list(Contact.objects.all().values_list("email", flat=True))
		EmailMessage(mail_subject, message, to=all_emails).send()
		return Response(
			status=status.HTTP_200_OK,
			data={"detail": "mass email sent.", "emails": all_emails})
