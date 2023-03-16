import subprocess

from flask import Flask
app = Flask(__name__)

def run_command(command):
    command = "ping -c 1 {}".format(command)
    args = shlex.split(command)
    return subprocess.Popen(args)
    

@app.route('/<command>')
def command_server(command):
    return run_command(command)
