# in tools
- `start.sh`  : start server
- `end.sh`    : end server
- `resume.sh` : resume server
- `auto.py`   : auto run client (WITH param)
- `mon.py`    : monitor and kill when dangera, with a file in argv, it only output pdu (WITH param)
- `alert.sh`  : killall hashcat and stop to generate new client
- `env.conf`  : useful environment (WITH param, NEED source)
- `recov.py`  : recovery ans not reported

# run a client(need a while)
`tools/auto.py`
`run_hashcat("node2","1,2,3","m")`

# dictionary format
`status:order:start:end`
- t:to crack
- l:lock to change
- p:crack pending
- c:completed
- b:crack break

# ATTENSION
- key length <= 35 => just attension
- Param and Source => power and source
- Dicts            => think and find

# TODO
BROKEN RECOVERY
