from django.db import models

class Tech(models.Model):
    class TechChoices (models.TextChoices):
        DJANGO = 'Django', 'Django'
        ETC = 'ETC', 'ETC'

    tech = models.CharField(choices=TechChoices.choices, default="ETC")