#!/bin/bash
#
testfile=passly_test_data.txt
OIFS="$IFS"
if [[ -f "$testfile" ]]
then
  #while IFS="," read -r message curltype curlurl curldata response
  while read -r line
  do
    echo "    line: $line"
    echo "---------------"
    IFS="," read -r message curltype curlurl curldata response <<< "$line"
    echo " message: $message"
    echo "curltype: $curltype"
    echo " curlurl: $curlurl"
    echo "curldata: $curldata"
    echo "response: $response"
  done < "$testfile"
else
    echo "Missing test file $testfile"
fi
IFS="$OIFS"
