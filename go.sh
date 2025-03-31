# /bin/sh
docker run -it --rm -v "$PWD":/app -w /app -p 8000:8000 --entrypoint=/bin/bash python:3.11