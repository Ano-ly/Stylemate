#!/usr/bin/env bash
# Set up for Stylemate web application

# Run api and web_app in two different sessions

tmux new-session -s stylemate_web_app -c ./frontend -d 'python3 -m web_app'
tmux new-session -s stylemate_api -d 'python3 -m api.v1.stylemate_app'
