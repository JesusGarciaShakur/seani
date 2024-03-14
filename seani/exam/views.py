from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from .forms import CandidateForm
from .models import Exam
from django.contrib.auth.models import User


def home(request):
    user = request.user
    return render(request, 'exam/home.html', {"user": user})

def question(request, m_id, q_id = 1):
    examn = request.user.exam
    questions = examn.breakdown_set.filter(question__module_id = m_id)
    question = questions[q_id - 1].question
    return render(request, 'exam/question.html', {"question": question})

def add_candidate(request):
    if request.method == "POST":
        form = CandidateForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            stage = form.cleaned_data['stage']
            career = form.cleaned_data['career']

            # crear usuario
            user = User.objects.create_user(username, email, password)
            # editar usuario
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            # crear exam
            exam = Exam.objects.create(user=user, stage=stage, career=career)
            # editar exam
            exam.set_modules()
            exam.set_questions()

            html = """
                <h1>Usuario y examen creado</h1>
                <a href="/exam/add/">Agregar otro</a>
                    """
            return HttpResponse(html)


    form = CandidateForm()
    return render(request, 'exam/add_candidate.html', {"form": form})