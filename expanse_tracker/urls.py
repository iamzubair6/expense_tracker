from sys import implementation
from django.urls import path
from.views import *

app_name = 'expense_history'

urlpatterns = [
    path('', expanse, name='expanse'),
    path("type_add/", newType, name='newType'),
    path("expanse_history/", history, name='history'),
    path("edit/<int:id>/", edit, name='edit'),
    path("delete/<int:id>/", delete, name='delete'),



]
