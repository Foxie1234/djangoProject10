from rest_framework import  serializers
from mydjpr.models import TestModel


class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestModel
        fields = '__all__'
