#!/bin/bash
./build.sh
docker rm -f istanbul-tools-http-api 2> /dev/null
docker run -tid -p 8080:8080 --name istanbul-tools-http-api councilbox/istanbul-tools-http-api
