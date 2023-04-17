from django.contrib import admin
from .models import Question, Choice, Category, Subcategory


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Категории', {'fields': ['category', 'subcategory']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'category', 'subcategory')

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'choice_text', 'scores', 'vote']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name']


@admin.register(Subcategory)
class Subcategory(admin.ModelAdmin):
    list_display = ['id', 'subcategory_name']
