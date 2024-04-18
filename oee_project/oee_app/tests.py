from django.test import TestCase
from rest_framework.test import APIClient
from .models import Machine, ProductionLog


class OEECalculationTestCase(TestCase):
    def setUp(self):
        self.machine = Machine.objects.create(machine_name="Machine 1", machine_serial_no="12345")
        self.production_log_1 = ProductionLog.objects.create(cycle_no="CN001", unique_id="001",
                                                             material_name="Material A", machine=self.machine,
                                                             start_time="2024-04-01 08:00:00",
                                                             end_time="2024-04-01 08:05:00", duration=5)
        self.production_log_2 = ProductionLog.objects.create(cycle_no="CN002", unique_id="002",
                                                             material_name="Material B", machine=self.machine,
                                                             start_time="2024-04-01 09:00:00",
                                                             end_time="2024-04-01 09:07:00", duration=7)

    def test_oee_calculation(self):
        client = APIClient()
        response = client.get(f'/machines/{self.machine.id}/calculate_oee/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['oee'], 100)  # Assuming all products are good


class APITestCase(TestCase):
    def setUp(self):
        self.machine = Machine.objects.create(machine_name="Machine 1", machine_serial_no="12345")
        self.production_log = ProductionLog.objects.create(cycle_no="CN001", unique_id="001",
                                                           material_name="Material A", machine=self.machine,
                                                           start_time="2024-04-01 08:00:00",
                                                           end_time="2024-04-01 08:05:00", duration=5)

    def test_machine_list(self):
        client = APIClient()
        response = client.get('/machines/')
        self.assertEqual(response.status_code, 200)

    def test_production_log_list(self):
        client = APIClient()
        response = client.get('/productionlogs/')
        self.assertEqual(response.status_code, 200)

    def test_calculate_oee(self):
        client = APIClient()
        response = client.get(f'/machines/{self.machine.id}/calculate_oee/')
        self.assertEqual(response.status_code, 200)


from django.test import TestCase

# Create your tests here.
