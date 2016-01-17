#!/usr/bin/env bash

apt-get update
#DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" upgrade

#http://superuser.com/questions/164553/automatically-answer-yes-when-using-apt-get-install
apt-get -y install git
apt-get -y install tmux
apt-get -y install curl
#apt-get -y install nodejs
#apt-get -y install npm

#npm install -g node-inspector

npm install -g bower

#npm -g install phaser

bower install phaser

wget https://bootstrap.pypa.io/get-pip.py
python ./get-pip.py
