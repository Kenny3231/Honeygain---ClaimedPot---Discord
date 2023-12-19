FROM python:alpine
COPY honeypot.py honeypot.py
COPY crontab.txt /crontab.txt
COPY entrypoint.sh /entrypoint.sh
RUN chmod 755 /honeypot.py /entrypoint.sh
RUN /usr/bin/crontab /crontab.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pyHoneygain discord-webhook
CMD ["/entrypoint.sh"]