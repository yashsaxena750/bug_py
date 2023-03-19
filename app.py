import subprocess
import shlex
import html

from flask import Flask
app = Flask(__name__)

def run_command(command):
    #command = shlex.quote(command)
    #ot = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE).communicate()[0]
    ot = subprocess.Popen(['cat', '/python-docker/app.py', command])
    return ot

@app.route('/<command>')
def command_server(command):
    return html.escape(run_command(command))

if __name__ == '__main__':  
   app.run()
