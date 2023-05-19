from django.urls import path,include
from  . import views
from django.conf import settings
from django.conf.urls.static import static
from blog.views import ResetPasswordView
from django.contrib.auth import views as auth_views



urlpatterns = [
   path('',views.index,name='home'),
   path('<slug:url>/',views.postdetails,name='postdetails'),
   path('category/<str:url>/',views.category,name='category'),
   path('newsletter/',views.newsletter,name='newsletter'),
   path('search',views.search,name='search'),
   path('blog/contact/',views.contact,name='contact'),
   path('tag/<slug:tag_slug>',views.index),
   path('user/<slug:author>/',views.author,name="user"),
   path('ckeditor/',include('ckeditor_uploader.urls')),
   path('signup',views.signup,name="signup"),
   path('login',views.loginhandle,name="login"),
   path('logout', views.handelLogout, name="handleLogout"),
   path('blog/account/',views.account,name="account"),
   path('profile/upload/',views.updateprofile),
   path('blog/password-reset/', ResetPasswordView.as_view(), name='password_reset'),
   path('blog/password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
   path('blog/password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
   path('blog/terms-conditions/',views.terms,name="terms"),
   path('blog/privacy-policy/',views.privacy,name="privacy"),
   path('blog/about/',views.about,name="about")
  
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)