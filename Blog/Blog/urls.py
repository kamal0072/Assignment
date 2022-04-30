
from django.contrib import admin
from django.urls import path,include
from poll import views
from rest_framework.routers import DefaultRouter
from dj_rest_auth.views import PasswordResetView,PasswordResetConfirmView
#creating router object-----------------
# router=DefaultRouter()
# # #register Studentviewset with route
# router.register("blog/",views.BlogpostList,basename='blog')
# # router.register("blog/",views.BlogPostRUD,basename='blog')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',views.BlogpostList.as_view()),
    # path('',include(router.urls)),
    # path('<int:pk>',include(router.urls)),
    path('blog/<int:pk>',views.BlogPostRUD.as_view()),
    path('users/',include('users.urls')),
    path('password-reset/',PasswordResetView.as_view),
    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view()),
]
