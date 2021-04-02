from rest_framework import serializers
from .models import Classification, Impacts, Orbits


class ClassificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Classification
        fields = (
        'neoReferenceId', 'name', 'absoluteMagnitude', 'estDiaInKmMin', 'estDiaInKmMax', 'estDiaInMMin', 'estDiaInMMax',
        'estDiaInMilesMin', 'estDiaInMilesMax', 'estDiaInFeetMin', 'estDiaInFeetMax')


class ImpactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Impacts
        fields = (
        'fullName', 'periodStart', 'periodEnd', 'possibleImpacts', 'cumulativeImpactProbability', 'asteroidVelocity',
        'absoluteMagnitude', 'cumulativePalermoScale', 'maximumPalermoScale')


class OrbitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orbits
        fields = (
        'name', 'epoch', 'orbitAxis', 'orbitEccentricity', 'orbitInclanation', 'periphelionArgument', 'nodeLongitude',
        'meanAnomaly', 'absoluteMagnitude', 'periphelionDistance', 'estDiaInKm')
