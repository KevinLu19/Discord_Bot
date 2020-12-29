#!/bin/sh

TIMEOUT="5s"

while : ; do
    cd bot/
    echo "Restarting in $TIMEOUT"
    sleep $TIMEOUT
done