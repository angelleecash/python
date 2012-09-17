# -*- coding: utf-8 -*-
#!/usr/bin/python
import xml.dom.minidom
import urllib

repositoryUrl = "https://dl-ssl.google.com/android/repository/repository-7.xml"

androidRepositoryBaseUrl = repositoryUrl[:repositoryUrl.rindex("/")+1]
print androidRepositoryBaseUrl
print "<html>"

def getElementText(element):
    texts = [];
    for node in element:
        if node.nodeType == node.TEXT_NODE:
            texts.append(node.data);
    return "\n".join(texts);

repositoryXmlStream = urllib.urlopen(repositoryUrl);
repositoryXml = repositoryXmlStream.read()
repositoryXml = repositoryXml.decode("utf8")

doc = xml.dom.minidom.parseString(repositoryXml)

sdkElements = doc.getElementsByTagName("sdk:platform");
for sdkElement in sdkElements:
    desc = sdkElement.getElementsByTagName("sdk:description")[0];
    print(getElementText(desc.childNodes))
    archives = sdkElement.getElementsByTagName("sdk:archives");
    for archive in archives:
        archiveUrl = archive.getElementsByTagName("sdk:url")[0];
        print(androidRepositoryBaseUrl + getElementText(archiveUrl.childNodes))

    print "\n"


print "</html>"

