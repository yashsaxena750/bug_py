import subprocess

from flask import Flask
app = Flask(__name__)

def run_command(command):
    #command = shlex.split(shlex.quote(command))
    return subprocess.Popen(command)
    

@app.route('/<command>')
def command_server(command):
    return run_command(command)
