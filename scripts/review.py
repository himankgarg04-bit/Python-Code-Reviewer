import subprocess


def getDiff():
    diff =subprocess.check_output(["git", "diff"], text=True)
    return diff


print(getDiff())
