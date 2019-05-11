from rest_framework import serializers
from .models import Professor

class ProfessorSerializer (serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Professor
        fields = '__all__'