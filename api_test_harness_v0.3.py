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

def testData(method, url, jsonbody, expected):
  print "method",method
  print "url",url
  print "jsonbody",jsonbody
  print "expexted",expected
  print
  call = apiurl + '/' + username + url + apiToken

  if method == "GET":
    response = requests.get(call)
  elif method == "PUT":
    response = requests.put(call, data=jsonbody)
  elif method == "POST":
    response = requests.post(call, data=jsonbody)
  elif method == "DELETE":
    response = requests.delete(call)
  elif method == "PATCH":
    response = requests.patch(call, data=jsonbody)
    
  print "---status code---"
  print response.status_code
  print "---headers---"
  print response.headers
  print "---response---"
  print response.text
  print "---json---"
  try:
    print response.json()
  except ValueError:
    print "NO JSON BODY"
    pass
  print "\n\n\n"

  test = printKeyVals(response.text)

apiToken = os.environ.get("DISTELLI_APITOKEN")
username = os.environ.get("DISTELLI_USERNAME")

if apiToken is None or username is None:
  print "You must set environment variables:"
  print "* DISTELLI_USERNAME=Your Distelli username http://docs.distelli.com/docs/finding-your-distelli-username"
  print "* DISTELLI_APITOKEN=Your Distelli API Token http://docs.distelli.com/docs/creating-an-api-token"
  sys.exit()

csv.register_dialect('singlequote', quotechar="'", quoting=csv.QUOTE_ALL)

with open('api_test_data.txt') as test_data:
  reader = csv.reader(test_data, dialect='singlequote')
  for row in reader:
    #print "row",row
    method = row[0]
    url = row[1]
    jsonbody = row[2]
    expected = row[3]
    test = testData(method, url, jsonbody, expected)

#test_data.close()

