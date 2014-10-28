from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from demo_mandrill.models import Correo


class AdminCorreos(SummernoteModelAdmin):
	model = Correo


admin.site.register(Correo, AdminCorreos)