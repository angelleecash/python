__author__ = 'chenliang'

import urllib2

import os
import cgi
import os.path
import time
import re
import Queue
import threading

outputDir = "/Users/chenliang/git_projects/connect/connect/Resources/icons/"
downloadUrlPattern = re.compile(
    'class="downloadlink" href="([^"]*)" data-format="png"  data-icon-id="[^"]*" data-size="128"')
downloadUrlPrefix = "https://www.iconfinder.com"

def download_icon_type(queue, type):
    icon_page_url = "https://www.iconfinder.com/iconsets/" + type
    try:
        icon_page = urllib2.urlopen(icon_page_url)
        icon_page_content = str(icon_page.read())
        all_download_urls = downloadUrlPattern.findall(icon_page_content)

        icon_output_dir = outputDir + icon + "/"

        if not os.path.exists(icon_output_dir):
            os.mkdir(icon_output_dir)

        count = 0
        for download_url in all_download_urls:
            icon_content = urllib2.urlopen(downloadUrlPrefix + download_url).read()
            icon_file = open(icon_output_dir + str(count) + ".png", "w")
            icon_file.write(icon_content)
            icon_file.flush()
            count += 1
    except Exception as e:
        print e.message, e.args
        print type, icon_page_url
    finally:
        queue.put("")


url = "https://www.iconfinder.com/free_icons"
response = urllib2.urlopen(url)
html = response.read()
htmlContent = str(html)

iconTypes = set();
p = re.compile('<a href="/iconsets/([^"]*)">')
results = p.findall(htmlContent)
for r in results:
    iconTypes.add(r)

queue = Queue.Queue()
for i in range(64):
    queue.put("")

def do_download(queue, type):
    t = threading.Thread(target=download_icon_type, args = (queue,type))
    t.daemon = True
    t.start()
totalCount = len(iconTypes)
while len(iconTypes) > 0:
    queue.get()
    icon = iconTypes.pop()
    download_icon_type(queue, icon)
    print "progress", len(iconTypes), "/", totalCount, "{:.2f}".format(len(iconTypes)*1.0/totalCount)









