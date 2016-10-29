# server start
```
HASH=input.test
./initial $HASH
python scatter.py 2435 2 md5_pool &
python scatter.py 2254 2 bcr_pool &
python gather.py m $HASH.md5.cracked 5342 &
python gather.py b $HASH.md5.cracked 4232 &
```
# server end
```
python arrange.py input.test input.test.md5.cracked input.test.bcrypt.cracked ans.test
```
# run a client
```
python client.py m md5_pool $HASH.md5.cracked
curl "127.0.0.1:8000?this.pot:0:10"
curl "127.0.0.1:8000/?c:1:0:100"
```
