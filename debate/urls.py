from . import views
from user import views as user_views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='debate-index'),
    path('register/', user_views.register, name='user-register'),
    path('profile/', user_views.profile, name='user-profile'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user-logout'),
    path('create/', views.create, name='debate-create'),
    path('motion/<int:motion_id>/', views.spec_motion, name='debate-motion'),
    path('argument/<int:motion_id>', views.make_arg, name='debate-argument'),
    path('arg/<int:arg_id>', views.spec_argument, name='debate-spec-arg'),
    path('point/<int:arg_id>', views.make_point, name='debate-makep'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)