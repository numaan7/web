from django.urls import path
from  . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   path('',views.index),
   path('category/<slug:url>/',views.category),
   path('<slug:url>/',views.postdetails),
   path('newsletter',views.newsletter),
   path('search',views.search),
   path('blog/contact',views.contact),
   path('tag/<slug:tag_slug>/',views.index, name='post_tag'), 
   path('author/<slug:author>/',views.author)
   
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)