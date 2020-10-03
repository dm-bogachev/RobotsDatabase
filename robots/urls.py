from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('arm/create', ArmCreateView.as_view(), name='arm_create'),
    path('backup/create', BackupCreateView.as_view(), name='backup_create'),
    path('client/create', ClientCreateView.as_view(), name='client_create'),
    path('controller/create', ControllerCreateView.as_view(), name='controller_create'),
    path('integrator/create', IntegratorCreateView.as_view(), name='integrator_create'),
    path('location/create', LocationCreateView.as_view(), name='location_create'),
    path('robot/create', RobotCreateView.as_view(), name='robot_create'),
    path('service/create', ServiceCreateView.as_view(), name='service_create'),

]