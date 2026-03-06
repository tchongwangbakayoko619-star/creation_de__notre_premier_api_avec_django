from django.urls import path
from api.api.view_set import ProductViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

""" 
default_router est utilisé pour les API RESTful complètes, offrant des fonctionnalités avancées telles que la prise en charge de différentes actions (list, create, retrieve, update, destroy) et la génération automatique d'URL basées sur les conventions REST. Il est idéal pour les applications nécessitant une gestion complète des ressources.

simple_router est plus léger et uttilise pour les simples operation de lecture (list et retrieve) sans les fonctionnalités avancées de création, mise à jour ou suppression. Il est adapté pour les cas où vous souhaitez exposer uniquement des points de terminaison de lecture pour vos ressources.
"""
router= DefaultRouter()
router.register('V1/product', ProductViewSet, basename='product')
urlpatterns = router.urls