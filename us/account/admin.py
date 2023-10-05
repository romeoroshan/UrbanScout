from django.contrib import admin
from .models import User,Contract,History
# Register your models here.
admin.site.register(User)
admin.site.register(Contract)
admin.site.register(History)