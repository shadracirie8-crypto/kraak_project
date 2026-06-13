from django.db import models

class Program(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    duration = models.CharField(max_length=50)  # ex: 3 mois
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(
        upload_to='programs/',
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ProgramFeature(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='features')
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title