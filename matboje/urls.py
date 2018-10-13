from django.urls import path

from matboje.views import *

app_name = 'matboje'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', MatbojDetailView.as_view(), name='detail'),
    path('<int:pk>/results/', MatbojResults.as_view(), name='results'),
    path('<int:pk>/submitpage/', MatbojSubmitPage.as_view(), name='submit_page'),
    path('<int:pk>/SubmitMatch/', SubmitMatch, name='submit_match'),
    path('<int:pk>/submitpage/SubmitMatch/', SubmitMatch, name='submit_match'),
    path('<int:pk>/MatbojAdmin/', MatbojAdminView.as_view(), name='matboj_admin'),
]
