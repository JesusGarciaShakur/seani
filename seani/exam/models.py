from django.db import models

from django.contrib.auth.models import User
from career.models import Career
from library.models import Module, Question

# Create your models here.
class Stage(models.Model):
    stage = models.IntegerField(
        verbose_name = "Etapa",
    )
    application_date = models.DateField(
        verbose_name = "Fecha de Aplicacion"
    )

    def month(self):
        months = [
            'enero', 'febrero', 'marzo', 
            'abril', 'mayo', 'junio', 'julio', 
            'agosto', 'septiembre', 'octubre',  
            'noviembre', 'diciembre'
            ]
        return months[self.application_date.month - 1]
    month.short_description = 'Mes'
    
    def year(self):
        return self.application_date.year
    year.short_description = 'Año'
    
    def __str__(self):
        return f"{ self.stage } - { self.month() } { self.year() }"
    
    class Meta:
        verbose_name = "etapa"
        verbose_name_plural = "etapas"

class Exam(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    modules = models.ManyToManyField(Module, through='ExamModule')
    questions = models.ManyToManyField(Question, through = 'Breakdown')
    score = models.FloatField(default = 0.0)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

class ExamModule(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    score = models.FloatField(default=0.0)

class Breakdown(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=5, default = '_')
    correct = models.CharField(max_length=5, default = '_')