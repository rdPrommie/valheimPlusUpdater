# this file starts the program
import socket, sys, time, threading, tkinter
from tkinter import messagebox
from datetime import datetime

from version_scrapping import VersionScrapper as Scrapper
from gui import GUIDrawing

NEXUSMODS_DOMAIN_URL = "www.nexusmods.com"
WAIT_TIME_SECONDS = 180

def test_connection(hostname):
    try:
        sock = socket.create_connection((hostname, 80))
        if sock is not None:
            print("Connection test for "+ hostname + " successful.", end='\n', file=sys.stdout, flush=True)
            sock.close()
        return True
    except:
        raise ConnectionError("404: There is no Internet connection, or NexusMods website is unavailable at the moment.")
    return False

def running_scrapper():
    codes = Scrapper().scrap_codes()
    #todo: if version is not the latest version

def main():
    GUIDrawing.draw()
    sys.exit()
    try:
        test_connection(NEXUSMODS_DOMAIN_URL)
        sys.exit()
        ticker = threading.Event()
        #running_scrapper()
        while not ticker.wait(WAIT_TIME_SECONDS):
            running_scrapper()
    except ConnectionError as error:
        print("Error: " + repr(error), end='\n', file=sys.stdout, flush=True)
        messagebox.showerror("Error!", "Error: " + repr(error))
    
if __name__ == "__main__":
    main()