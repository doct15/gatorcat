import requests
import json
import os
import sys
#import jsonpickle

debug=1

#class User(object):
#    def __init__(self, name, username):
#        self.name = name
#        self.username = username

#class ComplexEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, complex):
#             return [obj.real, obj.imag]
#         # Let the base class default method raise the TypeError
#         return json.JSONEncoder.default(self, obj)

def printKeyVals(data, indent=0):
    if isinstance(data, list):
        print
        for item in data:
            printKeyVals(item, indent+1)
    elif isinstance(data, dict):
        print
        for k, v in data.iteritems():
            print "    " * indent, k + ":",
            printKeyVals(v, indent + 1)
    else:
        print data

apiToken = os.environ.get("DISTELLI_APITOKEN")
username = os.environ.get("DISTELLI_USERNAME")

if apiToken is None or username is None:
  print "You must set environment variables:"
  print "* DISTELLI_USERNAME=Your Distelli username http://docs.distelli.com/docs/finding-your-distelli-username"
  print "* DISTELLI_APITOKEN=Your Distelli API Token http://docs.distelli.com/docs/creating-an-api-token"
  sys.exit()

#Test CreatApp 
apiurl = "https://api.distelli.com"
url = '/apps/TestApp1?apiToken='
jsonbody = '{"description":"Test App 1 description"}'
call = apiurl + '/' + username + url + apiToken

#response = requests.put(call, data=jsonbody)
#print (response.text)

#Test GetApp
apiurl = "https://api.distelli.com"
url = '/apps/TestApp1?apiToken='
jsonbody = '{"description":"Test App 1 description"}'
call = apiurl + '/' + username + url + apiToken

response = requests.get(call)

json_data = json.loads(response.text)

#u = User(**json_data)
#u = jsonpickle.decode(json_data)
#u = ComplexEncoder().encode(json_data)
#u = json.load(response.text)

print "---status code---"
print response.status_code
print "---headers---"
print response.headers
print "---text---"
print response.text
print "---json---"
print response.json()
print "---json_data---"
print json_data
print "---response.to_str---"
print response.text
#print "---decoded?---"
#print u

test = printKeyVals(json_data)





