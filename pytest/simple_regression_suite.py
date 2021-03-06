import json 
import pytest 
import requests
import ast


default_url="http://192.168.150.110:10001/fakebidder/"

data={"accept_language":"en-us,en;q=0.5","auction_id":"e59cf7f965e5634770bec77b8e234e8447da8992","country":"ca","domain_name":"www.bender-testing.com","ip_address":"137.122.14.11","page_url":"","secure":0,"network_user_id":"bid=3.02^robot_tracking=8498431437585754.94","xff":"209.232.44.21","region":"on","user_id":"9c051f73a0b28f3130fcedf6372f75c90f3a89cc","publisher_id":99999,"site_id":42,"designated_site_url":"www.bender-testing.com","user_agent":"python-requests/2.2.1 CPython/2.7.5 Linux/2.6.18-308.13.1.el5","denied_ad_types":[14001,14004,14006,14007,14008,14009,14010,14011,14012,14013,14020,14021,14022,14002,14003,14005,14014,14015,14016,14017,14018,14019],"render_status":"js","site_size_session_count":1,"user_tz":-400,"page_position":"unknown","expandable":0,"supported_tech":[],"private":0,"preferred_seats":["r1"],"pmp":{"deals":[{"id":"TA-99999-r1","floor":0.20000000298023224,"seats":["r1"],"type":2}]},"device":{"os":"25043","dclass":40,"carrier":"Other"},"ad_size_id":1,"ad_width_px":468,"ad_height_px":60,"alt_ads":[],"instl":0} 

@pytest.mark.parametrize(("url","payload","params","headers"), [
    (default_url,data,{'sessionKey': '9ebbd0b25760557393a43064a92bae539d962103', 'format': 'xml', 'platformId': 1},{'Content-Type':'application/json', 'cookie':'returnBidAmount=5.2345'})
])

def test_foo(url, payload, params, headers):
    print "\n\t printing url - "+ url
    print "\n\t printing data - "+ json.dumps(payload)
    print "\n\t printing params - "+ str(params) 
    print "\n\t printing headers - "+ str(headers)  


    print isinstance(payload , dict)
    print isinstance(headers , dict)

    response = requests.post(
             url, 
             params=params,
             headers=headers,
             data=json.dumps(payload)
    )

   
    print response
    print response.text
    assert response.status_code == 200
    #assert 200  == 200

    # requests.post(url, params=params, data=json.dumps(data), headers=headers)

    #assert response.text == "foo" 
    #assert response.json()["price"] == 5.5 


#
#
#
##def test_post_request(url, arguments, headers, cookies, predictions):
#def test_post_request(url1,headers1):
#    print "\n\t printing url - "+ url1  
#    response = requests.post(
#        "http://192.168.150.110:10001/fakebidder/",
#
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

@pytest.fixture
def before():
    print "------- before"

def test_ehlo(before):
    print "------- in test : test_ehlo"
    assert 200 == 200 # for demo purposes


def test_bar(before):
    print "------- in test : test_bar"
    assert 200 == 200 # for demo purposes


@pytest.mark.parametrize(("input", "output","expected"), [
    ("3+5", 8, True), 
    ("2+4", 6, True),
    ("6*9", 42, False )
])


#@pytest.mark.usefixtures("before") 
def test_eval(input, output, expected):
    if (expected):
        assert eval(input) == output
    else:
        assert pytest.mark.xfail( eval(input) == output ) 



@pytest.mark.usefixtures("startup") 
def test_1():
    print ("\n\t inside test1")

def test_2(startup):
    print ("\n\t inside test2")

def test_3(startup):
    print ("\n\t inside test3")



def findDiff(d1, d2, path=""):
    print "======= top level keys for d1 " , d1.keys()  
    print "======= top level keys for d2 " , d2.keys()  
    for k in d1.keys():
        print " top level checking for key ", k 
        
        if not d2.has_key(k):
            print path, ":"
            print k + " as key not in d2", "\n"
        else:
            if type(d1[k]) is dict:
                if path == "":
                    path = k
                else:
                    path = path + "->" + k
                findDiff(d1[k],d2[k], path)
            else:
                if d1[k] != d2[k]:
                    print path, ":"
                    print " - ", k," : ", d1[k]
                    print " + ", k," : ", d2[k] 





def validate_prediction(response,predictions):
    assert response.status_code == 200,  "value was odd, should be even"
    assert 200 == 200
    
    response_dict = {} 
    response_dict['headers'] = response.headers
    response_dict['status_code']  = response.status_code
    response_dict['text']    = json.loads(response.text)
     

    print response.text
    #print dict(response.text) 
    print "predictions------->   ", predictions
    print "response_dict -------> " , response_dict
    
    findDiff(predictions,response_dict) 
    #findDiff(response_dict,predictions) 

    #if predictions.viewitems() < response_dict.viewitems() : 
    #if ( predictions.viewitems().issubset(response_dict.viewitems()) ): 
    # Currently compares only keys and NOT values 
    if ( set(predictions).issubset(response_dict) ): 
        assert True ,  "subset " 


