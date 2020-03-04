from django.db import models

class Posting(models.Model):
    useremail = models.CharField(
        max_length = 20,
        default = 'anonymous'
    )
    title = models.CharField(max_length=20)
    content = models.TextField(
        null= True,
        blank = True,
    )
    updated_at = models.DateTimeField(blank=True, null=True)
    