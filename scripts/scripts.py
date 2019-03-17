import sys
import subprocess


def jevois_inventor():
    if sys.argv[1] == "jevois-inventor":
        subprocess.Popen("jevois-inventor")


jevois_inventor()
