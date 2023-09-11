from django.urls import path
from .views import getAll,getDetail,post,patch,put,delete,today,lastTen,status



urlpatterns = [
    path('getall/',getAll.as_view()),
    path('getdetail/<int:forid>', getDetail.as_view()),
    path('post/', post.as_view()),
    path('patch/<int:forid>', patch.as_view()),
    path('put/<int:forid>', put.as_view()),
    path('delete/<int:forid>', delete.as_view()),
    path('today/', today.as_view()),
    path('lastten/',lastTen.as_view()),
    path('status/',status.as_view())
]