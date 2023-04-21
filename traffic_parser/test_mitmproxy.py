# USAGE: mitmproxy -s path/to/http_manipulate_cookies.py
# In order to run the mitmproxy on own machine, need to go to network settings and set Proxies on for 
# http and https into localhost:8080
from mitmproxy import http
from typing import List, Dict
import json


# -- Helper functions --

def stringify_cookies(cookies: List[Dict]) -> str:
    """
    Creates a cookie string from a list of cookie dicts.
    """
    return ";".join([f"{c['name']}={c['value']}" for c in cookies])


def parse_cookies(cookie_string: str) -> List[Dict[str, str]]:
    """
    Parses a cookie string into a list of cookie dicts.
    """
    cookies = []
    for c in cookie_string.split(";"):
        c = c.strip()
        if c:            
            k, v = c.split("=", 1)
            cookies.append({"name": k, "value": v})
    return cookies


def request(flow: http.HTTPFlow) -> None:
    cookie_dict = {}
    for set_cookie_header in flow.request.headers.get_all("Set-Cookie"):
        try:
            cookie = http.cookies.parse_set_cookie_header(set_cookie_header)
            cookie_dict.update(cookie)
        except http.cookies.CookieError as e:
            print(f"Error parsing through Set-Cookies: {e}")
            exit(1)
        except Exception as e:
            print(f"Error parsing through Set-Cookies: {e}")
            exit(1)
    if (len(cookie_dict) > 0):
        with open("cookies.json", "w") as f:
            json.dump(cookie_dict, f, ensure_ascii=False, indent=4)

def response(flow: http.HTTPFlow) -> None:
    cookie_dict = {}
    for set_cookie_header in flow.response.headers.get_all("Set-Cookie"):
        try:
            cookie = http.cookies.parse_set_cookie_header(set_cookie_header)
            cookie_dict.update(cookie)
        except http.cookies.CookieError as e:
            print(f"Error parsing through Set-Cookies: {e}")
            exit(1)
        except Exception as e:
            print(f"Error parsing through Set-Cookies: {e}")
            exit(1)
    if (len(cookie_dict) > 0):
        with open("cookies.json", "w") as f:
            json.dump(cookie_dict, f, ensure_ascii=False, indent=4)

