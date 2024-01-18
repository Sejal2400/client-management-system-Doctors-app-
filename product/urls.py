from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .import views
#from .views import createproduct

urlpatterns = [
    
    path('productlist/',views.product_list,name='product_list'),
    #path('create/',createproduct.as_view(),name='create'),
    path('newproduct/',views.productadd,name='newproduct'),
    path('delete/<int:id>',views.delete_data,name='delete'),
    path('edit/<int:id>',views.editproduct,name='editproduct'),
    # path('productcount/',views.count_products,name='product_count'),
    path('sortproductn/',views.sort_pn,name='pn'),
    path('sortproductc/',views.sort_cn,name='cn'),
    path('sortproductp/',views.sort_pp,name='pp'),
    path('sortproducteb/',views.sort_eb,name='enb'),

]