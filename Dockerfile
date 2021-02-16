FROM python:latest

RUN pip install requests

COPY index.html /
COPY healthcheck.py /

HEALTHCHECK --interval=12s --timeout=12s --start-period=10s CMD python /healthcheck.py

CMD python -m http.server 8080

EXPOSE 8080