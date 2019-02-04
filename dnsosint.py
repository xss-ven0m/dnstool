#Created by apt-get
#twitter @aptget11
#dns zone transfer tool

import os
import time
import socket

#Making sure that 'host' tool is installed, (DEBIAN ONLY)
os.system("apt-get install host")

hostname = socket.gethostname()

#clear terminal
os.system("clear")

print ("[*] Dnslookup Helper")

domain = raw_input("\n\n[*] Please enter domain name: ")

def dirb_scan():

    print ("\n[*] Would you like to scan for directories? Y/n\n" )

    while True:
        
        Dir_wordlist = raw_input("%s@dnsscan: "%(hostname))

        if Dir_wordlist in ("Y","y"):
            print ("\n\n[*] Starting dirb..")
            print ("\n\n[*] Please enter URL PATH of domain to scan. Ex. 'http://expamle.com/': ")
            dirscaninput = raw_input("\n%s@dnsscan: "%(hostname))
            dirbscanstart = ("dirb %s" % (dirscaninput)) 
            os.system(dirbscanstart)
            raw_input("\n\n[*] Press 'Enter' to continue..\n\n")
            break

        elif Dir_wordlist in ("N", "n"):
            print ("\n\r\n[*] Skipping dirscan...\n\n\n")
            time.sleep(1)
            break
        else:
            print ("\n[*] Please select an 'y' or 'n'..\n")
            
def common_record_scan():
    print ("\n[*] Performing common record scan:\n\n")

    #perform nameserver scan on host
    print ("[*] Nameserver scan: \n")
    nsscan = ("host -t ns %s"%(domain))
    os.system(nsscan)
    print ("\n")

    #perform mailsever scan on host
    print ("[*] Mailserver scan: \n")
    mxscan = ("host -t mx %s"%(domain))
    os.system(mxscan)
    print ("\n")

    #perform SOA scan on host
    print ("[*] SOA scan: \n")
    soascan = ("host -t soa %s"%(domain))
    os.system(soascan)
    print ("\n")

    #perform CNAME scan on host
    print ("[*] CNAME scan: \n")
    cnamescan = ("host -t cname %s"%(domain))
    os.system(cnamescan)
    print ("\n")   

    #perform TXT scan on host
    print ("[*] TXT scan: \n")
    txtscan = ("host -t cname %s"%(domain))
    os.system(txtscan)
    print ("\n")   

    zone_transfer = raw_input("Would you like to perform a Zone Transfer? Y/n: ")
    
    if zone_transfer in ("Y", "y"):
        Zone_Transfer()
    else:
        print ("\n\n[*] Quitting...")
        exit()

def Zone_Transfer():
    #user inputs the dns server
    dns = raw_input("\n[*] Please enter dns sever to attempt Zone Transfer: ")
    time.sleep(1)
    print ("\n[*] Attempting Zone Transfer..\n\n")
    query = ("host -l %s %s"% (domain, dns))
    os.system(query)

def main():
    
    dirb_scan()
    common_record_scan()

if __name__ == "__main__":
    main()

