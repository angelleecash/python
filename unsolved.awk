BEGIN{
	groupCount=0;
	taskCount=0;
	printf("\t");
	_ord_init();
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
		printf("%c 组\n", ord("A") + FNR -1);
		for(i=1;i <= NF;i++)
		{
			studentName = $i;
			studentId = studentNameToId[studentName];
			printf("%s\t", studentName);
			for(j=0;j < taskCount;j++)
			{
				assignmentId = taskToAssignment[tasks[j]];
				questionCount = assignmentCount[assignmentId];
				for(k=1;k<=questionCount;k++)
				{
					questionId = assignmentIds[assignmentId, k];
					qa = answer[studentId, questionId];
					if(qa==-1)
					{
						printf("%d,", k);
					}
				}
				printf("\t");
			}
			printf("\n");
		}
		groupCount ++;	
		printf("\n");
	}
	else if(index(FILENAME, "submission_review") != 0) 
	{
		answer[$1, $2] = $3;
	}
	else if(index(FILENAME, "submission") != 0) 
	{
		submission[$3,$2] = $5
	}
	else if(index(FILENAME, "study_tasks") != 0) 
	{
		taskToAssignment[$1] = $2;
	}
	else if(index(FILENAME, "assignmentsToQuestionIds") != 0) 
	{
		assignmentCount[$1] = NF-1
		for(i=2; i <= NF;i++)
		{
			assignmentIds[$1,i-1] = $i;
		}
	}
	else
	{
		print "--------------------------------------UNKNOWN DATA -----> " FILENAME	
	}
}
END{
}


