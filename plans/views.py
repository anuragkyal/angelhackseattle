from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .models import Plan
from .serializers import PlanSerializer


class PlanViewSet(viewsets.ModelViewSet):
    """API endpoint for listing and creating sprints."""

    queryset = Plan.objects.all()
    serializer_class = PlanSerializer