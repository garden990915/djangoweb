from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('notice/',views.notice_list, name='notice_list'),
    path('notice/<int:pk>', views.notice_view, name='notice_view'),
    path('notice/add/',views.notice_add),
    path('notice/remove/<int:pk>', views.notice_remove),
    path('program/', views.notice_program),
]

