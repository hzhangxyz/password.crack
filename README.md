# tools
- `start.sh`    : start server
- `end.sh`      : end server
- `resume.sh`   : resume server
- `starter.py`  : auto run client
- `killer.py`   : monitor and kill when dangera, with a file in argv, it only output pdu
- `alert.sh`    : killall hashcat and stop to generate new client
- `env.conf     : useful environment
- `recovery.py` : recovery ans not reported
- `toolkit.py`  : tool to manager dicts
- `copier.py`   : copy dicts

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
- hashcat          => ask

# About dictionary
- Download as many dictionary as possible
- Find some partterns represent password well
- Seperate them and combine into proper size
- Bayesian...
- Maintain manually
