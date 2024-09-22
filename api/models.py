from django.db import models


class tbl_login(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    verify_status = models.CharField(max_length=50)
    post = models.CharField(max_length=50, default='default_post')  # Set a default value here
    token = models.CharField(max_length=255)
    flag = models.BooleanField(default=False)

