# ENV
```
SERVERDIR=/public/password.crack/crack/SERVERDIR
HASH=$SERVERDIR/input.test
MD5POOL=$SERVERDIR/md5_pool
BCRPOOL=$SERVERDIR/bcr_pool
MD5SCATTER=2222
MD5GATHER=2223
BCRSCATTER=2224
BCRGATHER=2225
LOCKEDNUM=2
ANSFILE=$SERVERDIR/output
PASSWDSERVER=node1
HASHCATADDR=/public/password.crack/hashcat/hashcat
HASHCATFLAG="--attack-mode 0 --workload-profile 4 --gpu-temp-disable"
```
# SERVERDIR start
```
./initial $HASH
python scatter.py m $HASH.md5 &
python scatter.py b $HASH.bcrypt &
python gather.py m $HASH.md5.cracked &
python gather.py b $HASH.bcrypt.cracked &
```
# SERVERDIR end
```
python arrange.py $HASH $HASH.md5.cracked $HASH.bcrypt.cracked $ANSFILE
```
# run a client
```
python client.py m $HASH.md5.cracked
```
