FROM python:3.11-slim

ENV debian_frontend=noninteractive

WORKDIR /code
COPY host_scripts/start.sh /tmp/start.sh

RUN apt update && \
    apt install -y curl jq && \
    chmod u+x /tmp/start.sh && \
    echo "swen-lab-l5-server" > /etc/hostname

RUN pip3 install black

ENTRYPOINT ["/tmp/start.sh" ]