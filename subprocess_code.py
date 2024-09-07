import subprocess

#subprocess.call(["calc"], shell=True) #Calculator application opens

#out = subprocess.check_call(["cmd", "/c", "calc"])

out = subprocess.check_output(["cmd", "/c", "whoami"])

print("The output was: {}".format(out.decode()))