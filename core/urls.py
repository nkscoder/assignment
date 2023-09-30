from .views import *
from django.urls import path


urlpatterns = [

    path('', home, name='home'),
    path('video/<int:video_id>/', watch_video, name='watch_video'),
    path('video/add_comment/', add_comment, name='add_comment'),
    path('video/add_like/<int:video_id>/', add_like, name='add_like'),
    path('<str:session_username>/profile/', profile, name='profile'),
    path('<str:session_username>/dashboard/', dashboard, name='dashboard'),
    path('add_subscriber/<viewer>/', add_sub, name='add_subscriber'),
    path('upload/', upload_video, name='upload'),
    path('edit_video/<int:video_id>', edit_video, name='edit_video'),
    path('delete_video/', delete_video, name='delete_video'),
    path('update_details/', update_details, name='update_details'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('search/', search, name='search'),
]