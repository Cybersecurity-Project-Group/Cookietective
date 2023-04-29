FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y
RUN apt-get install python3 python3-pip ipython3 wget -y
RUN apt-get install firefox -y
RUN apt-get install sqlite3 -y
RUN apt-get install libpcap0.8 -y
RUN apt-get install mitmproxy -y

WORKDIR /home/CoolestProject

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY Dockerfile .
COPY database.db .
COPY crawler/ ./crawler
COPY traffic_parser/ ./traffic_parser
COPY sql/ ./sql
COPY sample_urls.txt .
COPY test2.sh .
COPY mitmproxy-ca-cert.crt .

RUN sqlite3 database.db "delete from cnamepackets" ".exit"

ENTRYPOINT ["bash", "test2.sh"]
# CMD bash test.sh 
# CMD python3 traffic_parser/dnsscan.py & python3 crawler/crawler_dfs.py sample_urls.txt 0 3
# CMD mitmdump -s traffic_parser/mitmproxy_script.py & sudo python3 traffic_parser/dnsscan.py & python3 crawler/crawler_dfs.py sample_urls.txt 0 3
# ENTRYPOINT [ "python3", "crawler/crawler_dfs.py"]
# CMD ["sample_urls.txt", "0", "3"]
