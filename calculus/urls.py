from django.conf.urls import url
from . import views



urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^ratios', views.view_rat,name='ratios'),
    url(r'^grow_fact', views.view_grow_fact,name='grow_fact'),
    url(r'^grow_plan', views.view_grow_plan,name='grow_plan'),
    url(r'^itog', views.view_itog,name='itog'),
    url(r'^inf_mon', views.view_inf_mon,name='inf_mon'),
    url(r'^inf_kva', views.view_inf_kva,name='inf_kva'),
    url(r'^inf_day', views.view_inf_day,name='inf_day'),
    url(r'^inf_coef', views.view_inf_coef,name='inf_coef'),
    url(r'^income', views.view_income,name='income'),
    url(r'^bez_sutok', views.view_bez_sutok,name='bez_sutok'),
    url(r'^dev_mon', views.view_dev_mon,name='dev_mon'),
    url(r'^dev_kva', views.view_dev_kva,name='dev_kva'),
    url(r'^dev_day', views.view_dev_day,name='dev_day'),
]