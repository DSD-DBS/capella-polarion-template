FROM python:3.12.3-slim
LABEL maintainer="Polarion Team at SBB <polarion-opensource@sbb.ch>"

RUN apt-get update && \
    apt-get --yes --no-install-recommends install python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0 fonts-liberation chromium && \
    apt-get clean autoclean && \
    apt-get --yes autoremove && \
    pip install --no-cache-dir weasyprint==62.3  && \
    rm -rf /var/lib/apt/lists/*

ENV WORKING_DIR=/opt/weasyprint
ENV CHROME_EXECUTABLE_PATH=/usr/bin/chromium

WORKDIR ${WORKING_DIR}

ENTRYPOINT [ "weasyprint" ]
