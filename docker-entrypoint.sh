#!/bin/sh

echo Start docker-entrypoint.sh

export connected="no"
while [ $connected = "no" ]
do
  mysql -h db -u root -proot -e 'show databases;'
  echo $?
  echo "do"
  if [ $? -eq 0 ] ; then
    export connected="yes"
  fi
  sleep 1
done

python reminder/manage.py collectstatic --noinput

python reminder/manage.py makemigrations
python reminder/manage.py migrate

python reminder/manage.py loaddata reminder/fixtures/professors.json
python reminder/manage.py loaddata reminder/fixtures/lectures.json

supervisord