# tools
- `start.sh`  : start server
- `end.sh`    : end server
- `resume.sh` : resume server
- `auto.py`   : auto run client (WITH param)
- `mon.py`    : monitor and kill when dangera, with a file in argv, it only output pdu (WITH param)
- `alert.sh`  : killall hashcat and stop to generate new client
- `env.conf`  : useful environment (WITH param, NEED source)
- `recov.py`  : recovery ans not reported

# run a client(need a while)
`runs/starter.py`
`run_hashcat("node2","1,2,3","m")`
`kill_hashcat("node2",4)`

# dictionary format
`status:order:start:end`
- t:to crack
- l:lock to change
- p:crack pending
- c:completed
- b:crack break
in dicts , f is some tools

# ATTENSION
- key length <= 35 => just attension
- Param and Source => env.conf killer.py starter.py
- Dicts            => think and find, and f.py
- program stable   => try except and test
