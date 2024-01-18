from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns =[
    path('adddoctor/',views.add_doctor,name='adddoctor'),
    path('viewdoctor/',views.doctor_list,name='doctor_list'),
    path('editdoctor/<int:id>/',views.editdoctor,name='editdoctor'),
    path('deletedoctor/<int:id>/',views.delete_doctor,name='deletedoctor'),
    path('viewdoctordn/',views.sort_dn,name='dn'),
    path('viewdoctorsp/',views.sort_sp,name='sp'),
    path('viewdoctorlo/',views.sort_lo,name='lo'),
    path('viewdoctoreb/',views.sort_eb,name='eb'),
    
#__----------------------------------------------------------------------------------
    path('editappointment/<int:id>/',views.editappointment,name='editappointment'),
    path('addappointment/',views.add_appointment,name='addappointment'),
    path('viewappointment/',views.appointment_list,name='appointment_list'),
    path('deleteappointment/<int:id>/',views.delete_appointment,name='deleteappointment'),
    path('todayschedule/',views.todaysschedule,name='todayschedule'),
    path('viewappointmentdn/',views.sort_adn,name='adn'),
    path('viewappointmentds/',views.sort_ds,name='ds'),
    path('viewappointmenten/',views.sort_en,name='en'),
]