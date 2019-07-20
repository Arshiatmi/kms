import requests
import socket
import os

class IG:
    address = ""
    def __init__(self):
        self.address = "google.com"

    def a_records(self):
        return requests.get("https://api.hackertarget.com/hostsearch/?q=" + self.address).text

    def as_lookup(self):
        return requests.get("https://api.hackertarget.com/aslookup/?q=" + self.address).text

    def dns_lookup(self):
        return requests.get("https://api.hackertarget.com/dnslookup/?q=" + self.address).text

    def find_dns_servers(self):
        return requests.get("https://api.hackertarget.com/findshareddns/?q=" + self.address).text

    def http_headers(self):
        return requests.get("https://api.hackertarget.com/httpheaders/?q=" + self.address).text

    def ip_location(self):
        return requests.get("https://api.hackertarget.com/geoip/?q=" + self.address).text

    def page_links(self):
        return requests.get("https://api.hackertarget.com/pagelinks/?q=" + self.address).text

    def ping(self):
        return os.popen("ping -c 1" + self.address).read()

    def reverse_ip_lookup(self):
        return requests.get("https://api.hackertarget.com/reverseiplookup/?q=" + self.address).text

    def revere_dns(self):
        return requests.get("https://api.hackertarget.com/reversedns/?q=" + self.address).text

    def subnet_calc(self):
        return requests.get("https://api.hackertarget.com/subnetcalc/?q=" + self.address).text

    def tcp_port_scan(self):
        return requests.get("https://api.hackertarget.com/nmap/?q=" + self.address).text

    def traceroute(self):
        return requests.get("https://api.hackertarget.com/mtr/?q=" + self.address).text

    def whois(self):
        return requests.get("https://api.hackertarget.com/whois/?q=" + self.address).text

    def zone_transfer(self):
        return requests.get("https://api.hackertarget.com/zonetransfer/?q=" + self.address).text

    def get_ip(self):
        return socket.gethostbyname(self.address)
