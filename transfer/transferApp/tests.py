from django.test import SimpleTestCase,TestCase,Client
from django.urls import reverse,resolve
from .views import transferView,user_accountView
from django.contrib.auth.models import User
from .models import user_account,transfer
from transfer.settings import logger

# Create your tests here.

class TestUrls(SimpleTestCase):

    def test_transfer_is_resolved(self):
        url = reverse('transfer')
        self.assertEquals(resolve(url).func.view_class,transferView)
    
    def test_user_account_is_resolved(self):
        url = reverse('accounts')
        self.assertEquals(resolve(url).func.view_class,user_accountView)


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.transfer_url = reverse('transfer')
        self.user_account_url = reverse('accounts')


    def test_transfer_get(self):
        response = self.client.get(self.transfer_url)
        self.assertEquals(response.status_code, 200)

    def test_transfer_post(self):
        #u_account0 = user_account.objects.all().first()
        user0= User.objects.create(username ='testUse1452r',email= 'test@django.com', password ='testpassword'),
        user1= User.objects.create(username ='ttret452r', email='test3@django.com', password ='tes323tpassword'),
        logger.info(f'user0: {user0}')

        u_account0 = user_account.objects.create(
            user= user0[0],
            TIN= 14589632,
            invoice = 600.5,
        )
        u_account1 = user_account.objects.create(
            user= user1[0],
            TIN= 8953146,
            invoice = 800.5,
        )
        t = transfer.objects.create(
            transfer_From = u_account0.TIN,
            transfer_To_TIN = str(u_account1.TIN),
            amount_money = 500.2
        )


    
    def test_user_account_get(self):
        response = self.client.get(self.user_account_url)
        self.assertEquals(response.status_code, 200)

    def test_user_account_post(self):
        u= User.objects.create(username ='ttyujhg', email='test34@django.com', password ='testpassword'),
        response = self.client.post(self.user_account_url,{
            'user': u[0].pk,
            'TIN' : 145896132,
            'invoice' : 500.2,

        })
        logger.info(f'response: {response.content}')
        self.assertEqual(response.status_code, 201)
