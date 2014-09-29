__author__ = 'chenliang'

import os

for root, dirs, files in os.walk("/Users/chenliang/git_projects/connect/connect/Resources/icons"):
    for name in dirs:
        # os.rmdir()
        k = os.path.join(root, name)
        count = len(os.listdir(os.path.join(root, name)))
        if count <= 0:
            os.rmdir(k)
