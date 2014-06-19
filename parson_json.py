import sys
import json
# __author__ = 'chenliang'

file = open(sys.argv[1], 'r')

for line in file.readlines():
    decoded = json.loads(line)
    sequenceCount = len(decoded)
    for index in range(sequenceCount):
        # "taskIds":[183],"knowledgeId":50
        item = decoded[index];
        taskIds = item['taskIds'];
        assert len(taskIds) == 1
        # print "sequenceId=", item['sequenceId'], " knowledgeId=",item['knowledgeId'], " taskIds=", item['taskIds'], taskIds[0]
        print item['knowledgeId'], taskIds[0]
file.close()

# print sys.argv[1]



