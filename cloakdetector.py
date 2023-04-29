import socket
import sqlite3
import pandas as pd
import sys
from url-checker import url_func

def is_first_party_domain(domain_name, cname_domain_name):
    return domain_name.endswith(cname_domain_name)

def get_original_ip(domain_name):
    try:
        return socket.gethostbyname(domain_name)
    except:
        return None

def check_domain(domain_name):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    # Check for A type records
    cur.execute("SELECT hasAType FROM CNAMEpackets WHERE domainName = ?", (domain_name,))
    a_type_records = cur.fetchall()
    has_a_type_record = False
    for record in a_type_records:
        if record[0] == 1:
            has_a_type_record = True

    # Check for CNAME records
    cur.execute("SELECT CNAMEAlias FROM CNAMEpackets WHERE domainName = ?", (domain_name,))
    cname_records = cur.fetchall()
    has_cname_record = False
    cname_domain_name = None
    for record in cname_records:
        has_cname_record = True
        cname_domain_name = record[0]

    # Check if CNAME domain is a first-party domain
    is_first_party = False
    if has_cname_record:
        is_first_party = is_first_party_domain(domain_name, cname_domain_name)

    # Check if IP address is an IP address of the original URL
    original_ip = get_original_ip(domain_name)
    is_original_ip = False
    if original_ip:
        cur.execute("SELECT ip FROM ip WHERE domainName = ?", (domain_name,))
        ip_records = cur.fetchall()
        for record in ip_records:
            if record[0] == original_ip:
                is_original_ip = True

    conn.commit()
    conn.close()

    return has_a_type_record, has_cname_record, is_first_party, is_original_ip

domain_name = input("Enter domain name: ")
has_a_type_record, has_cname_record, is_first_party, is_original_ip = check_domain(domain_name)
print("Has A type record:", has_a_type_record)
print("Has CNAME record:", has_cname_record)
print("Is CNAME domain a first-party domain:", is_first_party)
print("Is domain IP address an IP address of the original URL:", is_original_ip)
