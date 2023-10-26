import os
import subprocess
os.system("ls")
subprocess.run(["ls"])
subprocess.run(["ls","-l"])
subprocess.run(["ls","-l","README.md"])

command="uname"
commandArguement="-a"
print(f'Gathering system information with command: {command} {commandArguement}')
subprocess.run([command,commandArguement])

command="ps"
commandArguement="-x"
print(f'Gathering system information with command: {command} {commandArguement}')
subprocess.run([command,commandArguement])