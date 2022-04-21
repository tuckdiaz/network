

import paramiko
import getpass

#### Still Under Devolopment ####

hostname = input("Enter the IP Address: ")
username = input("Enter Username: ")
password = getpass.getpass("Enter Password: ")

p = paramiko.SSHClient()

p.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    p.connect(hostname=hostname, username=username, password=password)
except:
    print("[!] Cannot Connect to the SSH Server")
    exit()

print("\n")
stdin, stdout, stderr = p.exec_command("diagnose internet-service id | grep -i microsoft \n")
print(stdout.read().decode())
err = stderr.read().decode()

#showing List of IP Addresses
print("\n")

print("Enter Service ID to get list of IP Addreses \n")
#sid = input ("Enter Service ID: ")
stdin, stdout, stderr = p.exec_command("diagnose internet-service id 327688 \n")
print(stdout.read().decode())
err = stderr.read().decode()


if err:
    print(err)

