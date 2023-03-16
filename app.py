import subprocess
import shlex

from flask import Flask
app = Flask(__name__)

def run_command(command):
    command = "ping -c 1 {}".format(command)
    args = shlex.split(command)
    if args[3]=='127.0.0.1':
        subprocess.Popen(args)
        return "ping done"
    else:
        return "bad"
    

@app.route('/<command>')
def command_server(command):
    return str(run_command(command))
    


if __name__ == '__main__':  
   app.run()
