"""
Monitors our code & docs for changes
"""
import os
import sys
import subprocess
import datetime
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

BASEDIR = os.path.abspath("C:/Documents and Settings/papenetbertdel-cp/Mes documents/GitHub/RapidNews/extra")

def get_now():
    "Get the current date and time as a string"
    return datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

def build_docs():
    """
    Run the Sphinx build (`make html`) to make sure we have the
    latest version of the docs
    """
    
    print >> sys.stderr, "Building docs at %s" % get_now()
    f=os.popen('pelican . -o ../ -s pelicanconf.py')
    for i in f.readlines():
        print "myresult:",i,



def getext(filename):
    "Get the file extension."

    return os.path.splitext(filename)[-1].lower()

class ChangeHandler(FileSystemEventHandler):
    """
    React to changes in Python and Rest files by
    running unit tests (Python) or building docs (.rst)
    """

    def on_any_event(self, event):
        "If any file or folder is changed"
        if getext(event.src_path) != 'publish.py':
            print event
            build_docs()
        

            
def main():
    """
    Called when run as main.
    Look for changes to code and doc files.
    """

    while 1:
    
        event_handler = ChangeHandler()
        observer = Observer()
        observer.schedule(event_handler, BASEDIR, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

if __name__ == '__main__':
    main()
