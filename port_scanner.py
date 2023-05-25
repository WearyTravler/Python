import sys
import socket
from datetime import datetime

##############
# port scanner
##############

common_port = dict()
result_names = dict()
responses_to_ignore = [111,10035]
ports_to_ignore = [1]

def setup_common_ports():
    common_port[80] = "HTTP"
    common_port[22] = "SSH"
    common_port[135] ="Remote procedure call"
    common_port[137] ="NetBIOS name service"    
    common_port[443] = "HTTPS"
    common_port[3389] = "Remote Desktop Protocol"
    common_port[21] = "ftp"
    common_port[20] = common_port[21]
    common_port[23] = "TELNET OH NO!!"
    common_port[139] = "SMB"
    common_port[53] = "DNS"
    common_port[853] = "SECDNS"
    common_port[445] = "HTTPS"
    common_port[902] = "vmware"
    common_port[912] = "Apex instant messaging"
    return

def setup_result_names():
    result_names[0] = "Success (OK)"
    result_names[111] = "ECONNREFUSED Connection refused"
    result_names[10061] = "WSAECONNREFUSED Connection refused"
    result_names[10013] = "WSAACCES Permission denied"
    result_names[10035] = "WSAEWOULDBLOCK Resource temporarily unavailable"
    return

def port_scanner(target,timeout):

    # ask the user what ports to scan ...
    # all, or only common ports

    choice = input("1 for all ports, 2 for common ports >")
    choice = int(choice)

    if choice == 1:
        # they want all - ask to what range
        upper = input("Scan to what max port? >")
        upper = int(upper)
        ports_to_scan = list(range(1,upper+1))
    else:
        ports_to_scan = common_port.keys()

    try:
        for port in ports_to_scan:
            # print("debug - scanning port",port)

            # set up our port socket

            s = socket.socket(socket.AF_INET,
                              socket.SOCK_STREAM)

            socket.setdefaulttimeout(timeout)
            tp = (target,port)

            # try to connect

            result = s.connect_ex(tp)

            # s.connect returns 0 if success,
            # or non-zero failure code

            # if we're not supposed to ignore this
            # one, print the information out

            if not result in responses_to_ignore  \
                   and not port in ports_to_ignore:

                name = common_port.get(port,"???")
                response = result_names.get(result,"??")
                print(port,name,result,response)

            s.close()
        #end for
            
    except KeyboardInterrupt:
            print("\n Ctrl-C -- Exiting Program !!!!")
            return

    except socket.gaierror:
            print("\n Could not get address")
            return
    return
    
def main():
    setup_common_ports()
    setup_result_names()
    print("Reminder - your own address is 127.0.0.1")
    server = input("Scan which server?  >")
    port_scanner(server,0.1)

if __name__ == "__main__":
    main()
