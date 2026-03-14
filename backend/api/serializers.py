from rest_framework import serializers
from datetime import date
from .models import TourRegistration, ContactUsForm, SpecialtyTourRegistration, Feedback

class TourRegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            'blank': 'Please enter your first name.',
            'required': 'First name is required.'
        }
    )

    last_name = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            'blank': 'Please enter your last name.',
            'required': 'Last name is required.'
        }
    )

    email = serializers.EmailField(
        required=True,
        allow_blank=False,
        error_messages={
            'blank': 'Please provide your email address.',
            'required': 'Email is required.',
            'invalid': 'Please enter a valid email address.'
        }
    )

    phone_number = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            'blank': 'Please provide a phone number.',
            'required': 'Phone number is required.'
        }
    )

    date = serializers.DateField(
        required=True,
        error_messages={
            'invalid': 'Please enter a valid date (MM-DD-YYYY).',
            'required': 'Date is required.',
        }
    )

    guests = serializers.IntegerField(
        required=True,
        error_messages={
            'invalid': 'Please enter a valid number of guests.',
            'required': 'Number of guests is required.'
        }
    )

    minors = serializers.IntegerField(
        required=True,
        error_messages={
            'invalid': 'Please enter a valid number of minors.',
            'required': 'Number of minors is required.'
        }
    )

    notes = serializers.CharField(
        required=False,
        allow_blank=True
    )

    class Meta:
        model = TourRegistration
        fields = '__all__'

    # Ensure guests >= 1
    def validate_guests(self, value):
        if value < 1:
            raise serializers.ValidationError("Number of guests must be at least 1.")
        return value

    # Ensure minors >= 0
    def validate_minors(self, value):
        if value < 0:
            raise serializers.ValidationError("Number of minors cannot be negative.")
        return value
    
    # Ensure the tour date is not the day of or before for historical regular
    def validate_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("The requested tour date cannot be in the past.")
        return value

class SpecialtyTourRegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            'blank': 'Please enter your first name.',
            'required': 'First name is required.'
        }
    )

    last_name = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            'blank': 'Please enter your last name.',
            'required': 'Last name is required.'
        }
    )

    email = serializers.EmailField(
        required=True,
        allow_blank=False,
        error_messages={
            'blank': 'Please provide your email address.',
            'required': 'Email is required.',
            'invalid': 'Please enter a valid email address.'
        }
    )

    phone_number = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            'blank': 'Please provide a phone number.',
            'required': 'Phone number is required.'
        }
    )

    date = serializers.DateField(
        required=True,
        error_messages={
            'invalid': 'Please enter a valid date (MM-DD-YYYY).',
            'required': 'Date is required.',
        }
    )

    time = serializers.TimeField(
        required=True,
        error_messages={
            'invalid': 'Please enter a valid time.',
            'required': 'Time is required.',
        }
    )

    guests = serializers.IntegerField(
        required=True,
        error_messages={
            'invalid': 'Please enter a valid number of guests.',
            'required': 'Number of guests is required.'
        }
    )

    minors = serializers.IntegerField(
        required=True,
        error_messages={
            'invalid': 'Please enter a valid number of minors.',
            'required': 'Number of minors is required.'
        }
    )

    tour_type = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            'blank': 'Please select a tour type.',
            'required': 'Tour type is required.'
        }
    )

    notes = serializers.CharField(
        required=False,
        allow_blank=True
    )

    class Meta:
        model = SpecialtyTourRegistration
        fields = '__all__'

    # Ensure guests >= 1
    def validate_guests(self, value):
        if value < 1:
            raise serializers.ValidationError("Number of guests must be at least 1.")
        return value

    # Ensure minors >= 0
    def validate_minors(self, value):
        if value < 0:
            raise serializers.ValidationError("Number of minors cannot be negative.")
        return value
    
    # Ensure the tour date is not the day of or before for historical regular
    def validate_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("The requested tour date cannot be in the past.")
        return value

class ContactUsFormSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            'blank': 'Please enter your first name.',
            'required': 'First name is required.'
        }
    )

    last_name = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            'blank': 'Please enter your last name.',
            'required': 'Last name is required.'
        }
    )

    email = serializers.EmailField(
        required=True,
        allow_blank=False,
        error_messages={
            'blank': 'Please provide your email address.',
            'required': 'Email is required.',
            'invalid': 'Please enter a valid email address.'
        }
    )

    subject = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            'blank': 'Please enter a subject.',
            'required': 'Subject is required.',
            'invalid': 'Please enter a valid subject.'
        }
    )

    message = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            'blank': 'Please enter a message.',
            'required': 'Message is required.',
            'invalid': 'Please enter a valid message.'
        }
    )

    class Meta:
        model = ContactUsForm
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    phone_number = serializers.CharField(required=False, allow_blank=True)
    rating = serializers.IntegerField(
        required=True,
        error_messages={
            'required': 'Rating is required.'
        }
    )

    date = serializers.DateField(
        required=True,
        error_messages={
            'invalid': 'Please enter a valid date (MM-DD-YYYY).',
            'required': 'Date is required.',
        }
    )

    time = serializers.TimeField(
        required=True,
        error_messages={
            'invalid': 'Please enter a valid time.',
            'required': 'Time is required.',
        }
    )

    tour_type = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            'blank': 'Please select a tour type.',
            'required': 'Tour type is required.'
        }
    )
    best_part_message = serializers.CharField(required=False, allow_blank=True)
    improvement_message = serializers.CharField(required=False, allow_blank=True)
    length_message = serializers.CharField(required=False, allow_blank=True)
    topics_message = serializers.CharField(required=False, allow_blank=True)
    source_message = serializers.CharField(required=False, allow_blank=True)
    other_comments = serializers.CharField(required=False, allow_blank=True)
    
    class Meta:
        model = Feedback
        fields = '__all__'