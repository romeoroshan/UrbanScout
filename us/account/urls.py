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
    path('updateStauts/<int:update_id>',views.updateStatus,name="updateStatus"),
    path('selectType/',views.selectType,name='selectType'),
    path('club-selected/',views.club_selected,name='club-selected'),
    path('player-selected/',views.player_selected,name='player-selected'),
    path('CompleteProfile/',views.CompleteProfile,name='CompleteProfile'),
    path('CompleteClub/',views.CompleteClub,name="CompleteClub"),
    path('EditClub/',views.editClub,name="EditClub"),
    path('RegisterScout/',views.registerScout,name="RegisterScout"),
    path('email/',views.sendEmail,name="email"),
    path('ShowInterest/<int:club_id>',views.showInterest,name="ShowInterest"),
    path('ClubPlayer',views.clubPlayer,name="ClubPlayer"),
    path('ShortlistPlayer/<int:player_id>',views.shortlistPlayer,name="ShortlistPlayer"),
    # path('auth/login/google-oauth2/', views.google_login, name='google_login'),
    # path('auth/login/google-oauth2/callback/', views.google_callback, name='google_callback'),

    # Google OAuth2 login
    # path('social-auth/login/google-oauth2/', views.google_login, name='google_login'),
    # Google OAuth2 callback
    # path('social-auth/login/google-oauth2/callback/', views.google_callback, name='google_callback'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)