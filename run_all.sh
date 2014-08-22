rm *.xls
#sh run.sh 16
#sh run.sh 17
#sh run.sh 18
#sh run.sh 19
#sh run.sh 20 
#sh run.sh 21 
#ssh run.sh 22 
#sh run.sh 24 
#sh run.sh 25 
#sh run.sh 26 
for mission in `seq 27 28`
do
    sh run.sh $mission
done
#echo "" | mutt -a "`ls *.xls`" -s "统计数据" -- huangxin@accurator.com.cn tuxiaolei@accurator.com.cn linxiao@accurator.com.cn zhuyanbin@accurator.com.cn chenliang@accurator.com.cn
