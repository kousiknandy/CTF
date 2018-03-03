#!/bin/bash

URL=$1
COOKIEFILE=`mktemp`
curl -# -D $COOKIEFILE $URL -o /dev/null
txt=`cat $COOKIEFILE | grep -oE "[A-Za-z0-9]*_[0-9]*.[0-9]*" | cut -f1 -d_ | rot13`
cookie=`cat $COOKIEFILE | grep -oE "session=[A-Za-z0-9]*_[0-9]*.[0-9]*"`
curl -d "captchatext=$txt" -b $cookie $URL
rm $COOKIEFILE
