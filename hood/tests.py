from django.test import TestCase
from .models import Neighbourhood, Business
from django.contrib.auth.models import User
# Create your tests here.
class BusinessModelTestcase(TestCase):
    @classmethod
    def setUpTestData(cls):
        neighbourhood = Neighbourhood.objects.create(name='Langata')
        user = User.objects.first()
        Business.objects.create(business_name="Dimex", neighbourhood=neighbourhood, email="obewas@gmail.com", industry='Health', user=user)

    def test_string_method(self):

        business = Business.objects.get(id=1)
        expected_string = f"{business.business_name}"
        self.assertEqual(str(business), expected_string)

    def test_get_absolute_url(self):
        business = Business.objects.get(id=1)
        self.assertEqual(business.get_absolute_url(), "/hood/business/1/")

 class NeighbourhoodModelTestcase(TestCase):
 	name = models.CharField(max_length=200, null=True)
    estate = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    occupants_count = models.IntegerField(null=True)
    admin = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def setUpTestData(cls):
    	admin = User.objects.first()
    	Neighbourhood.objects.create(name='Langata', estate='baraka', city='Nairobi', occupants_count=500, admin=admin)


    def test_string_method(self):
    	neighbourhood = Neighbourhood.objects.get(id=1)
    	expected_string = f"{neighbourhood.name}"
    	self.assertEqual(str(neighbourhood), expected_string)


    def test_get_absolute_url(self):
    	neighbourhood = Neighbourhood.objects.get(id=1)
    	self.assertEqual(neighbourhood.get_absolute_url(), '/hood/business/1/')