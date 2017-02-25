#IMPORT THINGS THAT SHOULD BE IMPORTED
import commands
import sys
import pycurl
import json

#TAKE ARG AS IP TO PING
ip = str(sys.argv[1])
#DEFINE SLACK URL
slackurl = 'https://hooks.slack.com/services/YOUR/URL/GOESHERE'
#DEFINE CURL OBJECT
c = pycurl.Curl()
c.setopt(c.URL, slackurl)
c.setopt(c.HTTPHEADER, [
                        'Content-Type: application/json'
                ])
c.setopt(pycurl.POST, 1)
#INIT LOOP VAR
loop=0

#DEFINE FUNCTION TO SCRAPE OUTPUT, RETURNS STRING VALUE OF TTL and RTT
def formatRTT(p):
        d = p[1].strip("PING "+ip+" 56(84) bytes of data.")
        d = d.strip('\n')
        d = d.split('\n')
        if d[1] == '1 packets transmitted, 0 received, 100% packet loss, time 0ms':
                return 'FAIL','FAIL'

        d = d[0]
        d = d.split('icmp_seq=1 ')
        d = d[1]
        d = d.strip('ttl= ')
        d = d.split(' ')
        ttl = d[0]
        rtt = d[1].strip('time=')
        return ttl, rtt

#ALERT LOOP
while loop < 10:
        #SEND DEFINED PING COMMAND, COLLECT OUTPUT
        cmd = commands.getstatusoutput('ping '+ip+' -c 1 -W 4')
        #FORMAT OUTPUT
        ttl,rtt = formatRTT(cmd)
        #CHECK FOR TIMEOUT
        if rtt == 'FAIL':
        #IF DEAD, FORMAT ALERT TO SEND
                emoji=':trumpno:'
                data =  json.dumps({"username": ip+":", "icon_emoji": emoji,"text": ip+" IS FUCKING DOWN, SHIT!FUCK!"})
        else:
        #IF RESPONDING, KILL ROUTINE
                break
        c.setopt(c.POSTFIELDS, data)
        #SEND FAILURE TO SLACK
        c.perform()
        #INC LOOP COUNTER
        loop+=1
