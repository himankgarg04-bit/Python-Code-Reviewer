import subprocess


def getDiff():
    diff =subprocess.run(["git", "diff"], text=True)
    return diff


print(getDiff())
