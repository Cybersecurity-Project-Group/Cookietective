import sys
import pandas as pd


def comparator(*stringsin):
    # read in MajesticMillion and NoTracking lists as sets
    with open('majmill_list.txt', 'r') as f:
        majmill = set(f.read().splitlines())
    with open('notrack_list.txt', 'r') as f:
        notrack = set(f.read().splitlines())

    # create output table as a DataFrame
    outtable = pd.DataFrame({'Address': stringsin,
                             'MajesticMillion': [1 if s in majmill else 0 for s in stringsin],
                             'NoTracking': [1 if s in notrack else 0 for s in stringsin]})

    # print output table
    print(outtable)
    return outtable
    
stringsin = sys.argv[1:]
comparator(*stringsin)


