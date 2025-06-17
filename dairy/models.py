from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Cow(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='cow_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class MilkProduction(models.Model):
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE, related_name='milk_productions')
    date = models.DateField(default=timezone.now)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.cow.name} - {self.date}: {self.amount}L"

class HealthRecord(models.Model):
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE, related_name='health_records')
    date = models.DateField(default=timezone.now)
    symptoms = models.TextField()
    diagnosis = models.TextField(blank=True, null=True)
    treatment = models.TextField(blank=True, null=True)
    is_urgent = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.cow.name} - {self.date}: {self.symptoms[:50]}"

class Veterinarian(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
