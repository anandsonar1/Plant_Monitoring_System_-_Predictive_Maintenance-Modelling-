# FROM python:3.9-slim-buster
# WORKDIR /python-docker
# RUN apt-get update \
#     && apt-get -y install --reinstall build-essential \
#     && apt-get install -y gcc python-opencv 
# RUN pip3 install --upgrade pip
# COPY requirements.txt requirements.txt
# RUN pip3 install wheel
# RUN pip3 install -r requirements.txt
# COPY . .
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

# FROM python:3.9-slim-buster
# WORKDIR /Flaskfinal_lt
# RUN apt-get update \
#     && apt-get -y install --reinstall build-essential \
#     && apt-get install -y gcc python-opencv 
# RUN pip install --upgrade pip
# COPY requirements.txt requirements.txt
# RUN pip install wheel
# RUN pip install -r requirements.txt
# COPY . .
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0" ]



FROM python:slim-buster
WORKDIR /Flaskfinal_Update 
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install wheel  
RUN pip install -r requirements.txt
COPY . /Flaskfinal_Update
ENTRYPOINT [ "python" ]
CMD [  "run.py" ]