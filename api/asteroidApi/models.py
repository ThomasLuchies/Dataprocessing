# Create your models here.
from django.db import models


class Classifications(models.Model):
    neoReferenceId = models.IntegerField()
    name = models.CharField(max_length=60)
    absoluteMagnitude = models.FloatField()
    estDiaInKmMin = models.FloatField()
    estDiaInKmMax = models.FloatField()
    estDiaInMMin = models.FloatField()
    estDiaInMMax = models.FloatField()
    estDiaInMilesMin = models.FloatField()
    estDiaInMilesMax = models.FloatField()
    estDiaInFeetMin = models.FloatField()
    estDiaInFeetMax = models.FloatField()

    def __str__(self):
        return self.name


class Orbits(models.Model):
    name = models.CharField(max_length=60)
    epoch = models.IntegerField()
    orbitAxis = models.FloatField()
    orbitEccentricity = models.FloatField()
    orbitInclanation = models.FloatField()
    periphelionArgument = models.FloatField()
    nodeLongitude = models.FloatField()
    meanAnomaly = models.FloatField()
    absoluteMagnitude = models.FloatField()
    periphelionDistance = models.FloatField()
    estDiaInKm = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Impacts(models.Model):
    fullName = models.CharField(max_length=60)
    periodStart = models.IntegerField()
    periodEnd = models.IntegerField()
    possibleImpacts = models.IntegerField()
    cumulativeImpactProbability = models.FloatField()
    asteroidVelocity = models.FloatField()
    absoluteMagnitude = models.FloatField()
    cumulativePalermoScale = models.FloatField()
    maximumPalermoScale = models.FloatField()

    def __str__(self):
        return self.fullname
