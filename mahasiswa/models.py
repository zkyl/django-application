from django.db import models

# Create your models here.
class MahasiswaModel(models.Model):
    GENDER = [
        ('LK','laki-laki'),
        ('PR', 'perempuan')
    ]
    nim = models.CharField(max_length=10)
    nama = models.CharField(max_length=255)
    gender = models.CharField(max_length=2, choices=GENDER)

    def __str__(self):
        return self.nama