# call comparator.py with a comma-separated list of websites
#
# example: python3 comparator.py google.com,pokenoms.com,youtube.com,polandki.pl,bmwgroup.com
#
# output table indicates if passed sites are present (1) or not (0) 
# in the Majestic Million and NoTracking lists

import sys
import pandas as pd

# read in MajesticMillion and NoTracking lists as sets
with open('majmill_list.txt', 'r') as f:
    majmill = set(f.read().splitlines())

with open('notrack_list.txt', 'r') as f:
    notrack = set(f.read().splitlines())

# get input list of strings from command-line arguments
stringsin = sys.argv[1].split(',')

# create output table as a DataFrame
outtable = pd.DataFrame({'Address': stringsin,
                         'MajesticMillion': [1 if s in majmill else 0 for s in stringsin],
                         'NoTracking': [1 if s in notrack else 0 for s in stringsin]})

# print output table
print(outtable)

