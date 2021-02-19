from rest_framework import serializers
from production.models import Production

class ProductionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Production
        fields = ('id','env','Q1','Q2','Q3','Q4','LQA','Status')
