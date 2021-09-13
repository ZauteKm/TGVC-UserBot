FROM python:latest

ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y ffmpeg opus-tools bpm-tools
RUN python -m pip install --upgrade pip
RUN python -m pip install wheel
RUN python -m pip install pytgcalls[pyrogram] TgCrypto ffmpeg-python psutil

RUN wget -q https://github.com/ZauteKm/TGVC-UserBot/archive/master.tar.gz && \
    tar xf master.tar.gz && rm master.tar.gz

WORKDIR /TGVC-UserBot-master
CMD python3 main.py
