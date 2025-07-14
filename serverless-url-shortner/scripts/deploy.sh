#!/bin/bash

cd ../lambda || exit 1

zip shorten_url.zip shorten_url.py
zip redirect_url.zip redirect_url.py

echo "Zipped both Lambda functions."
