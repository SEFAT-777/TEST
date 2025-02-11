import os, sys, platform
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    os.system(f"mv checker.cpython-312.so {sys.path[2]}/checker.cpython-312.so")
    import TEST
else:
    sys.exit("32 bit not work")
