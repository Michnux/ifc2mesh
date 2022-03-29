#FROM ubuntu:20.04
FROM python:3.8

#RUN apt-get update
#RUN apt-get -y install python3.8
#RUN apt-get -y install python3-pip

RUN python3 -m pip install alteia


COPY script_dir /home/script_dir/

#CMD ["sleep", "1d"]
CMD ["python3", "/home/script_dir/main.py"]