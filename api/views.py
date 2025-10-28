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

# Create your views here.

@csrf_exempt
def submit_feedback(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        time_str = data.get('time', '').strip()  # e.g., "11:00"
        feedback_time = None

        if time_str:
            try:
                hours, minutes = map(int, time_str.split(":"))
                feedback_time = time(hour=hours, minute=minutes)
            except ValueError:
                feedback_time = None  # or handle invalid input

        feedback = Feedback.objects.create(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
            phone_number=data.get('phone_number'),
            rating=data.get('rating'),
            date=data.get('date'),
            time=feedback_time,
            tour_type=data.get('tour_type'),
            best_part_message=data.get('best_part_message', ''),
            improvement_message=data.get('improvement_message', ''),
            length_message=data.get('length_message', ''),
            topics_message=data.get('topics_message', ''),
            source_message=data.get('source_message', ''),
            other_comments=data.get('other_comments', ''),
        )

        # Send feedback to chairs
        send_mail(
            subject=f"[FEEDBACK] Feedback for {feedback.tour_type} ({feedback.date})",
            message=(
                f"Feedback From {feedback.first_name or 'N/A'} {feedback.last_name or 'N/A'}\n"
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
                f"Other comments: {feedback.other_comments or 'N/A'}\n"
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CHAIR_EMAIL],  # change the chair email in .env if needed
        )
        return JsonResponse({'status': 'success', 'message': 'Feedback submitted successfully!'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

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

        # Send email to scheduler
        send_mail(
            subject="[TOUR REGISTRATION] New Standard Historical Tour Registration",
            message=(
                f"Standard Historical Tour Registration From {registration.first_name} {registration.last_name}\n"
                f"Registered on: {date.today()}\n"
                f"Email: {registration.email}\n"
                f"Phone: {registration.phone_number}\n"
                f"Date of Tour: {registration.date}\n"
                f"Guests: {registration.guests}\n"
                f"Minors: {registration.minors}\n"
                f"Notes: {registration.notes or 'None'}"
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            # recipient_list=[settings.SCHEDULER_EMAIL, settings.CHAIR_EMAIL], # change the scheduler email in .env if needed
            recipient_list=[settings.SCHEDULER_EMAIL],  # change the scheduler email in .env if needed
        )

        print(serializer.errors)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register_specialty_tour(request):
    serializer = SpecialtyTourRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        specialty_registration = serializer.save()

        # Send email to scheduler
        send_mail(
            subject=f"[REQUESTED TOUR] New {specialty_registration.tour_type} Tour Request",
            message=(
                f"Specialty Tour Registration From {specialty_registration.first_name} {specialty_registration.last_name}\n"
                f"Registered on: {date.today()}\n"
                f"Email: {specialty_registration.email}\n"
                f"Phone: {specialty_registration.phone_number}\n"
                f"Requested Date of Tour: {specialty_registration.date}\n"
                f"Guests: {specialty_registration.guests}\n"
                f"Minors: {specialty_registration.minors}\n"
                f"Tour Type: {specialty_registration.tour_type}\n"
                f"Tour Group Information & Details: {specialty_registration.notes or 'None'}"
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            # recipient_list=[settings.SCHEDULER_EMAIL, settings.CHAIR_EMAIL],  # change the scheduler email in .env if needed
            recipient_list=[settings.SCHEDULER_EMAIL],  # change the scheduler email in .env if needed

        )

        print(serializer.errors)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def contact_us(request):
    serializer = ContactUsFormSerializer(data=request.data)
    if serializer.is_valid():
        contact_us = serializer.save()
        email_sent = False

        # Try sending the email, but catch any exceptions
        try:
            send_mail(
                subject=f"[GUIDES WEBSITE - CONTACT US] {contact_us.subject}",
                message=(
                    f"From: {contact_us.first_name} {contact_us.last_name} ({contact_us.email})\n\n"
                    f"{contact_us.message}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CHAIR_EMAIL],
                fail_silently=False,
            )
            email_sent = True
        except BadHeaderError:
            return Response(
                {"detail": "Invalid header found in email."},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            # Log the error for debugging (Render will show this in logs)
            print("Email sending failed:", e)

        # Return success even if email fails (frontend won't break)
        return Response({
            "message": "Form submitted successfully.",
            "email_sent": email_sent,
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    # Validation failed
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FeedbackCreateView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer