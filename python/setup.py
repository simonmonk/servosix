from distutils.core import setup
import os

setup(name='servosix', version='1.0', py_modules=['servosix'])

print("Installing ServoBlaster by Richard Hirst")
os.system("sudo make")
os.system("sudo make install")