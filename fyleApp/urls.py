from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/getbank/(?P<ifsc>[A-Za-z]{4}\w{7})$',views.get_bank_by_bankname,name='get_bank_by_bankname'),
    url(r'^api/bankdetail/(?P<city>.*)/(?P<bank>.*)$',views.bank_detail,name='bank_detail'),
    
]
