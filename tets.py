import os
import subprocess

def main():
    while True:
        command = input("$ ")
        if command == "exit":
            break
        elif command == "help":
            print("psh: a simple shell written in Python")
        else:
            execute_commands(command)
