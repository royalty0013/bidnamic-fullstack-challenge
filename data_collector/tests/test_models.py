from django.test import TestCase
from data_collector.models import ClientData
from django.contrib.auth.models import User

class ClientDateTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='admin')
        self.data1 = ClientData.objects.create(user=user, title="Mr", first_name="Hassan", surname="Braimah",
                                        date_of_birth="1987-03-22", company_name="bidnamic", address="london", telephone="+448393939282",
                                        bidding_settings="High", google_ads_account_id="273737388373733")

    def test_create_data_to_db(self):
        data = self.data1
        self.assertTrue(isinstance(data, ClientData))
        self.assertEqual(str(data), "Mr Hassan")
