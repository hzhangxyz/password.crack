# script
```
kill %1 %2 %3 %4;git checkout -- ..;git clean -fdx ..;git pull
git commit -a -m update ; git push
```
# environment
```
export SERVERDIR=/public/password.crack/crack/server
export HASH=$SERVERDIR/input.test
export MD5POOL=$SERVERDIR/md5_pool
export BCRPOOL=$SERVERDIR/bcr_pool
export MD5SCATTER=2222
export MD5GATHER=2223
export BCRSCATTER=2224
export BCRGATHER=2225
export LOCKEDNUM=2
export ANSFILE=$SERVERDIR/ans.test
export PASSWDSERVER=node2
export HASHCATADDR=/public/password.crack/hashcat/hashcat
export HASHCATFLAG="--attack-mode 0 --workload-profile 4 --gpu-temp-disable"
```
# server start
```
./initial $HASH
python scatter.py m &
python scatter.py b &
python gather.py m &
python gather.py b &
```
# server end
```
python arrange.py $HASH $HASH.md5.cracked $HASH.bcr.cracked $ANSFILE
```
# run a client(need a while)
```
python client.py m
python client.py b
```
# dictionary format
`status:order:start:end`
- t:to crack
- l:lock to change
- p:crack pending
- c:completed
- b:crack break