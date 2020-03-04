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

class Comments(models.Model):
    post_num = models.IntegerField(
        null= True,
        blank = True,
    )
    user = models.CharField(
        max_length = 20,
        default = 'anonymous'
    )
    content = models.TextField(
        null= True,
        blank = True,
    )
    updated_at = models.DateTimeField(blank=True, null=True)
    