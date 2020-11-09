from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('arm/create', ArmCreateView.as_view(), name='arm_create'),
    path('arm/delete/<int:pk>', ArmDeleteView.as_view(), name='arm_delete'),
    path('arm/list/', ArmListView.as_view(), name='arm_list'),
    #
    path('backup/create', BackupCreateView.as_view(), name='backup_create'),
    path('backup/delete/<int:pk>', BackupDeleteView.as_view(), name='backup_delete'),
    #
    path('client/create', ClientCreateView.as_view(), name='client_create'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),
    path('client/list/', ClientListView.as_view(), name='client_list'),
    #
    path('controller/create', ControllerCreateView.as_view(), name='controller_create'),
    path('controller/delete/<int:pk>', ControllerDeleteView.as_view(), name='controller_delete'),
    path('controller/list/', ControllerListView.as_view(), name='controller_list'),
    #
    path('integrator/create', IntegratorCreateView.as_view(), name='integrator_create'),
    path('integrator/delete/<int:pk>', IntegratorDeleteView.as_view(), name='integrator_delete'),
    path('integrator/list/', IntegratorListView.as_view(), name='integrator_list'),
    #
    path('location/create', LocationCreateView.as_view(), name='location_create'),
    path('location/delete/<int:pk>', LocationDeleteView.as_view(), name='location_delete'),
    path('location/list/', LocationListView.as_view(), name='location_list'),
    #
    path('robot/create', RobotCreateView.as_view(), name='robot_create'),
    path('robot/read/<int:pk>', RobotReadView.as_view(), name='robot_read'),
    path('robot/update/<int:pk>', RobotUpdateView.as_view(), name='robot_update'),
    path('robot/delete/<int:pk>', RobotDeleteView.as_view(), name='robot_delete'),
    #
    path('service/create/<int:pk>', ServiceCreateView.as_view(), name='service_create'),
    path('service/update/<int:pk>', ServiceUpdateView.as_view(), name='service_update'),
    path('service/delete/<int:pk>', ServiceDeleteView.as_view(), name='service_delete'),
]
