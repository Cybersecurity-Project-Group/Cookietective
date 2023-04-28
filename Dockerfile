FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y 
RUN apt-get install python3 python3-pip ipython3 wget -y
RUN apt-get install firefox -y

WORKDIR /home/CoolestProject

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY Dockerfile .
COPY database.db .
COPY crawler/ ./crawler
COPY traffic_parser/ ./traffic_parser
COPY sql/ ./sql
COPY sample_urls.txt .

CMD ["python3", "traffic_parser/dnsscan.py"]
# ENTRYPOINT [ "python3", "crawler/crawler_dfs.py"]
# CMD ["sample_urls.txt", "0", "3"]