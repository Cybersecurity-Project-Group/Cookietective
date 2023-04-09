# USAGE: mitmproxy -s path/to/http_manipulate_cookies.py
from mitmproxy import http
from typing import List, Dict
import json


# -- Helper functions --
def load_json_cookies():
    """
    Load a particular json file containing a list of cookies.
    """
    with open(PATH_TO_COOKIES, "r") as f:
        return json.load(f)
# NOTE: or just hardcode the cookies as [{"name": "", "value": ""}]


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

PATH_TO_COOKIES = "./cookies.json"  # insert your path to the cookie file here
FILTER_COOKIES = {"userdata", "_ga"}  # update this to the specific cookie names you want to remove
# NOTE: we use a set for lookup efficiency

# -- Main interception functionality --

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

