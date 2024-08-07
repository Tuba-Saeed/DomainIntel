# DomainIntel

DomainIntel is a tool for gathering various types of information about domains. 



  
  # Features
  **IP Address Lookup:**    
  Retrieve the IP address associated with a domain.   
  **DNS Records:**   
  Fetch DNS records (A, AAAA, MX, NS, SOA, TXT) for a domain.   
  **Server Details:**     
  Obtain server information using IP-based lookups.   
  **WHOIS Information:**    
  Gather WHOIS data for domain registration details.    
  **SSL Certificate Details:**   
  Extract SSL certificate information for a domain.    
  **Server Information:**   
  Get server response headers.   
  **Port Scanning:**  
  Perform a quick port scan to identify open ports.    
  **Traceroute:**   
  Perform a traceroute to map the path packets take to the domain.   
  **Free Email Lookup:**   
  Check if a domain in is associated with free email services.   
**Subdomain Enumeration:**   
Identify subdomains associated with a domain.   
  **MAC Address Lookup:**   
  Example placeholder for MAC address lookup.   
 ## Adding Path
Check your shell and with command 
```bash
echo $0

```
Edit .bashrc or zshrc 


```bash
nano ~/.bashrc

```

```bash
nano ~/.zshrc

```
Add path in the last of the file.

```bash
export PATH=$PATH:/home/(use your username here)/.local/bin

```
After adding the path and installation is done close the previous terminal and open new one to try this tool.


## How to Install

```bash
https://github.com/Tuba-Saeed/DomainIntel.git

```
Go to the same directory where you clone the tool and type

```bash
pip install . 

```
After completing the installtion you need to type in your terminal  

 
```bash
python3 -m DomainIntel

```
Or You Can Type 

```bash
python3 -m DomainIntel example.com
```





## How to uninstall the tool 
```bash
pip uninstall DomainIntel

```

  
  
