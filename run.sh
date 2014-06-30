#error_stats.sh  run.sh  study_accuracy.sh  study_time.sh  unsolved.sh
sh prepare_data.sh $1
sh error_stats.sh
sh study_accuracy.sh
sh study_time.sh
sh unsolved.sh
java -cp JavaExcel/libs/poi-3.10-FINAL-20140208.jar:JavaExcel/build/libs/JavaExcel.jar Main

mysql -uchenliang -pzxcvb -B --skip-column-names -e "use private_2;select startTime from mission where id=$1" | sed -e "s/\\\\n//g" > mission_date
awk '{print $0/1000}' mission_date | xargs -I {} date "+%Y-%m-%d" -d @{} | xargs -I {} mv workbook.xls {}-统计.xls
