from django.urls import path
from .views import hello_world
from .views import register_tour, register_specialty_tour, contact_us, FeedbackCreateView, submit_feedback, feedback_dashboard

urlpatterns = [
    path('hello/', hello_world),
    path('register-tour/', register_tour),
    path('register-specialty-tour/', register_specialty_tour),
    path('contact-us/', contact_us),
    path('submit-feedback/', submit_feedback, name='submit-feedback'),
    path('feedback-dashboard/', feedback_dashboard, name='feedback-dashboard'),
]
