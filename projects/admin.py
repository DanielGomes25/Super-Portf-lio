from django.contrib import admin
from .models import Profile, Project, Certificate, CertifyingInstitution


# Register your models here.

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Certificate)
admin.site.register(CertifyingInstitution)
