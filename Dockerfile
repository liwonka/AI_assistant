FROM nvcr.io/nvidia/pytorch:22.08-py3

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get install -y --no-install-recommends \
    ca-certificates ninja-build build-essential git cmake wget ffmpeg libsm6 libxext6 unzip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /srv/www/sim-swap
COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt
CMD python 

