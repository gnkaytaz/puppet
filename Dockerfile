FROM cbeams/vanitygen:latest
RUN apt-get update
RUN apt-get install -y python
ADD word.py .
