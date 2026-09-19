import subprocess


def getDiff():
    diff =subprocess.check_output(["git", "show"], text=True)
    return diff


print(getDiff())
