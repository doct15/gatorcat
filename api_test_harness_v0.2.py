import requests
import json
import os
import sys
import csv

debug=1
apiurl = "https://api.distelli.com"

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
url = '/apps/TestApp1?apiToken='
jsonbody = '{"description":"Test App 1 description"}'
call = apiurl + '/' + username + url + apiToken
#response = requests.put(call, data=jsonbody)
#print (response.text)

#Test GetApp
url = '/apps/TestApp1?apiToken='
call = apiurl + '/' + username + url + apiToken
#response = requests.get(call)

#Test GetRelease
url = '/apps/ipv6utility_py/releases/v3?apiToken='
call = apiurl + '/' + username + url + apiToken
response = requests.get(call)

json_data = json.loads(response.text)

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

csv.register_dialect('singlequote', quotechar="'", quoting=csv.QUOTE_ALL)

with open('api_test_data.txt') as test_data:
  reader = csv.reader(test_data, dialect='singlequote')
  for row in reader:
    print "row",row
    for field in row:
      print "field",field


#test_data.close()

