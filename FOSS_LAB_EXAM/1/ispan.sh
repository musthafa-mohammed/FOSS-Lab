#!/bin/bash
t="$1"
c=0
arr=()
while [ "$t" -gt 0 ]
do
 e=$(($t%10))
 t=$(($t/10))
 arr["$c"]=$e
 c=$((c+1))
done
if [ "$c" -eq "$2" ];
then
t1=$2
flag=0
while [ "$t1" -gt 0 ]
do
 check=0
 for(( i=0; i<"$2"; i++))
 do
  if [ "$t1" == "${arr[$i]}" ];
  then
   check=1
  fi
 done
 if [ "$check" -eq 0 ];
 then
  flag=1
  break
 fi 
 t1=$((t1-1))
done
if [ "$flag" -eq 1 ];
then
 echo "npan"
else
 echo "pan"
fi
else
echo "npan"
fi
