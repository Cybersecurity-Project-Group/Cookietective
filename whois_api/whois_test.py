import whois
import threading
from time import sleep

def get_whois_data(whoisDomain):
    print("Thread started to look up " + whoisDomain)
    global whoisData
    whoisData = whois.whois(whoisDomain)

    # set the event to indicate that the whois call is completed
    whoisFound.set()
    sleep(1)

'''Test Code'''
# define the domain names
domainName = "linkedin.com"
originalURL = "play.google.com"

print("Domain Name: " + domainName)
print("Original URL: " + originalURL)


# create an event object
whoisFound = threading.Event() #Sets an event that is

# Pull data from Whois
domainNameWhoisThread = threading.Thread(target=get_whois_data, args=(domainName,))
domainNameWhoisThread.start()
whoisFound.wait()
domainNameWhois = whoisData
print(domainNameWhois.org)

# reset the event object
domainNameWhoisThread.join()
whoisFound.clear()

# pull data from Whois for other thread
originalURLWhoisThread = threading.Thread(target=get_whois_data, args=(originalURL,))
originalURLWhoisThread.start()
whoisFound.wait()
originalURLWhois = whoisData
print(originalURLWhois.org)

# reset these
originalURLWhoisThread.join()
whoisFound.clear()