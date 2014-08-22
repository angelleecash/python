__author__ = 'chenliang'

import os
import fnmatch


def ls(dir):
    for path, dirlist, filelist in os.walk(dir):
        for file in filelist:
            print file


def find(dir, pattern):
    for path, dirlist, filelist in os.walk(dir):
        for file in fnmatch.filter(filelist, pattern):
            print file

# ls("/Users/chenliang/tmp")
find("/Users/chenliang/tmp", "p*.txt")