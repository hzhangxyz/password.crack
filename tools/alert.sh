kill -2 `ps aux | grep starter.py | grep -v grep | awk '{printf $2}'` &
kill -2 `ps aux | grep starter.py | grep -v grep | awk '{printf $2}'` &
ssh node1 killall -9 hashcat &
ssh node2 killall -9 hashcat &
ssh node3 killall -9 hashcat &
ssh node4 killall -9 hashcat &
