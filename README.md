# script
```
kill %1 %2 %3 %4;git checkout -- ..;git clean -fdx ..;git pull
git commit -a -m update ; git push
export HASHCATFLAG="$HASHCATFLAG -d 1"
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
export HASHCATADDR=/public/password.crack/zj-hashcat/hashcat
export HASHCATFLAG="--attack-mode 0 --workload-profile 4 --gpu-temp-disable --restore-disable"
```
# server start
```
./initial
./scatter.py m &
./scatter.py b &
./gather.py m &
./gather.py b &
```
# server end
```
./finish
```
# run a client(need a while)
```
./client.py m
./client.py b
```
# dictionary format
`status:order:start:end`
- t:to crack
- l:lock to change
- p:crack pending
- c:completed
- b:crack break
