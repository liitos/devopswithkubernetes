#!/bin/ash
wikioftheday="Read_"$(curl -Ls -o /dev/null -w "%{url_effective}" https://en.wikipedia.org/wiki/Special:Random)""
curl -X POST -F "todotext="$wikioftheday"" http://projekti-be-svc/todos 2>/dev/null
echo $wikioftheday
