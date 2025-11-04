#! /bin/bash

usage() {
    echo "Usage: run_code <port>"
}

check_host1_running () {
    echo  "Checking that server is running: "
    if ! docker compose ps server | grep server > /dev/null; then
        echo "⚠️ Warning: server is not running, start with \"docker compose up -d\""
        exit 1
    else
        echo "✅ Pass: server is running."
    fi
}


if [[ $1 == "help" || $1 == "-h" ]]; then
    echo "Help"
    usage
    exit
fi

if [[ $# -ne 1 ]]; then
    echo "Error: Incorrect number of parameters"
    usage
    exit 1
fi


run_code() {
    docker compose exec server python3 server-answers.py $1
}

if check_host1_running; then
    run_code $1
fi
