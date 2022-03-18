from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register([ketProposal])
admin.site.register([StatusKaprodi,StatusWd3])
admin.site.register([Instansi])
admin.site.register([Semester])
admin.site.register([Jurusan])
admin.site.register([formatFile])