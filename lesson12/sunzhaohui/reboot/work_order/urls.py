# _*_ encoding:utf-8 _*_
__author__ = 'sunzhaohui'
__date__ = '2019-08-18 16:19'

from django.urls import path,re_path
from .views import WorkOrderApplyView,WorkOrderListView,WorkOrderDetailView,WorkOrderHistoryView

app_name='workorder'
urlpatterns = [
    path("apply/",WorkOrderApplyView.as_view(),name='apply'),
    path("list/",WorkOrderListView.as_view(),name='list'),
    re_path('detail/(?P<pk>[0-9]+)?/$',WorkOrderDetailView.as_view(),name='detail'),
    path("history/",WorkOrderHistoryView.as_view(),name='history'),
    ]