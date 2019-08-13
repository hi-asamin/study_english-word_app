#!/bin/bash
MYSQL=`which mysql`

CREATE_STR="CREATE DATABASE IF NOT EXISTS english_app_db;"
ADD_USER="GRANT ALL ON english_app_db.* TO django@'%' IDENTIFIED BY 'django';"
FLUSH="FLUSH PRIVILEGES;"
SQL="${CREATE_STR} ${ADD_USER} ${FLUSH}"

$MYSQL -u root -p -e "$SQL"
