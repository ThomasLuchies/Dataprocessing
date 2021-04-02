# Create your models here.
from django.db import models

class Classification(models.Model):
    neoReferenceId = models.IntegerField()
    name = models.CharField(max_length=60)
    absoluteMagnitude = models.IntegerField()
    estDiaInKmMin = models.IntegerField()
    estDiaInKmMax = models.IntegerField()
    estDiaInMMin = models.IntegerField()
    estDiaInMMax = models.IntegerField()
    estDiaInMilesMin = models.IntegerField()
    estDiaInMilesMax = models.IntegerField()
    estDiaInFeetMin = models.IntegerField()
    estDiaInFeetMax = models.IntegerField()

    def __str__(self):
        return self.name

class Orbits(models.Model):
    name = models.CharField(max_length=60)
    epoch = models.IntegerField()
    orbitAxis = models.IntegerField()
    orbitEccentricity = models.IntegerField()
    orbitInclanation = models.IntegerField()
    periphelionArgument = models.IntegerField()
    nodeLongitude = models.IntegerField()
    meanAnomaly = models.IntegerField()
    absoluteMagnitude = models.IntegerField()
    periphelionDistance = models.IntegerField()
    estDiaInKm = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

class Impacts(models.Model):
    fullName = models.CharField(max_length=60)
    periodStart = models.IntegerField()
    periodEnd = models.IntegerField()
    possibleImpacts = models.IntegerField()
    cumulativeImpactProbability = models.IntegerField()
    asteroidVelocity = models.IntegerField()
    absoluteMagnitude = models.IntegerField()
    cumulativePalermoScale = models.IntegerField()
    maximumPalermoScale = models.IntegerField()
    def __str__(self):
        return self.fullname