from django.urls import path
from .views import HomeView, NoticiaCreate, NoticiaView, NoticiaUpdate, NoticiaDelete, NoticiaDataView
from .views import WhatsAppAccountView, WhatsAppAccountCreate, WhatsAppAccountUpdate, WhatsAppAccountDelete

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('noticia_archive_day/<int:year>/<int:month>/<int:day>', NoticiaDataView.as_view(month_format='%m'),
         name='noticia_data'),
    path('noticia_list/', NoticiaView.as_view(), name='noticia_list'),
    path('noticia_create_form/', NoticiaCreate.as_view(), name='noticia_create_form'),
    path('noticia_update_form/<int:pk>', NoticiaUpdate.as_view(), name='noticia_update_form'),
    path('noticia_confirm_delete/<int:pk>', NoticiaDelete.as_view(), name='noticia_confirm_delete'),
    path('whatsapp_account_list/', WhatsAppAccountView.as_view(), name='whatsapp_account_list'),
    path('whatsapp_account_create_form/', WhatsAppAccountCreate.as_view(), name='whatsapp_account_create_form'),
    path('whatsapp_account_update_form/<int:pk>', WhatsAppAccountUpdate.as_view(), name='whatsapp_account_update_form'),
    path('whatsapp_account_delete_confirmation/<int:pk>', WhatsAppAccountDelete.as_view(), name='whatsapp_account_delete_confirmation'),  
    
]
