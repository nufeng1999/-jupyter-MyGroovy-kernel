FROM jupyter/minimal-notebook
MAINTAINER Xaver Klemenschits <klemenschits@iue.tuwien.ac.at>

USER root

# Install vim and ssh
RUN apt-get update
RUN apt-get install -y vim openssh-client

WORKDIR /tmp

COPY ./ jupyter_MyGroovy_kernel/

RUN pip install --no-cache-dir -e jupyter_MyGroovy_kernel/ > piplog.txt
RUN cd jupyter_MyGroovy_kernel && jupyter_MyGroovy_kernel --user > installlog.txt

WORKDIR /home/$NB_USER/

USER $NB_USER
