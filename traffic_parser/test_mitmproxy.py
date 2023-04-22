from mitmproxy import http

# Response function that is used whenever mitmproxy encounters an https response message
def response(flow: http.HTTPFlow) -> None:
    # Check if the response has Set-Cookie headers
    if ("set-cookie" in flow.response.headers):
        # Get the Set-Cookie headers and extract the cookie values
        set_cookie_headers = flow.response.headers.get_all("set-cookie")
        cookies = []

        # Add all found cookie headers into the cookies list
        for set_cookie_header in set_cookie_headers:
            cookies.extend(set_cookie_header.split(";"))

        # If any cookie headers are found, store into a file
        if (cookies):
            # Save the cookies to a file
            with open("cookies.txt", "a") as f:
                f.write("### Cookie ###\n\n")
                for cookie in cookies:
                    if (cookie[0] != " "):
                        f.write(f"Source domain: {flow.request.pretty_host}\n")
                        f.write(f"Source IP address: {flow.server_conn.ip_address[0]}\n")

                    # f.write("\n".join(cookies))
                    f.write(cookie)
                    f.write("\n")
                f.write("\n\n\n")

