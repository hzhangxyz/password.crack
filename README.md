字典策略

- 吉利的数字（日期20-40）【FPGA】(88888888)
- 简单的字母
- 常见单词（原文，首字母大写，全大写）（包括人名）
- 6位数字【FPGA】
- 字母/单词/数字组合（下划线，减号，混合，@ _  - ()）
- 字符变易
- 字典！！

TIPS

- 先随机若干穷举
- 先MD5

solution :

database(!)  :
{
    hashes   : [hashes...],
    dicts    : ["filename1","filename2",...],
    status   : ["Running","Pending","Scanned","Break"],
    pointer  : 最近的一个非Scanned status
    cracked  : [...]
}

server   :

F0 : initial hashes(split md5 and bcrypt) and mongodb from commitee
F1 : read new filename and add it into mongodb
F2 : accept request from hashcat and give hashes slice of hashes and dicts filename number
F3 : move hashes cracked into another list
F4 : after request, output the format required
