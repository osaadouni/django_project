from django.urls import reverse, resolve
from django.test import TestCase 

from ..views import EmployeeList
from ..models import Employee
from ..forms import EmployeeForm

from jobtitles.models import JobTitle 


class EmployeeListTests(TestCase):
    def setUp(self):
        jobtitle = JobTitle.objects.create(name='Femme Fatale')
        self.employee = Employee.objects.create(first_name='Jane', last_name='Doe', email='jane.doe@example.com', job_title=jobtitle) 
        url = reverse('employees:employee-list')
        self.response = self.client.get(url)

    def test_view_employee_list_status_code(self):
        self.assertEqual(self.response.status_code, 200)


    def test_view_employee_list_resolve_url(self):
        view = resolve('/employees/')
        self.assertEqual(view.func.view_class, EmployeeList)
