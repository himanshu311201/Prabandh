from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('product/',views.Productform,name="product"),
    path('ajax/load_subcat/', views.load_subcat, name='ajax_load_subcat'),
    path('wedding/<my_id>',views.Weddings,name="product"),
    path('Image/<prod_id>',views.Prod_view,name="Prod_view"),
<<<<<<< HEAD
    path('search/',views.search_subcat,name="search"),
    path("NewImage/",views.AddImage,name="addImage"),
=======
    path("NewImage/",views.NewImage,name="NewImage"),
>>>>>>> 154d2101f9160d2391c44d2c688c11fcda6a7483
    path('subcategory/<str:mysubcat>',views.search_subcat,name="Search subcat"),
    path('Image/',views.load,name="load"),
    path('deleteImage/',views.deleteImage,name="Delete Image"),
]
