from django.urls import path , include
from django.views.generic import TemplateView
from rest_framework.routers import  DefaultRouter
from .views import CustomerViewSet, AccountDetailsViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'account-details', AccountDetailsViewSet)


urlpatterns = [
    path('', TemplateView.as_view(template_name= 'customer/index.html')),
    path('api/', include((router.urls, 'customer')))
    
]