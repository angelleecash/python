#!/usr/bin/python
# coding=utf-8
__author__ = 'chenliang'
import urllib2
import re

url = "http://www.luoo.net/music/"
response = urllib2.urlopen(url)
html = response.read()
htmlContent = str(html).split("\n")
matched = False

for line in htmlContent:
    line = line.lstrip()
    line = line.rstrip()

    if line == '<div class="pagenav-wrapper">':
        matched = True
    else:
        if (matched):
            # print line

            p = re.compile('<a href="([^"]*)" class="item">([^<]*)</a>')
            results = p.findall(line)

            # print len(results)
            break

print """Content-Type: text/html\n"""
print "<html>"
print "<body>"

print "<table>"

for result in results:
    print "<tr>"
    print "<td><a href=\""+ result[0] + "\">"+ result[1] + "</a></td>"
    print "</tr>"

print "</table>"

print "</body>"
print "</html>"




