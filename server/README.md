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
HASHCAT=/public/password.crack/hashcat/hashcat
```
# SERVERDIR start
```
./initial $HASH
python scatter.py $MD5SCATTER $LOCKEDNUM $MD5POOL $HASH.md5 &
python scatter.py $BCRSCATTER $LOCKEDNUM $BCRPOOL $HASH.bcrypt &
python gather.py m $HASH.md5.cracked $MD5GATHER &
python gather.py b $HASH.bcrypt.cracked $BCRGATHER &
```
# SERVERDIR end
```
python arrange.py $HASH $HASH.md5.cracked $HASH.bcrypt.cracked $ANSFILE
```
# run a client
```
python client.py m $SERVERDIR/md5_pool $HASH.md5.cracked $MD5SCATTER $MD5GATHER $PASSWDSERVER $HASHCAT
```
