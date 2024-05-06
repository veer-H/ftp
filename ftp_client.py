# Import Module
import ftplib
from ftplib import FTP_TLS
ftp=FTP_TLS()

server_address = "127.0.0.1"
username = "user"
password = "password"


# Connect FTP Server
ftp_server = ftplib.FTP(server_address, username, password)

# force UTF-8 encoding
ftp_server.encoding = "utf-8"

# Enter File Name with Extension
filename = "uptime.tsv"

# Write file in binary mode
with open(filename, "wb") as file:
	# Command for Downloading the file "RETR filename"
	ftp_server.retrbinary(f"RETR {filename}", file.write)

# Get list of files
ftp_server.dir()

# Display the content of downloaded file
file= open(filename, "r")
print('File Content:', file.read())

# Close the Connection
ftp_server.quit()
