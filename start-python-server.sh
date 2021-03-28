#!/bin/bash
PORT=8000
if [ -n "$1" ]
then
  PORT=$1
fi
echo starting server on port $PORT
#python -m CGIHTTPServer $PORT
python3 -m http.server --cgi $1
