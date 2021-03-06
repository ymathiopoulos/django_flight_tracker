"""django_flight_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache, cache_control


urlpatterns = [
    path('admin/', admin.site.urls),
]

# Use include() to add paths from the home application
urlpatterns += [
    path('home/', include('home.urls')),
]

# Add URL maps to redirect the base URL to our application
urlpatterns += [
    path('', RedirectView.as_view(url='/home/', permanent=True)),
]

# Use static() to add url mapping to serve static files during development (only)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# TODO: I added the following to not save cache of the static files, check if any of them are needed
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, view=cache_control(no_cache=True, must_revalidate=True)(serve))
#
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, view=never_cache(serve))
