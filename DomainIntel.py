import socket
import requests
import whois
import ssl
import subprocess
import tldextract
from OpenSSL import crypto
import dns.resolver

def get_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return None

def get_dns_records(domain):
    records = {}
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['8.8.8.8', '8.8.4.4']  # Set Google's public DNS servers as fallback
    for qtype in ['A', 'AAAA', 'MX', 'NS', 'SOA', 'TXT']:
        try:
            answers = resolver.resolve(domain, qtype, raise_on_no_answer=False)
            records[qtype] = [answer.to_text() for answer in answers]
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.Timeout, dns.exception.DNSException):
            records[qtype] = []
    return records

def get_server_details(ip):
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        return response.json()
    except requests.RequestException as e:
        return str(e)

def get_whois_info(domain):
    try:
        return whois.whois(domain)
    except Exception as e:
        return str(e)

def ssl_certificate_details(domain):
    try:
        cert = ssl.get_server_certificate((domain, 443))
        x509 = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
        return {
            'Issuer': x509.get_issuer().get_components(),
            'Subject': x509.get_subject().get_components(),
            'Serial Number': x509.get_serial_number(),
            'Version': x509.get_version(),
            'Not Before': x509.get_notBefore(),
            'Not After': x509.get_notAfter()
        }
    except Exception as e:
        return str(e)

def server_information(domain):
    try:
        cmd = f"curl -sI {domain}"
        return subprocess.check_output(cmd, shell=True, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        return str(e)

def subdomain_enumeration(domain):
    try:
        subdomains = []
        ext = tldextract.extract(domain)
        base_domain = f"{ext.domain}.{ext.suffix}"
        url = f"https://crt.sh/?q=%25.{base_domain}&output=json"
        response = requests.get(url)
        data = response.json()
        for entry in data:
            subdomains.append(entry['name_value'].strip())
        return subdomains
    except Exception as e:
        return str(e)

def port_scanning(ip):
    try:
        cmd = f"nmap -F {ip}"
        return subprocess.check_output(cmd, shell=True, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        return f"Port Scanning failed: {str(e)}"

def free_email_lookup(domain):
    free_email_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    return domain in free_email_domains

def mac_address_lookup(mac_address):
    return mac_address

def main():
    domain = input("Enter domain: ")

    print(f"\nBasic Information for Domain: {domain}\n")

    ip = get_ip(domain)
    if ip:
        print(f"IP Address: {ip}")

        print("\nDNS Records:")
        dns_records = get_dns_records(domain)
        if isinstance(dns_records, dict):
            for record_type, records in dns_records.items():
                print(f"{record_type}:")
                for record in records:
                    print(f"  {record}")
        else:
            print(dns_records)

        print("\nServer Details:")
        server_details = get_server_details(ip)
        for key, value in server_details.items():
            print(f"{key}: {value}")

        print("\nWHOIS Information:")
        whois_info = get_whois_info(domain)
        print(whois_info)

        print("\nSSL Certificate Details:")
        ssl_details = ssl_certificate_details(domain)
        if isinstance(ssl_details, dict):
            for key, value in ssl_details.items():
                print(f"{key}: {value}")
        else:
            print(ssl_details)

        print("\nServer Information:")
        server_info = server_information(domain)
        print(server_info)

        print("\nSubdomain Enumeration:")
        subdomains = subdomain_enumeration(domain)
        if isinstance(subdomains, list):
            for subdomain in subdomains:
                print(subdomain)
        else:
            print(subdomains)

        print("\nPort Scanning:")
        port_scan = port_scanning(ip)
        print(port_scan)

        email_domain = domain.split('@')[-1]
        print("\nFree Email Lookup:")
        is_free_email = free_email_lookup(email_domain)
        print(f"Free Email Domain: {is_free_email}")

        mac_address = "00:14:22:01:23:45"  # Predefined MAC address for testing
        mac_address = mac_address_lookup(mac_address)
        print(f"\nMAC Address Lookup:")
        print(f"MAC Address: {mac_address}")

    else:
        print("Invalid domain or unable to resolve IP")

if __name__ == "__main__":
    main()
