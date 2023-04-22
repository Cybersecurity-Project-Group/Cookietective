FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y 
RUN apt-get install python3 python3-pip ipython3 wget -y
RUN apt-get install firefox -y

WORKDIR /CoolestProject

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "crawler/crawler.py", "sample_urls.txt", "1", "3" ]