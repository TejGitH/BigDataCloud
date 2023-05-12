from rest_framework import serializers
from incentives.models import Incentive

class IncentiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incentive
        fields = '__all__'

        