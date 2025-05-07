#!/bin/bash
# Skrypt automatyzujący commit i push
git add .
git commit -m "${1:-Aktualizacja}"
git push
