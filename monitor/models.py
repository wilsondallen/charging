from django.db import models


class Camera(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)

    class Meta:
        db_table = 'camera'