from django.urls import path
from .views import AdvertismentList, register, endreg, UserUpdateView, UserView, AdvertismentCreate, AdvertismentUpdate, \
    AdvertismentDetail, CommentCreate, comment_accept, comment_delete, subscribe
# from .views import UserUpdateView, CategoryList
from django.contrib.auth.views import LoginView, LogoutView
# from .views import upgrade_me, subscribe, unsubscribe, restriction_num_posts


urlpatterns = [
    path('', AdvertismentList.as_view(), name='advertisments'),
    path('register/', register, name="register"),
    path('activation_code_form/', endreg, name="endreg"),
 #   path('', activation, name='activation'),
    #
    # path('',   cache_page(60)(PostListSearch.as_view()), name='post_search'),
    path('<int:pk>/', AdvertismentDetail.as_view(), name='advertisment'),
    # path('search/', cache_page(60)(PostListSearch.as_view()), name='post_search'),
    path('add/', AdvertismentCreate.as_view(), name='advertisment_create'),
    path('<int:pk>/edit/', AdvertismentUpdate.as_view(), name='advertisment_update'),
    path('<int:pk>/comment/', CommentCreate.as_view(), name='comment_create'),
    path('<int:pk>/accept/', comment_accept, name='comment_accept'),
    path('<int:pk>/delete/', comment_delete, name='comment_delete'),
    path('user/', UserView.as_view(), name='user'),
    #path('login/', LoginView.as_view(), name='login'),
    #path('logout/', LogoutView.as_view(), name='logout'),
    # path('sign/signup/', BaseRegisterView.as_view(), name='signup'),
    # path('upgrade/', upgrade_me, name='upgrade'),
    path('<int:pk>/profile/', UserUpdateView.as_view(), name='profile'),
    # path('categories/', CategoryList.as_view(), name='categories'),
    path('subscribe/', subscribe, name='subscribe'),
    # path('scategories/<int:pk>/unsubscribe/', unsubscribe, name='unsubscribe'),
    # path('error/', restriction_num_posts, name='restriction_num_posts'),
]
