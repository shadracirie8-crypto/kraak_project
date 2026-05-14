from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title


class ServiceDetail(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='details')
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return f"{self.service.title} - {self.title}"