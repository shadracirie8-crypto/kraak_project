from django.db import models

class Statistic(models.Model):
    title = models.CharField(max_length=100)  # ex: Participants
    value = models.CharField(max_length=50)   # ex: +100
    icon = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.title} - {self.value}"


class Partner(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='partners/')
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(upload_to='testimonials/', blank=True)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team/')
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.name