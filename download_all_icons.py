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
    'class="downloadlink" href="([^"]*)" data-format="png" data-icon-id="[^"]*" data-size="128"')
downloadUrlPrefix = "https://www.iconfinder.com"

timeOut = 1000000


def remove_empty_directory(path):
    if os.path.exists(path) and os.path.isdir(path):
        if len(os.listdir(path)) <= 0:
            os.rmdir(path)

def download(url, failCount=3):
    count = 0
    while(count < failCount):
        try:
            time.sleep(5)
            response = urllib2.urlopen(url, timeout=timeOut)
            content = response.read()
            return True, content
        except Exception as e:
            count += 1
            print url, e
    return False, ""

def download_icon_type(queue, type):
    icon_page_url = "https://www.iconfinder.com/iconsets/" + type
    icon_output_dir = outputDir + icon + "/"

    ok, icon_page_content = download(icon_page_url)

    if not ok:
        remove_empty_directory(icon_output_dir)
        print "-------------------->", icon_page_url
        queue.put("")
        return

    all_download_urls = downloadUrlPattern.findall(str(icon_page_content))
    if not os.path.exists(icon_output_dir):
        os.mkdir(icon_output_dir)

    count = 0
    failed_urls = set()
    for download_url in all_download_urls:
        ok, icon_content = download(downloadUrlPrefix + download_url, failCount=10000)
        if not ok:
            print "fail to download ", download_url, "for type ", type
            failed_urls.add(download_url)
            continue

        icon_file_path = icon_output_dir + str(count) + ".png"
        icon_file = open(icon_file_path, "w")
        icon_file.write(icon_content)
        icon_file.flush()
        count += 1
    if count >= len(all_download_urls):
        print type, "OK"
    else :
        print type, "INCOMPLETE"
        for failed_url in failed_urls:
            print "MISSING", failed_url
    remove_empty_directory(icon_output_dir)
    queue.put("")

bufferPath = "/Users/chenliang/tmp/lhmswww"
if os.path.exists(bufferPath):
    bufferFile = open(bufferPath)
    htmlContent = bufferFile.read()
else:
    url = "https://www.iconfinder.com/free_icons"
    response = urllib2.urlopen(url, timeout=timeOut)
    html = response.read()
    htmlContent = str(html)
    open(bufferPath, "w").write(htmlContent)

iconTypes = set()
p = re.compile('<a href="/iconsets/([^"]*)">')
results = p.findall(htmlContent)
for r in results:
    iconTypes.add(r)

queue = Queue.Queue()
for i in range(1):
    queue.put("")


def do_download(queue, type):
    t = threading.Thread(target=download_icon_type, args=(queue, type))
    t.daemon = True
    t.start()

iconTypes = set()
# iconTypes.add("ilb")
# iconTypes.add("cat-power")

iconTypes.add("adobe-flat-icons")
iconTypes.add("christmas-special")
iconTypes.add("cat-force")
iconTypes.add("yama1-social-3")
iconTypes.add("simple-files")
iconTypes.add("creative-nerds-wooden-icons")
iconTypes.add("imoticons")
iconTypes.add("minimalist-social-media-icons-by-design-bolts")
iconTypes.add("buttonz")
iconTypes.add("dooffy_design_flags")
iconTypes.add("monster-icons")
iconTypes.add("chocolate_hearts")
iconTypes.add("flag_set")
iconTypes.add("hex-social-media")
iconTypes.add("circle-payment-methods-4")
iconTypes.add("social-set-2")
iconTypes.add("195-flat-flag-psd-icons")
iconTypes.add("hayal-social")
iconTypes.add("european-country-flags")

totalCount = len(iconTypes)
while len(iconTypes) > 0:
    queue.get()
    icon = iconTypes.pop()
    do_download(queue, icon)
    print "progress", len(iconTypes), "/", totalCount, "{:.2f}".format(len(iconTypes) * 1.0 / totalCount)
    # break