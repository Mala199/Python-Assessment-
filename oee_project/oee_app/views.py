from rest_framework import viewsets
from rest_framework.response import Response
from .models import Machine, ProductionLog
from .serializers import MachineSerializer, ProductionLogSerializer
from rest_framework.decorators import action
from django.db.models import Sum, F, ExpressionWrapper, fields


class OEEViewSet(viewsets.ViewSet):
    queryset = Machine.objects.all()

    @action(detail=True, methods=['get'])
    def calculate_oee(self, request, pk=None):
        machine = self.get_object()
        production_logs = ProductionLog.objects.filter(machine=machine)

        total_available_time = 3 * 8  # Total available time for 3 shifts of 8 hours each
        total_good_products = production_logs.filter(duration=5).count()
        total_bad_products = production_logs.exclude(duration=5).count()
        total_products = total_good_products + total_bad_products
        total_available_operating_time = total_products * 5  # Assuming ideal cycle time is 5 minutes

        unplanned_downtime = total_available_time - total_available_operating_time

        availability = (ExpressionWrapper(
            (total_available_time - unplanned_downtime) / total_available_time * 100,
            output_field=fields.FloatField())
        )

        performance = (ExpressionWrapper(
            (5 * total_products) / total_available_operating_time * 100,
            output_field=fields.FloatField())
        )

        quality = (ExpressionWrapper(
            (total_good_products) / total_products * 100,
            output_field=fields.FloatField())
        )

        oee = availability * performance * quality

        return Response({'oee': oee})


class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer


class ProductionLogViewSet(viewsets.ModelViewSet):
    queryset = ProductionLog.objects.all()
    serializer_class = ProductionLogSerializer


from django.shortcuts import render

# Create your views here.
