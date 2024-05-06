import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Define variables
FTP_USERNAME = "user"
FTP_PASSWORD = "password"
FTP_DIRECTORY = "D:/TCP"
FTP_PORT = 21

def run_ftp_server():
    # Instantiate an authorizer
    authorizer = DummyAuthorizer()
    authorizer.add_user(FTP_USERNAME, FTP_PASSWORD, FTP_DIRECTORY, perm='elradfmw')

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Instantiate FTP server
    server = FTPServer(("0.0.0.0", FTP_PORT), handler)

    # Start the FTP server
    server.serve_forever()

if __name__ == "__main__":
    run_ftp_server()
