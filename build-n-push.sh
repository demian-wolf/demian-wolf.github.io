#!/bin/bash

rm -rf flask_src/build
rm -rf flask_src/__pycache__
python3 flask_src/freeze.py
rsync -avh --dry-run flask_src/build .
git commit -a -m "Updated CodeClub page with new information"
git push
