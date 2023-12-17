#!/bin/bash
set -e
. /home/ubuntu/.bashrc
export PATH="/usr/local/bin:/usr/bin:/bin"

git pull > /tmp/git_changes.txt

if grep -q "Already up to date." /tmp/git_changes.txt; then
    echo "NO CHANGES"
else
    echo "Reloading..."
    export LATEST_COMMIT=$(git log -1 --format="%H")
    docker-compose build
    docker-compose up -d
fi
