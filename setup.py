import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
with open("src/Requirements.txt") as f:
    for i in f:
        install (i)
