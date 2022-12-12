#!/bin/bash
# setup script for running exbitron cli
# make the file executable first with chmod +x setup.sh and then run ./setup.sh

# checking if we are using gnu/linux
if [[ "$OSTYPE" == "linux-gnu"* ]]; then

    # checking if python is not already installed
    if ! hash python; then

        # checking if we are using debian/ubuntu derived os
        if command -v apt-get >/dev/null; then
            OS=$(cat /etc/*-release)
            echo "Installing Python 11 with APT on $OS..."
            sudo apt-get update
            sudo apt-get -y install python3.11
            echo "Successfully installed Python on Ubuntu/Debian!"
        
        # checking if we are using centos or similar with yum package manager
        elif command -v yum >/dev/null; then
            OS=$(cat /etc/*-release)
            echo "Installing Python 11 with Yum on $OS..."
            yum update
            yum install -y openssl-devel bzip2-devel libffi-devel
            yum groupinstall "Development Tools"
            wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0a4.tgz
            tar -xzf Python-3.11.0a4.tgz
            echo "Successfully installed Python on Centos!"
        else
            echo "Could not install Python on your OS!"
        fi
    fi

# checking if we are using macOS
elif [[ "$OSTYPE" == "darwin"* ]]; then

    # checking if python is not already installed
    if ! hash python; then
        echo "Installing Python 11 with Brew on $OS..."
        brew install python@3.11
    fi

else
    echo "Could not install Python on your OS!"
fi

python cli.py