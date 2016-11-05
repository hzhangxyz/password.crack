# in tools
`start.sh`  : start
`end.sh`    : end
`resume.sh` : resume
`auto.sh`   : auto run client (WITH param)
`mon.sh`    : monitor and kill when dangera (WITH param)
`alert.sh`  : killall hashcat and stop to generate new client
`env.conf`  : useful environment (WITH param, NEED source)

# run a client(need a while)
`cstart/arr.py`
`run_hashcat("node2","1,2,3","m")`

# dictionary format
`status:order:start:end`
- t:to crack
- l:lock to change
- p:crack pending
- c:completed
- b:crack break

# ATTENSION
key length <= 35
source env.conf !!!

# TODO?
CLIENT and DEVICE
    PAUSE KILL
DICT
BROKEN RECOVERY
POWER
