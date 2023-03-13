from django.contrib import admin
from .models import Hodregister,teacherregister,studentregister,leave,exam,mark


# Register your models here.

admin.site.register(Hodregister)
admin.site.register(teacherregister)
admin.site.register(studentregister)
admin.site.register(leave)
admin.site.register(exam)
admin.site.register(mark)
