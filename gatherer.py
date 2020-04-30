#!/usr/bin/env python3
import requests
import socket


def top():
    print("IP/WEB Checker")


def menu():
    print("""
1) Whois Lookup             8) HTTP Header                  
2) DNS Lookup               9) Host Finder
3) GeoIP Lookup             10) IP-Locator   
4) Subnet Lookup            11) Find Shared DNS Servers 
5) Port Scanner             12) Get Robots.txt   
6) Page Links               13) Host DNS Finder
7) Zone Transfer            14) Exit                
          """)
    print()


def check():
    try:
        if 1 > 2:
            print("buffer")
        else:
            options()
    except socket.gaierror:
        check()
    except UnboundLocalError:
        check()
    except requests.exceptions.ConnectionError:
        exit()
    except IndexError:
        print('?')
        check()


def options():
    top()
    website = input('Website : ')
    menu()
    select = input('Option: ')

    if select == '1':
        whois = 'https://api.hackertarget.com/whois/?q=' + website
        info = requests.get(whois)
        print('')
        print(info.text)
        options()

    elif select == '2':
        dnslook = 'https://api.hackertarget.com/dnslookup/?q=' + website
        info = requests.get(dnslook)
        print('')
        print(info.text)
        options()

    elif select == '3':
        ipgeo = 'https://api.hackertarget.com/geoip/?q=' + website
        info = requests.get(ipgeo)
        print('')
        print(info.text)
        options()

    elif select == '4':
        subnet = 'http://api.hackertarget.com/subnetcalc/?q=' + website
        info = requests.get(subnet)
        print('')
        print(info.text)
        options()

    elif select == '5':
        port = 'https://api.hackertarget.com/nmap/?q=' + website
        info = requests.get(port)
        print('')
        print(info.text)
        options()

    elif select == '6':
        pagelink = 'https://api.hackertarget.com/pagelinks/?q=' + website
        info = requests.get(pagelink)
        print('')
        print(info.text)
        options()

    elif select == '7':
        zone = 'https://api.hackertarget.com/zonetransfer/?q=' + website
        info = requests.get(zone)
        print('')
        print(info.text)
        options()

    elif select == '8':
        header = "https://api.hackertarget.com/httpheaders/?q=" + website
        info = requests.get(header)
        print('')
        print(info.text)
        options()

    elif select == '9':
        host = "https://api.hackertarget.com/hostsearch/?q=" + website
        info = requests.get(host)
        print('')
        print(info.text)
        options()

    elif select == '10':
        website = socket.gethostbyname(website)
        iplt = 'https://ipinfo.io/' + website + '/json'
        info = requests.get(iplt)
        print('')
        print(info.text)
        options()

    elif select == '11':
        shared = 'https://api.hackertarget.com/findshareddns/?q=' + website
        info = requests.get(shared)
        print('')
        print(info.text)
        options()

    elif select == '12':
        robots = 'http://' + website + '/robots.txt'
        info = requests.get(robots)
        print('')
        print(info.text)
        options()

    elif select == '13':
        hostdns = 'https://api.hackertarget.com/mtr/?q=' + website
        info = requests.get(hostdns)
        print('')
        print(info.text)
        options()

    elif select == '14':
        exit()
    else:
        check()


check()
