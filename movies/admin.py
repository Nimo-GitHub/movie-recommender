from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin 
from .models import User


class ViewAdmin(ImportExportModelAdmin):
	pass	 

admin.site.register(Movie, ViewAdmin)
admin.site.register(User)


