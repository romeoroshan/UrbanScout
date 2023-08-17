from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register-player/',views.registerPlayer,name='register-player'),
    path('playerhome/',views.playerHome,name="player-home"),
    path('register-club/',views.registerClub,name="register-club"),
    path('clubhome',views.clubHome,name="clubhome"),
    path('logout/',views.logout,name="logout"),
    path('player-club',views.playerClub,name="player-club"),
    path('edit-player-profile',views.editPlayerProfile,name="edit-player-profile"),
    path('deleteUser/<int:delete_id>',views.deleteUser,name="deleteUser"),
    path('updateStauts/<int:update_id>',views.updateStatus,name="updateStatus")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)