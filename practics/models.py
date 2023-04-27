from django.db import models


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comments'


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'
