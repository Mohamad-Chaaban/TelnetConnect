import telnetlib

HOST = "192.168.232.127"
user = "cisco"
password = "cisco"

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"show ip int br\n")
tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))

tn.get_socket()

tn.close()