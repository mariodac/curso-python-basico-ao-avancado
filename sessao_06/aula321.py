import subprocess
import os
import re


encoding = 'utf-8'
cmd = ['ping', '8.8.8.8', '-c', '4']
proc = subprocess.run(
    cmd,
    capture_output=True
)

if os.name == 'nt':
    encoding = 'cp'
    get_encoding = subprocess.run('chcp', capture_output=True, text=True, shell=True)
    code = re.search(r'[0-9]+', get_encoding.stdout)
    if code:
        encoding = f'cp{code.group()}'
    else:
        encoding = 'cp850'
    
    cmd = ['ping', '8.8.8.8',]
    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        encoding=encoding
    )
# print(proc.args)
# print(proc.stderr)
print(proc.stdout)
# print(proc.returncode)
