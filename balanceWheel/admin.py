from django.contrib import admin

from .models import Question, Choice, Category, Subcategory, Result, Branch


class ChoiceInline(admin.StackedInline):
    fk_name = 'question'
    model = Choice
    extra = 3


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'result')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Ветка', {'fields': ['branch']}),
        ('Категории', {'fields': ['category', 'subcategory']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('id', 'question_text', 'branch', 'category', 'subcategory')


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'branch_name',)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'choice_text', 'points', 'value', 'link', 'vote']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name']


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'subcategory_name']
