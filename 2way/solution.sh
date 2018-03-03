./gencert.sh client
for i in `seq 1 60` 
do 
     curl -k ${1} --cert client.crt --key client.key
     if [ $? -eq 35 ]
     then
           sleep 10
     else
           break
     fi
done
rm -f client.crt client.key
