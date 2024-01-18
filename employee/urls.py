from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .import views




urlpatterns =[
    #path('createemployee/',createemployee.as_view(),name='create_employee'),
    path('addemployee/',views.add_employee,name='addemployee'),
    path('viewemployee/',views.employee_list,name='employee_list'),
    path('editemployee/<int:id>/',views.editemployee,name='editemployee'),
    path('deleteemployee/<int:id>/',views.delete_employee,name='deleteemployee'),
    path('doctorvisit/',views.doctor_visits_view,name='doctorvisit'),
    path('dealsdone/',views.dealsdone,name='dealsdone'),
    path('productlistt/',views.productlist,name='productlistt'),
    path('doctorlistt/',views.doctorlist,name='doctorlistt'),
    path('viewemployeefn/',views.sort_fn,name='fn'),
    path('viewemployeeln/',views.sort_ln,name='ln'),
    path('viewemployeeun/',views.sort_un,name='un'),
    path('viewemployeedj/',views.sort_dj,name='dj'),
    path('profile/<int:pk>/',views.ProfileView.as_view(),name='profile'),

    
    #path('editemployee/<int:pk>/',Employeeedit.as_view(),name='editemployee'),
]