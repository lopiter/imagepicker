#!/bin/bash

if [ -z "$1" ]
  then
    echo "please input search word ex) run.sh lionking"
    exit
fi
if [ -z "$2" ]
  then
    echo "please input repeat number ex) run.sh lionking 10"
    exit
fi

scrapy crawl nv_imagepicker -a SearchWord=$1 -a iteration=$2
