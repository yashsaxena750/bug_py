import subprocess
import shlex
import html

from flask import Flask
app = Flask(__name__)
uname = "check"
password = "news"
def run_command(command):
    #command = shlex.split(command)
    API_KEY = "fgmffdgjdskgjsrr374989ridjg"
    #ot = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE).communicate()[0]
    ot = subprocess.Popen(command,shell=True)
    return ot

@app.route('/<command>')
def command_server(command):
    return html.escape(run_command(command))

if __name__ == '__main__':  
   app.run()
