# server start
```
SERVER=/public/password.crack/crack/server
HASH=$SERVER/input.test

./initial $HASH
python scatter.py 2435 2 md5_pool $HASH.md5 &
python scatter.py 2254 2 bcr_pool $HASH.bcrypt &
python gather.py m $HASH.md5.cracked 5342 &
python gather.py b $HASH.bcrypt.cracked 4232 &
```
# server end
```
python arrange.py input.test input.test.md5.cracked input.test.bcrypt.cracked ans.test
```
# run a client
```
python client.py m $SERVER/md5_pool $HASH.md5.cracked
```
