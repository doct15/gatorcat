import requests
import json
import os
import sys
import csv
from jq import jq

debug=1
apiurl="https://api.distelli.com"

def main():
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
      testname = row[0]
      method = row[1]
      url = row[2]
      jsonbody = row[3]
      expected = row[4]
      test = testData(testname, method, url, jsonbody, expected)

  #test_data.close()


def printKeyVals(data, indent=0):
    if isinstance(data, list):
        #print
        for item in data:
            printKeyVals(item, indent+1)
    elif isinstance(data, dict):
        #print
        for k, v in data.iteritems():
            #print "    " * indent, k + ":",
            print "K:",k
            printKeyVals(v, indent + 1)
    else:
        print data

def compare(expected_data, data, indent=0):
    if isinstance(expected_data, list):
        for item in expected_data:
            compare(item, indent+1)
    elif isinstance(expected_data, dict):
        for k, v in expected_data.iteritems():
            print "K:",k
            compare(v, indent + 1)
    else:
        print expected_data

def testData(testname, method, url, jsonbody, expected):
  print "testname",testname
  print "method",method
  print "url",url
  print "jsonbody",jsonbody
  print "expected",expected
  print
  call = apiurl + '/' + username + url + apiToken

  request = require('request')
  if method == "GET":
    response = requests.get({url:call})
  elif method == "PUT":
    #response = requests.put(call, data=jsonbody)
    response = requests.put({url:call, body:jsonbody})
  elif method == "POST":
    #response = requests.post(call, data=jsonbody)
    response = requests.post({url:call, json:true, body:jsonbody})
  elif method == "DELETE":
    #response = requests.delete(call)
    response = requests.delete({url:call})
  elif method == "PATCH":
    #response = requests.patch(call, data=jsonbody)
    response = requests.patch({url:call, json:true, body:jsonbody})
    
  print "---call---"
  print call
  print "---jsonbody---"
  print jsonbody
  print "---status code---"
  print response.status_code
  print "---headers---"
  print response.headers
  print "---expected---"
  print expected
  print "---response---"
  print response.text
  print "---json---"
  try:
    print response.json()
  except ValueError:
    print "NO JSON BODY"
    pass
  print "\n\n\n"

  parsed_json = json.loads(response.text)
  parsed_expected = json.loads(expected)
  #test = printKeyVals(parsed_json)
  test = compare(parsed_expected,parsed_json)
  print "---test---"
  print test
  
  print "---pretty---"
  #print json.dumps(response.text, sort_keys=True, indent=4, separators=(',', ': '))
  #print jq(".").transform(response.text)
  #parsed_json = json.loads(response.text)
  #print parsed_json
  #for (i, item) in parsed_json:
  #    print i, item

  print "DONE PRINTKEYVALS"


