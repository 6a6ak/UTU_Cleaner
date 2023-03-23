#!/bin/bash

function display_menu() {
  echo "Choose an option to clean your Ubuntu server:"
  echo "1. Empty trash and temporary files"
  echo "2. Remove old kernels"
  echo "3. Remove unused packages"
  echo "4. Analyze disk usage"
  echo "0. Exit"
}

while true; do
  display_menu
  read -p "Enter your choice: " choice

  case $choice in
    1)
      echo "Emptying trash and temporary files..."
      sudo apt-get autoclean
      sudo apt-get clean
      rm -rf ~/.cache/thumbnails/*
      rm -rf ~/.cache/*
      ;;

    2)
      echo "Removing old kernels..."
      sudo apt autoremove --purge
      ;;

    3)
      echo "Removing unused packages..."
      sudo apt-get install deborphan
      sudo deborphan | xargs sudo apt-get -y remove --purge
      ;;

    4)
      echo "Analyzing disk usage..."
      sudo apt-get install ncdu
      ncdu /
      ;;

    0)
      echo "Exiting..."
      exit 0
     
