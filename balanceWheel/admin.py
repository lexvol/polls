from django.contrib import admin
from .models import Question

@admin.register(Question)
class Question(admin.ModelAdmin):
    list_display = ['id', 'question_text', 'pub_date']
    list_filter = ['id', 'pub_date']
