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
tn.write("conf t\n")
tn.write("int loopback10\n")
tn.write("ip add 10.10.10.10 255.0.0.0\n")
tn.write("int loopback20\n")
tn.write("ip add 20.20.20.20 255.0.0.0\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()


