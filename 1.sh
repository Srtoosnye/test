#!/bin/bash

i=0
sum=0
std=100
while [ "$i" -lt "$std" ]
do
    let "i+=1"
    let "sum+=i"
done
echo "$sum"
