mysql -uchenliang -pzxcvb -B --skip-column-names -e "use private_2;select subTasks from mission where id=5" | sed -e "s/\\\\n//g" > mission_data

python parse_json.py mission_data > task_knowledge

mysql -uchenliang -pzxcvb -B --skip-column-names -e "use private_2;select * from submission" > submission

mysql -uchenliang -pzxcvb -B --skip-column-names -e "use common;select * from knowledge" > knowledges 


mysql -uchenliang -pzxcvb -B --skip-column-names -e "use private_2;select * from student" > students

#groups ready

awk -F " " -f study_accuracy.awk knowledges  task_knowledge students submission groups > "准确率统计"

