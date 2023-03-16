import subprocess

from flask import Flask
app = Flask(__name__)

def run_command(command):
    if command=='id':
        return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()
    else:
        return "RCE"

@app.route('/<command>')
def command_server(command):
    return run_command(command)
