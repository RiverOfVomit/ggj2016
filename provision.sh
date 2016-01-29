#!/usr/bin/env bash

apt-get update
#DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" upgrade

#http://superuser.com/questions/164553/automatically-answer-yes-when-using-apt-get-install
apt-get -y install git
apt-get -y install tmux
apt-get -y install curl
#apt-get -y install nodejs
#apt-get -y install npm
apt-get -y install rubygems

# http://stackoverflow.com/questions/11094718/error-command-gcc-failed-with-exit-status-1-while-installing-eventlet
apt-get -y install python-dev
apt-get -y install libevent-dev

#npm install -g node-inspector

npm install -g bower
npm install -g debug
npm install -g express
npm install -g express-generator
npm install -g swig

#npm -g install phaser
bower install phaser

wget https://bootstrap.pypa.io/get-pip.py
python ./get-pip.py

pip install Flask
pip install flask-socketio

#pip install virtualenv
#pip install virtualenvwrapper # http://docs.python-guide.org/en/latest/dev/virtualenvs/
#export WORKON_HOME=~/Envs
#source /usr/local/bin/virtualenvwrapper.sh

# or:
# http://virtualenvwrapper.readthedocs.org/en/latest/index.html
# You will want to add the command to source /usr/local/bin/virtualenvwrapper.sh to your shell startup file

gem install rhc

git clone https://github.com/photonstorm/phaser/tree/v2.4.4
