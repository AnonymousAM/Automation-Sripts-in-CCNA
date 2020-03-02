import getpass
import sys
import telnetlib

HOST="192.168.0.200"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")

if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("123\n")
tn.write("r1\n")
if tn.read_until("Trying r1 (1.1.1.1, 2033)...")
  	tn.write("clear line 33\n")
	tn.read_until("[confirm]\n")

while tn.read_until("% connection refused by remote host")

tn.write("end\n")
tn.write("exit\n")

print tn.read_all()


