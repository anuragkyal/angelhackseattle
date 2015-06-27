from rest_framework import serializers

from .models import Plan

class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = ('hotel_name', 'hotel_price', 'rental_name', 'rental_price', 'user_id')