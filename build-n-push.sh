#!/bin/bash


cleanup () {
    rm -rf flask_src/build
    rm -rf flask_src/__pycache__
}

cleanup
python3 flask_src/freeze.py
rsync -avh --dry-run flask_src/build .
git commit -a -m "Updated build-n-push.sh script"
git push
cleanup
