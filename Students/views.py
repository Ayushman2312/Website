from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password, check_password
from django.views.generic import TemplateView,CreateView

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        student = StudentData.GetStudentByUsername(username)
        if student:
            check = check_password(password, student.password)
            if check:
                request.session['username'] = username
                return redirect('home')
            else:
                messages.info(request, "Invalid Password or Username")
                return redirect("login")
        else:
            messages.info(request, "Username does not exist")
            return redirect("login")
    return render(request, 'login.html')
def signup(request):
    if request.method == "POST":
        studentname = request.POST.get('studentname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        password = request.POST.get('password')
        # pass
        if StudentData.objects.filter(student_name=studentname).exists():
            messages.info(request, "Username already exists")
            return redirect('signup')
        else:
            student = StudentData(
                student_name=studentname,
                username=username,
                password=password,
                email=email, 
                phone_no=phoneno
            )
            student.password = make_password(student.password)
            student.save()
            return redirect('/')

    return render(request, 'signup.html')

def logout(request):
    request.session.clear()
    return redirect('home')

class HomeView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = StudentData.objects.all()
        context['username'] = self.request.session.get('username')
        # print("you are: ", self.request.session.get('username'))
        return context


class AboutView(TemplateView):
    template_name = "about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ContactView(TemplateView):
    template_name = "contact.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CoursesView(TemplateView):
    template_name = "courses.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CourseDetailView(TemplateView):
    template_name = "courses-details.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EventsView(TemplateView):
    template_name = "events.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PricingView(TemplateView):
    template_name = "pricing.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TrainersView(TemplateView):
    template_name = "trainers.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



    