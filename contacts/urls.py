from django.urls import path
from .views import (ContactListView,ContactDetailView,SearchView,ContactCreateView,ContactUpdateView,ContactDeleteView,SignupView)

urlpatterns = [
    path('',ContactListView.as_view(),name='home'),
    path('detail/<int:pk>/', ContactDetailView.as_view(), name='detail'),
    path('search/', SearchView.as_view(), name='search'),
    path('contacts/create/', ContactCreateView.as_view(), name='create'),
    path('contacts/update/<int:pk>/', ContactUpdateView.as_view(), name='update'),
    path('contacts/delete/<int:pk>/', ContactDeleteView.as_view(), name='delete'),
    path('signup/', SignupView.as_view(), name='signup')
]
