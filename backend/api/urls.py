from django.urls import path
from .views import register_specialty_tour, contact_us, FeedbackCreateView, submit_feedback, backups_dashboard

urlpatterns = [
    # Legacy endpoint intentionally disabled; the frontend uses register-specialty-tour/.
    # path('register-tour/', register_tour),
    path('register-specialty-tour/', register_specialty_tour),
    path('contact-us/', contact_us),
    path('submit-feedback/', submit_feedback, name='submit-feedback'),
    path('backups-dashboard/', backups_dashboard, name='backups-dashboard'),
]
