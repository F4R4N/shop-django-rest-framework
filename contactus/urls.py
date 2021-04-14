from django.urls import path
from .views import CreateForm, AdminContactReader, AdminSendMassEmail

app_name = "contact"

urlpatterns = [
	path("", CreateForm.as_view()),
	path("admin/contact/", AdminContactReader.as_view()),
	path("admin/contact/<int:year>/<int:month>/", AdminContactReader.as_view()),
	path("admin/mass_mail/", AdminSendMassEmail.as_view()),
]
