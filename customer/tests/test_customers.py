from rest_framework import status
from rest_framework.test import APIClient

class TestCreateCustomer:
    def test_if_user_is_annonymous_returns_401(self):
        #Arrange

        #Act
        client = APIClient()
        response = client.post('/api/customers/', {'account_number': 2345354,
                                     'date_of_birth': '2000-01-01', 
                                     'title':'Mr',
                                     'address': 'myaddress'})
        
        #Assert

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self):
        #Arrange
        #Act
        client = APIClient()
        client.force_authenticate(user={})
        response = client.post('/api/account-details/', {'account_number': 2345354,
                                     'date_of_birth': '2000-01-01', 
                                     'title':'Mr',
                                     'address': 'myaddress'})
        
        #Assert

        assert response.status_code == status.HTTP_403_FORBIDDEN