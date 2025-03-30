from django.db import models

# Create your models here.
class Text(models.Model):
    text = models.TextField(default="Это текст по умолчанию.")

    def __str__(self):
        return self.text