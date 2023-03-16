import subprocess
import shlex

from flask import Flask
app = Flask(__name__)

def run_command(command):
    command = "ping -c 1 {}".format(command)
    args = shlex.split(command)
    if args[3]=='127.0.0.1':
        subprocess.Popen(args)
        return 1
    else:
        return 0
    

@app.route('/<command>')
def command_server(command):
    if run_command(command) == 1:
        return "ping done"
    else:
        return "failed!"
    


if __name__ == '__main__':  
   app.run()
