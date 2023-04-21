# Info
The purpose of the URL scanner is come up with a confidence score if URLS are related. This is accomplished by scanning through the URLS and determining if there are strings in common and how mnay strings there are.

## Implementation Ideas
Find a function that allows for the longest string to be found, as well as any common strings in the URL, with symbols as delinitors.

### Scanner update
The scanner that is currently implemented is great for checking if the domains have a common top-level domain, but is not effective for finding if different top-level domains belong to the same owner. I would like to update the scanner to be more robust, for example:

    *Update to scan strings for longest sequence of letters in common
        "www.hilton.com" and "www.hilton-hotels.com" would catch 'hilton' as being the longest sequence of letters in common
    *Update to find multiple of these "long letter sequences"
        "www.hotels.hilton.com" and "www.hiltonhotels.com" would catch 'hilton' and 'hotel' as both being mentioned in the URL.

### Class to store data
