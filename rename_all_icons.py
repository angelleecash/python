__author__ = 'chenliang'

import os

dirRoot = "/Users/chenliang/tmp/backup"
for root, dirs, files in os.walk(dirRoot):
    for dir in dirs:
        print "-------------------------------->", dir
        parentDir = os.path.join(root, dir);
        for file in os.listdir(parentDir):
            # print file, "----------->", "{}-{}".format(dir, file)

            os.rename(os.path.join(parentDir, file) , os.path.join(parentDir, "{}-{}".format(dir, file)))

    # for name in dirs:
    #
    #     k = os.path.join(root, name)
    #     count = len(os.listdir(os.path.join(root, name)))
    #     if count <= 0:
    #         os.rmdir(k)
