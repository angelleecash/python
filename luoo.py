# __author__ = 'chenliang'
import urllib2

print """Content-Type: text/html\n"""
print "<html>"
print "<body>"


def parseLink(line):
    # l = '<a href="http://www.luoo.net/music/229" class="name" title="Leap Of Faith">vol.229 Leap Of Faith</a>'
    l = line


    hrefStart = l.index('"') + 1
    hrefEnd = l.index('"', hrefStart)

    href = l[hrefStart:hrefEnd]

    start = l.index(">") + 1
    end = l.index('<', start)

    title = l[start:end]

    return title, href

def comp(x, y):
    xLike = int(x[7])
    yLike = int(y[7])

    if xLike < yLike:
        return -1
    elif xLike > yLike:
        return 1
    else:
        return 0

categories = ["folk", "metal"]

for category in categories:
    guessPageCount = 20

    allItems = []
    print "<table border=\"1\">"

    # url = "http://www.luoo.net/music/folk"
    for page in range(1,20):
        url = "http://www.luoo.net/tag/" + category + "?p=" + str(page)
        response = urllib2.urlopen(url)
        html = response.read()
        htmlContent = str(html).split("\n")
        count = 0
        matched = False
        lineno = 1

        currentItem = []

        for line in htmlContent:
            count += 1
            line = line.lstrip()
            line = line.rstrip()

            if line == '<div class="meta rounded clearfix">':
                matched = True
                lineno = 1
                currentItem = []
            else:
                if line == '</div>':
                    if matched:
                        matched = False
                        # print currentItem
                        if len(currentItem) > 0:
                            allItems.append(currentItem)
                        currentItem = []
                else:
                    if matched :
                        # print lineno, ":", line
                        lineno += 1
                        currentItem.append(line)




    if len(allItems) <= 0:
        continue

    # print "---->", category

    # allItems.sort(cmp=lambda x,y : cmp(x[7], y[7]))
    allItems.sort(cmp=comp, reverse=True)

    print "<tr>"
    for i in range(0, min(len(allItems), 10)):
        link = allItems[i][0]
        like = allItems[i][7]
        title, href = parseLink(link)
        print "<td><a href=\""+ href+ "\">"+ title + "</a></td>"
    print "</tr>"

    print "</table>"
        # print title, "(", str(like) ,")" #, "-->",href
    # for item in allItems:
    #     link = item[0]
    #     like = item[7]
    #
    #     title, href = parseLink(link)
    #     print title, "(", str(like) ,")" #, "-->",href

    # print "\n\n\n"




print "</body>"
print "</html>"




