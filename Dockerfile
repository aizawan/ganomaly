# https://github.com/aizawan/.env/blob/master/docker/pth/Dockerfile
FROM ubuntu.pth:latest

ADD requirements.txt /tmp/requirements.txt

RUN conda create -n ganomaly python=3.7
SHELL ["conda", "run", "-n", "ganomaly", "/bin/bash", "-c"]
RUN pip install --user --requirement /tmp/requirements.txt

WORKDIR /workspace

CMD ["/bin/zsh"]
