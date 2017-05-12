FROM python:3.6-alpine

WORKDIR /envcat
ENTRYPOINT ["envcat"]
CMD ["--help"]
COPY . /app
RUN cd /app && python setup.py install

