#!/bin/bash
# Author: massard-t/

readonly TAG=${TAG:-'3.5'}

docker run \
        -d \
        --name mongo \
        -v "$PWD/mongo_data:/data/db" \
        --rm \
        "mongo:$TAG"
