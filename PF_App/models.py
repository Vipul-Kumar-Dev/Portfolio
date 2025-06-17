from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    preferred_contact = models.CharField(
        max_length=10,
        choices=[('email', 'Email'), ('phone', 'Phone')],
        default='email'
    )
    best_time = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"


class FAQQuestion(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    question = models.TextField()

    def __str__(self):
        return f"Question from {self.name}"
