import subprocess
import shlex

from flask import Flask
app = Flask(__name__)

def run_command(command):
    command = shlex.quote(command)
    ot = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE).communicate()[0]
    return ot

@app.route('/<command>')
def command_server(command):
    return run_command(command)

if __name__ == '__main__':  
   app.run()
