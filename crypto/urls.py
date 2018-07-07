from django.conf.urls import url
from . import views

app_name='crypto'

urlpatterns = [
    
    url(r'^sell/$',views.sell_block,name="sell"),
    url(r'^dashboard/$',views.dashboard,name="dashboard"),
    #url(r'^error/$',views.error,name="error"),
]
