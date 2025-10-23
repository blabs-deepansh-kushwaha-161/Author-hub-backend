# api/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books")
    book_name = models.CharField(max_length=255)
    manuscript = models.FileField(upload_to="manuscripts/")  # PDF, DOCX, etc.
    front_cover = models.ImageField(upload_to="covers/front/", null=True, blank=True)
    back_cover = models.ImageField(upload_to="covers/back/", null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    mrp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    isbn = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book_name} by {self.user.username}"
