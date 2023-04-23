import os
import sys
import subprocess
import time
import threading

def run_proxy(args):
    port = args[0]
    command = ["mitmproxy", "-q", "-m", "transparent", "-s", "traffic_parser/mitmproxy_script.py", "--listen-host", "localhost", "-p", str(port)]
    subprocess.run(command)
    time.sleep(15)
    return

# Check if a port is specified in command line call
if (len(sys.argv) < 2):
    print("Error: No port specified")
    exit(0)

port = sys.argv[1]

proxy_thread = threading.Thread(target=run_proxy, args=[port])
proxy_thread.start()


