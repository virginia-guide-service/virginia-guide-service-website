from django.db import models

# Create your models here.

class TourRegistration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    date = models.DateField()
    guests = models.PositiveIntegerField()
    minors = models.PositiveIntegerField(default=0)
    tour_type = models.CharField(max_length=100, default="Standard Historical Tour")
    notes = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.date}"

class SpecialtyTourRegistration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    minors = models.PositiveIntegerField(default=0)
    tour_type = models.CharField(max_length=100, default="Standard Historical Tour")
    notes = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.date}"
    
class ContactUsForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.TextField(blank=True)
    message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.message}"

class Feedback(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    rating = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()
    tour_type = models.CharField(max_length=100, default="Standard Historical Tour")
    best_part_message = models.TextField(blank=True)
    improvement_message = models.TextField(blank=True)
    length_message = models.TextField(blank=True)
    topics_message = models.TextField(blank=True)
    source_message = models.TextField(blank=True)
    other_comments = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.first_name} {self.last_name} ({self.submitted_at.date()})"
    

class SpecialtyTourBackup(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField(default=1)
    minors = models.PositiveIntegerField(default=0)
    tour_type = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.tour_type} on {self.date}"

class FeedbackBackup(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    tour_type = models.CharField(max_length=100, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    best_part_message = models.TextField(blank=True)
    improvement_message = models.TextField(blank=True)
    length_message = models.TextField(blank=True)
    topics_message = models.TextField(blank=True)
    source_message = models.TextField(blank=True)
    other_comments = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.tour_type} ({self.date})"


class ContactUsBackup(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"
