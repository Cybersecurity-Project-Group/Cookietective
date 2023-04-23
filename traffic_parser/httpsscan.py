from mitmproxy import http
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import sql.sql_func as sql

from mitmproxy.options import Options
from mitmproxy.tools.dump import DumpMaster
from mitmproxy.addons.proxyserver import Proxyserver
import threading
import asyncio
import time

# Addon class to be used for mitmproxy
# class Addon(object):
#     # Response function that is used whenever mitmproxy encounters an https response message
#     def response(flow: http.HTTPFlow) -> None:
#         # Check if the response has Set-Cookie headers
#         if ("set-cookie" in flow.response.headers):
            
#             # Get the Set-Cookie headers and extract the cookie values
#             set_cookie_headers = flow.response.headers.get_all("set-cookie")

#             # Get the source domain and IP address
#             src_domain = flow.request.pretty_host
#             src_ip = flow.server_conn.ip_address[0]
#             # Parse through each Set-Cookie header found in the HTTPS packet
#             for set_cookie_header in set_cookie_headers:
#                 cookies = set_cookie_header.split(";")
#                 Secure = False
#                 httpOnly = False
#                 domain = ""

#                 # Parse through each value in the Set-Cookie header and write values to file
#                 for cookie in cookies:
#                     # Check if any of the current header values are secure, httponly, or domain attributes
#                     if (cookie):
#                         if (cookie == " Secure"):
#                             Secure = True
#                         if (cookie == " HttpOnly"):
#                             httpOnly = True
#                         if ("domain=" in cookie):
#                             domain = cookie[8:]
                    
#                     sql.insertCookieEntry(src_domain, src_ip, domain, httpOnly, Secure)

class Addon(object):
    def __init__(self):
        self.num = 1

    def request(self, flow):
        flow.request.headers["count"] = str(self.num)

    def response(self, flow):
        self.num = self.num + 1
        flow.response.headers["count"] = str(self.num)
        print(self.num)

# Main function for mitmproxy that specifies options and runs mitmproxy
async def run_proxy(port):
    
    settings = Options(
        listen_host='localhost',
        listen_port=port
        # mode='transparent',
        # scripts=["mitmproxy_script.py"]
    )
    m = DumpMaster(settings, with_termlog=True)
    m.addons.add(Addon())

    # Run the proxy until it times out, then shutdown the proxy
    try:
        await asyncio.wait_for(m.run(), timeout=15)
    except asyncio.TimeoutError:
        m.shutdown()


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(run_proxy(8080))
finally:
    loop.close()
    
    


