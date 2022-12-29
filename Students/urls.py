from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('about', AboutView.as_view(), name="about"),
    path('contact', ContactView.as_view(), name="contact"),
    path('courses', CoursesView.as_view(), name="courses"),
    path('events', EventsView.as_view(), name="events"),
    path('pricing', PricingView.as_view(), name="pricing"),
    path('trainers', TrainersView.as_view(), name="trainers"),
    path('course-detail', CourseDetailView.as_view(), name="course-detail"),
    path('login', login_view, name="login"),
    path('signup', signup, name="signup"),
    path('logout', logout, name="logout"),
]
