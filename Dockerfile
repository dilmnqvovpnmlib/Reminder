FROM python:3.7

MAINTAINER dilmnqvovpnmlib <simplelpmis6@gmail.com>

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ENV TZ Asia/Tokyo

RUN apt-get update
RUN apt-get install -y nginx && \
  apt-get install -y vim && \
  apt-get install -y curl && \
  apt-get install -y supervisor && \
  apt-get install -y mariadb-client

# make working directory.
RUN mkdir /app
WORKDIR /app
ADD . /app

# install python packages.
RUN pip install -r requirements.txt

# copy configuration files.
COPY ./conf/default /etc/nginx/sites-enabled/default
COPY ./conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 80

# Setting .bashrc
RUN { \
  echo "alias ll='ls -l'"; \
  echo "alias la='ls -A'"; \
  echo "alias l='ls -CF'"; \
  echo "PS1='\[\e[1;34m\][\u@\h \W]\\$ \[\e[m\]'"; \
  } > ~/.bashrc

ENTRYPOINT ["bash", "./docker-entrypoint.sh"]