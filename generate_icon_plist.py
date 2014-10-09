__author__ = 'chenliang'

import os

iconDir = "/Users/chenliang/git_projects/connect/asset/icons"

with open("/Users/chenliang/git_projects/connect/connect/Resources/icons/icons.plist", "w") as plist:
    plist.write('<plist version="1.0">')
    plist.write('<dict>')
    iconTypeList = os.listdir(iconDir)
    for iconType in iconTypeList:
        if ".DS_Store" == iconType:
            continue
        iconTypeDir = iconDir + "/" + iconType
        if os.path.isdir(iconTypeDir):
            filesInDirectory = os.listdir(iconTypeDir);
            fileCount = 0
            for file in filesInDirectory:
                if not file == ".DS_Store" :
                    fileCount += 1

            # fileCount = len(filesInDirectory)
            if fileCount <= 4:
                print iconType
                continue
            plist.write('<key>' + iconType + '</key>')
            plist.write('<string>' + str(fileCount) + '</string>')
    plist.write('</dict>')
    plist.write('</plist>')
