from django.urls import path
from .views.Region.views import *
from .views.Municipio.views import *
from .views.Nacionalidad.views import *
from .views.Discapacidad.views import *
from .views.Persona.views import *

app_name = 'appInfancia'
urlpatterns = [
    # Region
    path('Region/list', RegionListView.as_view(), name='region_list'),
    path('Region/Create', RegionCreateView.as_view(), name='region_create'),
    path('Region/edit/<int:pk>/', RegionUpdateView.as_view(), name='region_edit'),
    path('Region/delete/<int:pk>/', RegionDeleteView.as_view(), name='region_delete'),

    # Municipio
    path('Municipio/list', MunicipioListView.as_view(), name='municipio_list'),
    path('Municipio/Create', MunicipioCreateView.as_view(), name='municipio_create'),
    path('Municipio/edit/<int:pk>/', MunicipioUpdateView.as_view(), name='municipio_edit'),
    path('Municipio/delete/<int:pk>/', MunicipioDeleteView.as_view(), name='municipio_delete'),

    # Nacionalidad
    path('Nacionalidad/list', NacionalidadListView.as_view(), name='nacionalidad_list'),
    path('Nacionalidad/Create', NacionalidadCreateView.as_view(), name='nacionalidad_create'),
    path('Nacionalidad/edit/<int:pk>/', NacionalidadUpdateView.as_view(), name='nacionalidad_edit'),
    path('Nacionalidad/delete/<int:pk>/', NacionalidadDeleteView.as_view(), name='nacionalidad_delete'),

    # Discapacidad
    path('Discapacidad/list', DiscapacidadListView.as_view(), name='discapacidad_list'),
    path('Discapacidad/Create', DiscapacidadCreateView.as_view(), name='discapacidad_create'),
    path('Discapacidad/edit/<int:pk>/', DiscapacidadUpdateView.as_view(), name='discapacidad_edit'),
    path('Discapacidad/delete/<int:pk>/', DiscapacidadDeleteView.as_view(), name='discapacidad_delete'),

    # Persona
    path('Persona/list', PersonaListView.as_view(), name='persona_list'),
    path('Persona/Create', PersonaCreateView.as_view(), name='persona_create'),
    path('Persona/edit/<int:pk>/', PersonaUpdateView.as_view(), name='persona_edit'),
    path('Persona/delete/<int:pk>/', PersonaDeleteView.as_view(), name='persona_delete')

]
