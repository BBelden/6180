#!/bin/bash

python3 -m http.server --cgi 5994 &   ## use one of my rbutler ports
node child_process_spawn.js                      ## should use one of your ports

