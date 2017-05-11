#!/bin/bash
echo "Please enter the number of digits"
read n
echo "----------------------------------------------------------------------------------------------------------"
echo "calculating....."
m=$((10**n))
pmax=0
for(( i=10; i<"$m"; i++))
do
 r1=$(./isprime.sh $i)
 r2=$(./ispan.sh $i $n)
 if [ "$r1" == "prime" ] && [ "$r2" == "pan" ];
 then
  echo $i
  if [ "$i" -gt "$pmax" ];
  then
   pmax=$i
  fi
 fi
done
if [ "$pmax" -eq 0 ];
then
 echo "No prime pan digit in given limit"
else
 echo "The greatest prime pan digit in given limit is $pmax"
fi
