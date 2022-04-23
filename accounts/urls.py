from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django import views
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'profile',profile_viewsets,'profile')

urlpatterns = [ 


    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls')),

    path('customer_registration/',customer_registration,name='customer_registration'),
   
    path('customer_login/',TokenObtainPairView.as_view(),name='tokenobtainpair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='tokenrefresh'),
    # path('<int:pk>/',profile_view,name='profile-view'),
    path('trainer_registration/',trainer_registration,name='trainer_registration'),
    
    path('trainer_login/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),

   
    
]