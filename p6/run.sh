#!/bin/bash

python3 -m http.server --cgi 5994 &   ## use one of my rbutler ports
node p6server.js                      ## should use one of your ports

