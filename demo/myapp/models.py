from django.db import models

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(max_length=50, default="Name")
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}: {self.status}"

    def save(self, *args, **kwargs):
        super(MyModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "My Model"
        verbose_name_plural = "My Models"