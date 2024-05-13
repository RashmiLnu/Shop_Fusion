from django.db import models
class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message_type = models.CharField(max_length=255)
    other_message = models.TextField()

    def __str__(self):
        return self.name





