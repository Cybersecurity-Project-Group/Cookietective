# Info
The purpose of the Comparator is to quickly identify if a domain name is present in either or both the the Majestic Million and NoTracking lists for easy comparison.

## Explanation
#### python3 comparator.py domain1,domain2,domain3,...
The program is called with a list of domain names and outputs a table indicating if passed domain names are present (1) or not (0) in the Majestic Million and NoTracking lists.
```
python3 comparator.py google.com,pokenoms.com,youtube.com,polandki.pl,bmwgroup.com

Output:
        Address  MajesticMillion  NoTracking
0    google.com                1           0
1  pokenoms.com                0           1
2   youtube.com                1           0
3   polandki.pl                0           1
4  bmwgroup.com                1           0
```

