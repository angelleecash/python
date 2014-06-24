BEGIN{
	groupCount=0;
	taskCount=0;
	printf("\t");
	_ord_init();
	lastGroup = "";
	groupCount = 1;
}
function _ord_init(    low, high, i, t)
{
    low = sprintf("%c", 7) # BEL is ascii 7
    if (low == "\a") {    # regular ascii
        low = 0
        high = 127
    } else if (sprintf("%c", 128 + 7) == "\a") {
        # ascii, mark parity
        low = 128
        high = 255
    } else {        # ebcdic(!)
        low = 0
        high = 255
    }

    for (i = low; i <= high; i++) {
        t = sprintf("%c", i)
        _ord_[t] = i
    }
}
function ord(str,    c)
{
    # only first character is of interest
    c = substr(str, 1, 1)
    return _ord_[c]
}
{
	if(index(FILENAME, "students") != 0)
	{
		studentIdToName[$1] = $3;
		studentNameToId[$3] = $1;
		if(!xxx)
		{
			printf("\n");
			xxx=1;	
		}
	}
	else if(index(FILENAME, "task_knowledge") != 0)
	{
		tasks[taskCount] = $2;
		taskCount++;
		taskToKnowledge[$2] = $1;
		printf("%s\t", knowledgeIds[$1]);
	}
	else if(index(FILENAME, "knowledges") != 0)
	{
		knowledgeIds[$1] = $4;
	}
	else if(index(FILENAME, "groups") != 0)
	{
		if(lastGroup != $1)
		{
			lastGroup = $1;
			groupCount = 1;
		}
		printf("%s组 第%d组\n", $1, groupCount);
		groupCount ++;
		#printf("%c 组\n", ord("A") + FNR -1);
		for(i=2;i <= NF;i++)
		{
			studentName = $i;
			studentId = studentNameToId[studentName];
			printf("%s\t", studentName);
			for(j=0;j < taskCount;j++)
			{
				printf("%.2f%%\t", accuracy[studentId,tasks[j]]*100);
			}
			printf("\n");
		}
		printf("本组准确率\t");
		for(i=0;i<taskCount;i++)
		{
			groupSum = 0;
			for(j=2;j<=NF;j++)
			{
				studentId = studentNameToId[$j];
				groupSum += accuracy[studentId, tasks[i]];	
			}
			printf("%.2f%%\t", groupSum/NF*100);
		}
		printf("\n");
	}
	else if(index(FILENAME, "submission") != 0) 
	{
		submission[$3,$2] = $5
		accuracy[$3,$2] = $6/$7;
	}
	else
	{
		print "--------------------------------------UNKNOWN DATA -----> " FILENAME	
	}
}
END{
	printf("\n总的平均正确率\t");
		for(i=0;i<taskCount;i++)
		{
			groupSum = 0;
			studentCount=0;
			for(studentName in studentNameToId) 
			{
				studentCount ++;
				studentId = studentNameToId[studentName];
				groupSum += accuracy[studentId, tasks[i]];	

			}
			printf("%.2f%%\t", groupSum/studentCount*100);
		}
		printf("\n");

}


