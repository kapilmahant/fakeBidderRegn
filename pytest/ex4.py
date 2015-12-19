import pytest 
import requests


#
#@pytest.mark.parametrize("url","headers1" [
#    ("http://192.168.150.110:10001/fakebidder/","{'Content-Type':'application/json', 'cookie':'returnBidAmount=5.2345'}"),
#    ("http://192.168.150.110:10001/fakebidder/","{'Content-Type':'application/json', 'cookie':'returnBidAmount=5.2345'}"),
#    ("http://192.168.150.110:10001/fakebidder/","{'Content-Type':'application/json', 'cookie':'returnBidAmount=5.2345'}"),
#    ("http://192.168.150.110:10001/fakebidder/","{'Content-Type':'application/json', 'cookie':'returnBidAmount=5.2345'}")
#])
#
#

default_url="http://192.168.150.110:10001/fakebidder/"


@pytest.mark.parametrize(("url_arg","headers_arg"), [
    (default_url,"{'Content-Type':'application/json', 'cookie':'returnBidAmount=5.2345'}"),
    (default_url,"{'Content-Type':'application/json', 'cookie':'returnBidAmount=5.2345'}"),
    (default_url,"{'Content-Type':'application/json', 'cookie':'returnBidAmount=5.2345'}"),
    (default_url,"{'Content-Type':'application/json', 'cookie':'returnBidAmount=5.2345'}")
])

def test_foo(url_arg, headers_arg):
    print "\n\t printing url - "+ url_arg 
    print "\n\t printing headers1 - "+ headers_arg  
    assert 200 == 200
 


#
#
#
##def test_post_request(url, arguments, headers, cookies, predictions):
#def test_post_request(url1,headers1):
#    print "\n\t printing url - "+ url1  
#    response = requests.post(
#        "http://192.168.150.110:10001/fakebidder/",
#
#        data={"accept_language":"en-us,en;q=0.5","auction_id":"e59cf7f965e5634770bec77b8e234e8447da8992","country":"ca","domain_name":"www.bender-testing.com","ip_address":"137.122.14.11","page_url":"","secure":0,"network_user_id":"bid=3.02^robot_tracking=8498431437585754.94","xff":"209.232.44.21","region":"on","user_id":"9c051f73a0b28f3130fcedf6372f75c90f3a89cc","publisher_id":99999,"site_id":42,"designated_site_url":"www.bender-testing.com","user_agent":"python-requests/2.2.1 CPython/2.7.5 Linux/2.6.18-308.13.1.el5","denied_ad_types":[14001,14004,14006,14007,14008,14009,14010,14011,14012,14013,14020,14021,14022,14002,14003,14005,14014,14015,14016,14017,14018,14019],"render_status":"js","site_size_session_count":1,"user_tz":-400,"page_position":"unknown","expandable":0,"supported_tech":[],"private":0,"preferred_seats":["r1"],"pmp":{"deals":[{"id":"TA-99999-r1","floor":0.20000000298023224,"seats":["r1"],"type":2}]},"device":{"os":"25043","dclass":40,"carrier":"Other"},"ad_size_id":1,"ad_width_px":468,"ad_height_px":60,"alt_ads":[],"instl":0}, 
#
#        headers={'Content-Type':'application/json' , 
#                 'cookie': 'returnBidAmount=5.2345' }
#    )
#    print response
#
#
#    assert response.status_code == 200
#    #assert response.text == "foo" 
    #assert response.json()["price"] == 5.5 


