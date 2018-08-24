FROM ubuntu:16.04
RUN apt-get update -y
RUN apt-get install gcc -y
RUN apt-get install python-dev -y
RUN apt-get install build-essential -y 
RUN apt-get install python-setuptools python-pip -y
COPY requirements.txt /src/requirements.txt
COPY app.py /src/app.py
COPY yara_finder/matcher.py /src/yara_finder/matcher.py
COPY yara_finder/__init__.py /src/yara_finder/__init__.py
COPY rules/ /src/rules
COPY yara_finder/uploads/ /src/yara_finder/uploads
RUN pip install -r /src/requirements.txt
CMD python /src/app.py
