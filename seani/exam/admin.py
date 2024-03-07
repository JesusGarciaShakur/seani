from django.contrib import admin

from .models import Stage, Exam, ExamModule

@admin.register(Stage)
class StateAdmin(admin.ModelAdmin):
    list_display = ['stage', 'month', 'year']

class ExamModuleInLine(admin.TabularInline):
    model = ExamModule
    extra = 1

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['user', 'career', 'stage', 'score']
    list_filter = ['career', 'stage']
    inlines = [ExamModuleInLine]