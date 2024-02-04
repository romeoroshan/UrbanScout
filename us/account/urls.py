from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import UserListCreateView
urlpatterns = [
    
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register-player/',views.registerPlayer,name='register-player'),
    path('playerhome/<int:user_id>',views.playerHome,name="player-home"),
    path('scouthome/<int:user_id>',views.scoutHome,name="scout-home"),
    path('register-club/',views.registerClub,name="register-club"),
    path('clubhome/<int:user_id>',views.clubHome,name="clubHome"),
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
    path('PlayerScout',views.playerScout,name="PlayerScout"),
    path('ShortlistScout/<int:scout_id>',views.shortlistScout,name="ShortlistScout"),
    path('ScoutPlayer',views.scoutPlayer,name="ScoutPlayer"),
    path('ClubScout',views.clubScout,name="ClubScout"),
    path('ShortlistClubScout/<int:scout_id>',views.shortlistClubScout,name="ShortlistClubScout"),
    path('ScoutClub',views.scoutClub,name="ScoutClub"),
    path('AcceptRequest/<int:req_id>',views.acceptRequest,name="AcceptRequest"),
    path('ScoutPlayerEdit/<int:update_id>',views.scoutPlayerEdit,name="ScoutPlayerEdit"),
    path('ScoutClubEdit/<int:update_id>',views.scoutClubEdit,name="ScoutClubEdit"),
    path('PostImage',views.postImage,name="PostImage"),
    path('PostVideo',views.postVideo,name="PostVideo"),
    path('Contract/<int:user_id>',views.contract,name="Contract"),
    path('EditContract/<int:user_id>',views.contractNegotiation,name="EditContract"),
    path('EditContractClub/<int:user_id>',views.contractNegotiationClub,name="EditContractClub"),
    path('AcceptContract/<int:user_id>',views.acceptContract,name="AcceptContract"),
    path('AcceptContractClub/<int:user_id>',views.acceptContractClub,name="AcceptContractClub"),
    path('RejectContract/<int:user_id>',views.rejectContract,name="RejectContract"),
    path('RejectContractClub/<int:user_id>',views.rejectContractClub,name="RejectContractClub"),
    path('validate_email/', views.validate_email, name='validate_email'),
    path('like_feed_ajax/<int:feed_id>/', views.like_feed_ajax, name='like_feed_ajax'),
    path('check_like_status/<int:feed_id>/', views.check_like_status, name='check_like_status'),
    path('follow/<int:followed_id>',views.following_funtion,name="following"),
    path('is_follow/<int:followed_id>',views.is_following,name="is_following"),
    path('following_feeds',views.following_feeds,name="following_feeds"),
    path('search_by_name/<str:name>/',views.searchByName,name="search_by_name"),
    path('follower/<int:user_id>',views.follower,name="follower"),
    path('payment/',views.payment,name="payment"),
    path('followingUsers/<int:user_id>',views.followingUsers,name="followingUsers"),
    path('likesUsers/<int:feed_id>',views.likesUsers,name="likesUsers"),
    path('notificationUsers/<int:user_id>',views.notificationUsers,name="notificationUsers"),
    path('deleteNotification/<int:user_id>',views.deleteNotification,name="deleteNotification"),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('contract/pdf/<int:player_id>/', views.render_contract_as_pdf, name='render_contract_as_pdf'),
    path('contact/<int:user_id>',views.contact,name="contact"),
    path('tour',views.tour,name="tour"),
    path('tournaments',views.tournaments,name="tournaments"),
    path('enrolled',views.enrolled,name="enrolled"),
    path('enrol_tour/<int:tour_id>',views.enrol_tour,name="enrol_tour"),
    path('hosted_tour',views.hosted_tour,name="hosted_tour"),
    path('cancel_tour<int:tour_id>',views.cancel_tour,name="cancel_tour"),
    path('tour_participants/<int:tour_id>',views.tour_participants,name="tour_participants"),
    path('trial',views.trial,name="trial"),
    path('trial_list',views.trial_list,name="trial_list"),
    path('api/your-model/', UserListCreateView.as_view(), name='your-model-list-create'),
    path('enroltrial/<int:tour_id>',views.enroltrial,name="enroltrial"),
    path('enrolled_trials',views.enrolled_trials,name="enrolled_trials"),
    # path('auth/login/google-oauth2/', views.google_login, name='google_login'),
    # path('auth/login/google-oauth2/callback/', views.google_callback, name='google_callback'),

    # Google OAuth2 login
    # path('social-auth/login/google-oauth2/', views.google_login, name='google_login'),
    # Google OAuth2 callback
    # path('social-auth/login/google-oauth2/callback/', views.google_callback, name='google_callback'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)