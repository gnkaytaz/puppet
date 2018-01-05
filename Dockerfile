FROM cbeams/vanitygen:latest
RUN apt-get update
RUN apt-get install -y python
RUN pip install -i https://pypi.python.org/simple/ base58
ADD word.py .
