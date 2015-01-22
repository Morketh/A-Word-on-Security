#Firewall rules to prevent SynFlood
The raw table handles untracked connections, the "CT" stands for conntrack and the --notrack options excludes them from tracking.
Second rule matches the SYN packets (UNTRACKED as per previous rule) and ACK packets (INVALID as per „nf_conntrack_tcp_loose=0“) and forwards them to the SYNPROXY target, which then verifies the syncookies (parallel, which wasn't possible previously) and establishes the full TCP connections. And finally we add a rule that drops every packet that the previous rule didn't catch, read bad packets/DDoS.
Your server should be able to handle multiple millions of packets per second, as long as your NIC doesn't crumble and your ISP doesn't nullroute your IP. 

```bash
iptables -t raw -I PREROUTING -p tcp -m tcp --syn -j CT --notrack
iptables -I INPUT -p tcp -m tcp -m state --state INVALID,UNTRACKED -j SYNPROXY --sack-perm --timestamp --wscale 7 --mss 1460
iptables -A INPUT -m state --state INVALID -j DROP
```
A DOS attack is primarily a half open connection a DDOS attack is also a half open connection from SEVERAL hosts at once in 3 simple firewall rules you can clean out INVALID (half open) connections and close them about as fast they can be opened by remote hosts.