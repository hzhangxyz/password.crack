# script
```
kill %1 %2 %3 %4;git checkout -- ..;git clean -fdx ..;git pull
git commit -a -m update ; git push
export HASHCATFLAG="$HASHCATFLAG -d 1"
```
# environment
```
look up in `env.conf`
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
