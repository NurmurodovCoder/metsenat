from django.urls import path, include
from rest_framework import routers
from .views import StudentView, UniversitetView, DonatorView, DonationsView, dashboard


router = routers.DefaultRouter()
router.register(r'student', StudentView)
router.register(r'donator', DonatorView)
# router.register(r'donat', DonatView)
router.register(r'universitet', UniversitetView)

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', dashboard, name='dashboard'),
    path('donations/', DonationsView.as_view, name='dashboard'),

]
