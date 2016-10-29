```
HASH=input.test
./initial $HASH
python scatter.py 2435 2 md5_pool &
python scatter.py 2254 2 bcr_pool &
python gather.py m $HASH.md5.cracked 5342 &
python gather.py b $HASH.md5.cracked 4232 &
```

```
python arrange.py input.test input.test.md5.cracked input.test.bcrypt.cracked ans.test
```
```
python client.py m md5_pool $HASH.md5.cracked
```


```
python f3.py m input.test.md5 1:3 ../dict 1:3 input.test.md5.cracked
curl "127.0.0.1:8000?this.pot:0:10"
```

```
rm "pool/t*" "pool/l*" "pool/p*" "pool/c*" "pool/b*"
touch pool/t:1:0:100
touch pool/t:2:100:200
touch pool/t:3:200:300
touch pool/t:4:300:400
python f1.py 8000 2 &
curl "127.0.0.1:8000/?query"
ls pool
curl "127.0.0.1:8000/?c:1:0:100"
ls pool
```
