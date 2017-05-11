#!/bin/sh
if [ "$1" -eq 2 ];
then
 echo "prime"
else
 h=$(($1/2))
 d=2
 flag=0
 while [ "$d" -lt "$h" ]
 do
  m=$(($1%$d))
  if [ "$m" -eq 0 ];
  then
   flag=1
  fi
  d=$(($d+1))
 done
 if [ "$flag" -eq 1 ];
 then
  echo "nprime"
 else
  echo "prime"
 fi
fi
