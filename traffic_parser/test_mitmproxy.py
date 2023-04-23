from mitmproxy import http

# Response function that is used whenever mitmproxy encounters an https response message
def response(flow: http.HTTPFlow) -> None:
    # Check if the response has Set-Cookie headers
    if ("set-cookie" in flow.response.headers):
        # Get the Set-Cookie headers and extract the cookie values
        set_cookie_headers = flow.response.headers.get_all("set-cookie")
        cookies = []

        # Get the source domain and IP address
        src_domain = flow.request.pretty_host
        src_ip = flow.server_conn.ip_address[0]
        with open("cookies.txt", "a") as f:


            # Parse through each Set-Cookie header found in the HTTPS packet
            for set_cookie_header in set_cookie_headers:
                cookies = set_cookie_header.split(";")
                Secure = False
                httpOnly = False
                domain = ""

                # Parse through each value in the Set-Cookie header and write values to file
                for cookie in cookies:
                    # Check if any of the current header values are secure, httponly, or domain attributes
                    if (cookie):
                        if (cookie == " Secure"):
                            Secure = True
                        if (cookie == " HttpOnly"):
                            httpOnly = True
                        if (cookie[:7] == " domain="):
                            domain = cookie[8:]
                
                f.write("### Cookie ###\n\n")
                f.write() 



        # # If any cookie headers are found, store into a file
        # if (cookies):
        #     # Save the cookies to a file
        #     with open("cookies.txt", "a") as f:
        #         f.write("### Cookie ###\n\n")
        #         all_cookies = []
        #         cookie = "\n".join(cookies)
                
        #         for i in cookie.split("\n"):
        #             if (i[0] != " "):
                        


                # for cookie in cookies:
                #     if (cookie[0] != " "):
                #         f.write(f"Source domain: {flow.request.pretty_host}\n")
                #         f.write(f"Source IP address: {flow.server_conn.ip_address[0]}\n")

                #     f.write(cookie)

                #     f.write("\n")
                # f.write("\n\n\n")

