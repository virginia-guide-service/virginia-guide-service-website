from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics, permissions
from .models import Feedback
from .serializers import TourRegistrationSerializer, ContactUsFormSerializer, SpecialtyTourRegistrationSerializer, FeedbackSerializer
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from datetime import date
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import Feedback
import json
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import Feedback
from django.db.models import Avg, Count
from datetime import date, time
import os
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactUsFormSerializer

# Create your views here.

# pull from os for froms
MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN")
MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
SCHEDULER_EMAIL = os.getenv("EMAIL_SCHEDULER_RECEIVER")
CHAIR_EMAIL = os.getenv("EMAIL_CHAIR_RECEIVER")


def is_exec_team(user):
    return user.is_staff  # or use a custom field for exec access


@user_passes_test(is_exec_team)
def feedback_dashboard(request):
    today = date.today()
    month_feedback = Feedback.objects.filter(
        submitted_at__month=today.month,
        submitted_at__year=today.year
    )

    stats = month_feedback.aggregate(
        avg_rating=Avg('rating'),
        total_feedback=Count('id')
    )

    return render(request, 'feedback_dashboard.html', {
        'feedback_list': month_feedback.order_by('-submitted_at'),
        'stats': stats,
    })


@api_view(['POST'])
def register_tour(request):
    serializer = TourRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        registration = serializer.save()

        reply_to = f"{registration.first_name} {registration.last_name} <{registration.email}>"

        # full message with reply note to scheduler
        full_message = (
            f"Standard Historical Tour Registration from {registration.first_name} {registration.last_name}\n\n"
            f"Registered on: {date.today()}\n"
            f"Email: {registration.email}\n"
            f"Phone: {registration.phone_number}\n"
            f"Date of Tour: {registration.date}\n"
            f"Guests: {registration.guests}\n"
            f"Minors: {registration.minors}\n"
            f"Notes: {registration.notes or 'None'}\n\n"
            f"---\n[You can reply directly to this email and it will go to "
            f"{registration.first_name} {registration.last_name} <{registration.email}>]"
        )

        print("Sending standard tour registration email...")
        print("To:", SCHEDULER_EMAIL)
        print("Subject: [TOUR REGISTRATION] New Standard Historical Tour Registration")
        print("Message:", full_message)

        # send to scheduler
        try:
            response = requests.post(
                f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
                auth=("api", MAILGUN_API_KEY),
                data={
                    "from": f"Virginia Guides Website <no-reply@{MAILGUN_DOMAIN}>",
                    "to": SCHEDULER_EMAIL,
                    "subject": "[TOUR REGISTRATION] New Standard Historical Tour Registration",
                    "text": full_message,
                    "h:Reply-To": reply_to
                }
            )
            print("Mailgun response:", response.status_code, response.text)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print("Mailgun error:", str(e))
            return Response({"error": f"Failed to send email: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        # confirmation email to user
        confirmation_message = (
            f"Hi {registration.first_name},\n\n"
            "Thank you for registering for a Standard Historical Tour with the Virginia Guides Service!\n\n"
            "We have received your submission. If you have any questions or need to make changes, please email our schedulers (scheduler@virginiaguides.org).\n\n"
            f"Your submitted information:\n"
            f"Date of Tour: {registration.date}\n"
            f"Guests: {registration.guests}\n"
            f"Number of Children in Grade K-8: {registration.minors}\n"
            f"Notes: {registration.notes or 'None'}\n\n"
        )

        # send to user that registered
        try:
            requests.post(
                f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
                auth=("api", MAILGUN_API_KEY),
                data={
                    "from": f"Virginia Guides <no-reply@{MAILGUN_DOMAIN}>",
                    "to": registration.email,
                    "subject": "[TOUR REGISTRATION CONFIRMATION]",
                    "text": confirmation_message
                }
            )
        except requests.exceptions.RequestException as e:
            print("Failed to send confirmation email to user:", str(e))

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register_specialty_tour(request):
    serializer = SpecialtyTourRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        specialty_registration = serializer.save()

        reply_to = f"{specialty_registration.first_name} {specialty_registration.last_name} <{specialty_registration.email}>"

        # full message for schedulers
        full_message = (
            f"Specialty Tour Registration from {specialty_registration.first_name} {specialty_registration.last_name}\n\n"
            f"Registered on: {date.today()}\n"
            f"Email: {specialty_registration.email}\n"
            f"Phone: {specialty_registration.phone_number}\n"
            f"Requested Date of Tour: {specialty_registration.date}\n"
            f"Time of Tour: {specialty_registration.time}\n"
            f"Guests: {specialty_registration.guests}\n"
            f"Minors: {specialty_registration.minors}\n"
            f"Tour Type: {specialty_registration.tour_type}\n"
            f"Tour Group Information & Details: {specialty_registration.notes or 'None'}\n\n"
            f"---\n[You can reply directly to this email and it will go to "
            f"{specialty_registration.first_name} {specialty_registration.last_name} <{specialty_registration.email}>]"
        )

        print("Sending specialty tour registration email...")
        print("To:", SCHEDULER_EMAIL)
        print("Subject:", f"[REQUESTED TOUR] New {specialty_registration.tour_type} Tour Request")
        print("Message:", full_message)

        # send to scheduler
        try:
            response = requests.post(
                f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
                auth=("api", MAILGUN_API_KEY),
                data={
                    "from": f"Virginia Guides Website <no-reply@{MAILGUN_DOMAIN}>",
                    "to": SCHEDULER_EMAIL,
                    "subject": f"[REQUESTED TOUR] New {specialty_registration.tour_type} Tour Request",
                    "text": full_message,
                    "h:Reply-To": reply_to
                }
            )
            print("Mailgun response:", response.status_code, response.text)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print("Mailgun error:", str(e))
            return Response({"error": f"Failed to send email: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        # confirmation email to user
        confirmation_message = (
            f"Hi {specialty_registration.first_name},\n\n"
            f"Thank you for requesting a {specialty_registration.tour_type} Tour with the Virginia Guides Service!\n\n"
            "We have received your submission and will be in touch soon to confirm your tour details. If you have any questions or need to make changes, please email our schedulers (scheduler@virginiaguides.org).\n\n"
            f"Your submitted information:\n"
            f"Tour Type: {specialty_registration.tour_type}\n"
            f"Date of Tour: {specialty_registration.date}\n"
            f"Time of Tour: {specialty_registration.time}\n"
            f"Guests: {specialty_registration.guests}\n"
            f"Number of Children in Grade K-8: {specialty_registration.minors}\n"
            f"Notes: {specialty_registration.notes or 'None'}\n\n"
        )

        # send to user that registered
        try:
            requests.post(
                f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
                auth=("api", MAILGUN_API_KEY),
                data={
                    "from": f"Virginia Guides <no-reply@{MAILGUN_DOMAIN}>",
                    "to": specialty_registration.email,
                    "subject": "[SPECIALTY TOUR REQUEST RECIEVED]",
                    "text": confirmation_message
                }
            )
        except requests.exceptions.RequestException as e:
            print("Failed to send confirmation email to user:", str(e))

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def submit_feedback(request):
    serializer = FeedbackSerializer(data=request.data)
    if not serializer.is_valid():
        # Return field-level validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    feedback = serializer.save()  # This automatically creates the Feedback instance
    
    # Email sending logic (unchanged)
    reply_to = f"{feedback.first_name or ''} {feedback.last_name or ''} <{feedback.email or ''}>"
    full_message = (
        f"Feedback from {feedback.first_name or 'N/A'} {feedback.last_name or 'N/A'}\n\n"
        f"Email: {feedback.email or 'N/A'}\n"
        f"Phone: {feedback.phone_number or 'N/A'}\n"
        f"Tour Type: {feedback.tour_type or 'N/A'}\n"
        f"Date of Tour: {feedback.date or 'N/A'}\n"
        f"Time of Tour: {feedback.time or 'N/A'}\n"
        f"Rating: {feedback.rating or 'N/A'}\n"
        f"Best Part: {feedback.best_part_message or 'N/A'}\n"
        f"What needs improvement: {feedback.improvement_message or 'N/A'}\n"
        f"How was the length of the tour?: {feedback.length_message or 'N/A'}\n"
        f"Wanted topics or places: {feedback.topics_message or 'N/A'}\n"
        f"How did you hear about Guides: {feedback.source_message or 'N/A'}\n"
        f"Other comments: {feedback.other_comments or 'N/A'}\n\n"
        f"---\n[If the person who submitted the form provided their contact information, you can reply directly to this email and it will send to their email ({feedback.first_name or 'N/A'} {feedback.last_name or 'N/A'} <{feedback.email or 'N/A'})>"
    )

    try:
        response = requests.post(
            f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
            auth=("api", MAILGUN_API_KEY),
            data={
                "from": f"Virginia Guides Website <no-reply@{MAILGUN_DOMAIN}>",
                "to": CHAIR_EMAIL,
                "subject": f"[FEEDBACK] Feedback for {feedback.tour_type} ({feedback.date})",
                "text": full_message,
                "h:Reply-To": reply_to
            }
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return Response({"error": f"Failed to send email: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # Confirmation email to the user
    try:
        confirmation_message = (
            f"Hi {feedback.first_name},\n\n"
            f"Your feedback has been received successfully.\n\n"
            f"Thank you for taking the time to provide feedback for your {feedback.tour_type} tour on {feedback.date}.\n\n"
            f"We truly value your input and use it to improve our tours and experiences."
        )

        requests.post(
            f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
            auth=("api", MAILGUN_API_KEY),
            data={
                "from": f"Virginia Guides <no-reply@{MAILGUN_DOMAIN}>",
                "to": feedback.email,
                "subject": "Feedback Received",
                "text": confirmation_message
            }
        )
    except requests.exceptions.RequestException as e:
        print("Failed to send confirmation email to user:", str(e))

    return Response({"status": "success"}, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def contact_us(request):
    serializer = ContactUsFormSerializer(data=request.data)
    if serializer.is_valid():
        contact_us = serializer.save()

        # Debug logging before sending
        print("Attempting to send email via Mailgun...")
        print("From:", f"{contact_us.first_name} {contact_us.last_name} <postmaster@{MAILGUN_DOMAIN}>")
        print("To: rjd8wv@virginia.edu")
        print("Subject:", f"[GUIDES WEBSITE - CONTACT US] {contact_us.subject}")
        print("Message:", contact_us.message)
        print("MAILGUN_API_KEY exists?", MAILGUN_API_KEY is not None)

        reply_to = f"{contact_us.first_name} {contact_us.last_name} <{contact_us.email}>"
        full_message = f"{contact_us.message}\n\n---\n[You can reply directly to this email, and it will go to {contact_us.first_name} {contact_us.last_name} <{contact_us.email}>]"

        # Send email to chairs via Mailgun
        try:
            response = requests.post(
                f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
                auth=("api", MAILGUN_API_KEY),
                data={
                    "from": f"{contact_us.first_name} {contact_us.last_name} via Virginia Guides Website <no-reply@{MAILGUN_DOMAIN}>",
                    "to": CHAIR_EMAIL,
                    "subject": f"[GUIDES WEBSITE - CONTACT US FORM] {contact_us.subject}",
                    "text": full_message,
                    "h:Reply-To": reply_to,
                }
            )

            print("Mailgun response:", response.status_code, response.text)
            response.raise_for_status()

        except requests.exceptions.RequestException as e:
            print("Mailgun error:", str(e))
            return Response(
                {"error": f"Failed to send email: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        # confirmation email to user
        confirmation_message = (
            f"Hi {contact_us.first_name},\n\n"
            f"Thank you for reaching out to us. We have received your message:\n\n"
            f"Subject: {contact_us.subject}\n"
            f"Message: {contact_us.message}\n\n"
            "Our chairs will review your message and get back to you as soon as possible."
        )

        # send to user that registered
        try:
            requests.post(
                f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
                auth=("api", MAILGUN_API_KEY),
                data={
                    "from": f"Virginia Guides <no-reply@{MAILGUN_DOMAIN}>",
                    "to": contact_us.email,
                    "subject": "Contact Us Message Recieved",
                    "text": confirmation_message
                }
            )
        except requests.exceptions.RequestException as e:
            print("Failed to send confirmation email to user:", str(e))

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # If serializer is invalid
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# TESTING ALL THINGS MAIL -- LOCAL DEV ONLY
# @api_view(['POST'])
# def contact_us(request):
#     serializer = ContactUsFormSerializer(data=request.data)
#     if serializer.is_valid():
#         contact_us = serializer.save()
    
#         # Send email to chairs
#         send_mail(
#             subject=f"[GUIDES WEBSITE - CONTACT US] {contact_us.subject}",
#             message=(
#                 f"From: {contact_us.first_name} {contact_us.last_name} ({contact_us.email})\n\n"
#                 f"{contact_us.message}"
#             ),
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             recipient_list=[settings.CHAIR_EMAIL],  # change the chair email in .env
#         )

#         print(serializer.errors)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
#     print(serializer.errors)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FeedbackCreateView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer