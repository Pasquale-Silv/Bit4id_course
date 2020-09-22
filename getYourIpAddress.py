import socket

hostname = socket.gethostname()
print(f"Hostname: \n{hostname}")

ipAddress = socket.gethostbyname(hostname)
print("\nMy IP address is:\n{}".format(ipAddress))
