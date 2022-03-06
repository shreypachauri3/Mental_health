from typing import final
from urllib import response
from django.contrib import admin

from landing.models import basicinfo, final, questions,res

# Register your models here.
admin.site.register(questions)
admin.site.register(basicinfo)
admin.site.register(res)
