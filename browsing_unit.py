# -*- coding: utf-8 -*-
#browsing and installation unit 



import webbrowser
import os
from logs.physical import log_action
import time


# Browsing section
def youtube():
    print("We are now starting to browse YouTube")
    os.system("firefox https://youtube.com/")
    log_action(action="browsing", process_name="youtube", process_type="online")
    



def osintframe():
    print("We are now starting to browse OSINT Framework")
    os.system("firefox https://osintframework.com/")
    log_action(action="browsing", process_name="osint frame", process_type="online")



def dnslookup():
    print("We are now starting to browse DNS Lookup")
    os.system("firefox https://www.nslookup.io/")
    log_action(action="browsing", process_name="DNS Lookup", process_type="online")



def waybackmachine():
    print("We are now starting to browse Wayback Machine")
    os.system("firefox http://web.archive.org/")
    log_action(action="browsing", process_name="Wayback machine", process_type="online")



def ip2location():
    print("We are now starting to browse IP2Location")
    os.system("firefox http://ip2location.com")
    log_action(action="browsing", process_name="IP2Location", process_type="online")



def rdpguard():
    print("We are now starting to browse RDPGuard")
    os.system("firefox https://rdpguard.com")
    log_action(action="browsing", process_name="RDP Guard", process_type="online")



def hackergpt():
    print("We are now starting to browse Hacker GPT")
    os.system("firefox https://chat.hackerai.co/")
    log_action(action="browsing", process_name="hacker Gpt", process_type="online")



def wiki():
    print("We are now starting to browse Wikipedia")
    os.system("firefox https://en.wikipedia.org")
    log_action(action="browsing", process_name="Wikipedia", process_type="online")
    
    

def panzer():
    print("We are now starting to browse PanzerRush Game")
    os.system("firefox https://www.panzerrush.com/?e=1")
    log_action(action="browsing", process_name="PanzerRush Game", process_type="online")



def bmi():
    print("We are now starting to browse Microsoft Bin")
    os.system("firefox messenger.microsoft.com/")
    log_action(action="browsing", process_name="Microsoft bin", process_type="online")



def updater():
    log_action("Updating system")
    print("Now! We will update")
    os.system("sudo apt update && sudo apt upgrade -y")
    os.system('clear')
    log_action(action="Updating system ", process_name="updater", process_type="online")
 
    
 
def python3_error():
    os.system('sudo apt install python3-venv')
    os.system('python3 -m venv path/to/venv')
    os.system('source path/to/venv/bin/activate')
    print("Now ready to use!")
    log_action(action="Error fix python", process_name="Python error fix", process_type="online")
    
    


# Install section
def virtualbox_install():
    os.system("sudo apt update")
    os.system("sudo apt install virtualbox -y")
    os.system("sudo apt install virtualbox-dkms")
    os.system("sudo apt full-upgrade -y")
    os.system("sudo apt install build-essential dkms linux-headers-$(uname -r)")
    print("We installed VirtualBox on your Linux system")
    print("We will reboot")
    time.sleep(3)
    os.system("sudo apt purge virtualbox -y && reboot")
    log_action(action="Installing", process_name="Virtualbox install", process_type="online")



def telegram_install():
    log_action(action="Installing", process_name="telegram install", process_type="online")
    print("You need to browse and download the file")
    print("We will start browsing the Telegram download website")
    os.system("firefox https://desktop.telegram.org/")



def spyder_install():
    log_action(action="Installing", process_name="Spyder install", process_type="online")
    print("Now! We will install Python Spyder")
    os.system("sudo apt install spyder")



def code_installer():
    log_action(action="Installing", process_name="Code-Oss install", process_type="online")
    print("Now! We will install Code-OS")
    os.system("sudo apt install code-os")



def rise_installer():
    log_action(action="Installing", process_name="Riseup install", process_type="online")
    print("Now! We will install Rise-UP VPN")
    os.system("sudo apt install rise-up")



def vlc_installer():
    log_action(action="Installing", process_name="vlc-bin install", process_type="online")
    print("Now! We will install VLC-bin")
    os.system("sudo apt install vlc-bin")
    
    
#Browsing Service 
#penetration search engine and other lis
def pentest_service():
    log_action(action="Pentration Web List", process_name="pentest service", process_type="printing")
    # List of services categorized by type
    services = [
        {
            "Category": "Search Engine",
            "Name": "Shodan",
            "URL": "https://www.shodan.io"
        },
        {
            "Category": "Search Engine",
            "Name": "Censys",
            "URL": "https://censys.com/"
        },
        {
            "Category": "Search Engine",
            "Name": "Onyphe",
            "URL": "https://www.onyphe.io/"
        },
        {
            "Category": "Search Engine",
            "Name": "Bin",
            "URL": "https://messenger.microsoft.com"
        },
        {
            "Category": "Search Engine",
            "Name": "ZoomEye",
            "URL": "https://www.zoomeye.hk/"
        },
        {
            "Category": "Search Engine",
            "Name": "Binary Edge",
            "URL": "https://www.binaryedge.io/"
        },
        {
            "Category": "Search Engine",
            "Name": "Wigle",
            "URL": "https://wigle.net/"
        },
        {
            "Category": "Search Engine",
            "Name": "BuiltWith",
            "URL": "https://builtwith.com/"
        },
        {
            "Category": "Search Engine",
            "Name": "Public WWW",
            "URL": "https://publicwww.com/"
        },
        {
            "Category": "Threat Intelligence",
            "Name": "Pulsedive",
            "URL": "https://pulsedive.com/"
        },
        {
            "Category": "Threat Intelligence",
            "Name": "Urlscan",
            "URL": "https://urlscan.io/"
        },
        {
            "Category": "Vulnerabilities",
            "Name": "Vulners",
            "URL": "https://vulners.com/"
        },
        {
            "Category": "Virus Scan",
            "Name": "VirusTotal",
            "URL": "https://www.virustotal.com"
        },
        {
            "Category": "Virus Scan",
            "Name": "Jotti's Virus Scan",
            "URL": "https://virusscan.jotti.org/it"
        },
        {
            "Category": "IP Lookup",
            "Name": "What is My IP",
            "URL": "https://whatismyip.com/"
        },
        {
            "Category": "IP Lookup",
            "Name": "What's Their IP",
            "URL": "https://whatstheirip.com/"
        },
        {
            "Category": "Breach Search Engines",
            "Name": "Intelligence X",
            "URL": "https://intelx.io"
        },
        {
            "Category": "Breach Search Engines",
            "Name": "Leakcheck",
            "URL": "https://leakcheck.io"
        },
        {
            "Category": "Breach Search Engines",
            "Name": "We Leak Info",
            "URL": "https://weleakinfo.to"
        },
        {
            "Category": "Breach Search Engines",
            "Name": "Leak Peek",
            "URL": "https://leakpeek.com"
        },
        {
            "Category": "Breach Search Engines",
            "Name": "Snusbase",
            "URL": "https://snusbase.com"
        },
        {
            "Category": "Breach Search Engines",
            "Name": "Leakedsource",
            "URL": "https://wikileaks.org"
        },
        {
            "Category": "Breach Search Engines",
            "Name": "GlobelLeaks",
            "URL": "https://globaleaks.org"
        },
        {
            "Category": "Breach Search Engines",
            "Name": "Firefox Monitor",
            "URL": "https://monitor.firefox.com"
        },
        {
            "Category": "Breach Search Engines",
            "Name": "Breach Alarm",
            "URL": "https://breachalarm.com"
        }
    ]
    
    
    
    print("\n")
    for service in services:
        print(f"{service['Category']:20} | {service['Name']:20} | {service['URL']}")
        

    def browse_service():
        print("\n")
        response = input("Emily:Do you want to browse? (yes/no): ").strip().lower()
        if response == "yes":
            log_action("User make browsing:", response)
            service_name = input("Emily:Type the website name: ").strip()
            for service in services:
                log_action("User make browsing:", service_name)
                if service['Name'].lower() == service_name.lower():
                    print(f"Opening {service['Name']} at {service['URL']}")
                    webbrowser.open(service['URL'])
                    return
            print("Emily:Sorry, the service you entered is not in the list.")
        else:
            print("Emily:Okay, have a nice day!")


    browse_service()
    