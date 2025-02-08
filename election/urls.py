from django.urls import path
from . import views

urlpatterns = [
    path('polling_unit_selection/', views.polling_unit_selection, name='polling_unit_selection'),
    path('polling_unit_results/', views.polling_unit_results, name='polling_unit_results'),
    path('lga_results/', views.lga_results, name='lga_results'),
    path('add_results/', views.add_polling_unit_results, name='add_polling_unit_results'),
]
