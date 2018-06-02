from django.urls import path,re_path
from . import views

app_name='music'
urlpatterns=[
    #/music/
    path('',views.IndexView.as_view(),name="index"),
    #/music/72
    path('<pk>/',views.DetailView.as_view(),name="detail"),
    #/music/72/favorite
    #path('<int:album_id>/favorite/',views.favorite,name="favorite")
    
    path('album/add',views.AlbumCreate.as_view(),name="Albumadd"),

    path('album/<pk>',views.AlbumUpdate.as_view(),name="AlbumUpdate"),

    path('album/<pk>/Delete',views.AlbumDelete.as_view(),name="delete_album"),


]