from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns =[
    path('adddeals/',views.add_deal,name='add_deals'),
    path('viewdeals/',views.deal_list,name='deal_list'),
    path('editdeal/<int:id>/',views.editdeals,name='editdeal'),
    path('deletedeal/<int:id>/',views.delete_deals,name='delete_deal'),
    path('sortdoctor/',views.sort_docname,name='sortdoctor'),
    path('sortproduct/',views.sort_pname,name='sortproduct'),
    path('sortdate/',views.sort_date,name='sortdate'),
    path('sortquan/',views.sort_quan,name='sortquan'),
    path('sortentby/',views.sort_entby,name='sortentby'),



    
]