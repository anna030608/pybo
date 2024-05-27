from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subjects']

# Register your models here.
admin.site.register(Question, QuestionAdmin)

