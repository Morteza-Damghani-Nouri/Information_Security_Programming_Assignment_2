import subprocess
host_ip = input("Enter the IP address of the host which you want to scan: ")
subprocess.run("nmap -sV " + host_ip)
















