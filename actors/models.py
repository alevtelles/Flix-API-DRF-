from django.db import models


NATIONALITY_CHOICES = (
    ('EUA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil'),
    ('ARG', 'Argentina'),
    ('MEX', 'México'),
    ('COL', 'Colômbia'),
    ('ES', 'Espanha'),
    ('FRA', 'França'),
    ('ITA', 'Itália'),
    ('GER', 'Alemanha'),
    ('UK', 'Reino Unido'),
    ('PR', 'Porto Rico'),
    ('AU', 'Austrália'),
    ('ZA', 'África do Sul'),
    ('NZ', 'Nova Zelândia'),

)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name   