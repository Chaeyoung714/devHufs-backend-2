from django.db import models

class Job(models.Model):
    class JobChoices (models.TextChoices):
        WEB = 'WEB', 'WebDeveloper'
        APP = 'APP', 'AppDeveloper'
        BACKEND = 'BE', 'BackendDeveloper'
        FRONTEND = 'FE', 'FrontendDeveloper'
        DBANALYST = 'DB', 'DBAnalyst'
        GAME = 'GAME', 'GameDeveloper'
        PM = 'PM', 'ProductManager'
        ETC = 'ETC', 'ETC'

    job = models.CharField(choices=JobChoices.choices, default="ETC")