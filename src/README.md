./f0 input.test
python f3.py m input.test.md5 1:3 ../dict 1:3 input.test.md5.cracked
python f4.py m input.test.md5.cracked 8000
curl "127.0.0.1:8000?this.pot:0:10"
python f3.py m input.test.md5 1:3 ../dict 1:3 input.test.md5.cracked
python f5.py input.test input.test.md5.cracked input.test.bcrypt.cracked ans.test
