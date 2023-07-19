from django.urls import path
from document_management.views import (
    user_login,
    user_registration,
    document_list_create,
    document_retrieve_update_delete,
    get_document_versions,
)

urlpatterns = [
    path('login/', user_login, name='user-login'),
    path('register/', user_registration, name='user-registration'),
    path('documents/', document_list_create, name='document-list-create'),
    path('documents/<int:pk>/', document_retrieve_update_delete, name='document-retrieve-update-delete'),
    path('documents/<int:pk>/versions/', get_document_versions, name='document-versions'),
]
