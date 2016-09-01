#
# SETTING UP YOUR MACHINE (for Linux/Ubuntu)
#

You need to install:
- Latest Java JDK http://www.oracle.com/technetwork/java/javase/downloads/index.html
- Android Studio or SDK https://developer.android.com/studio/index.html
- NodeJS (+npm) https://nodejs.org/en/
- Appium http://appium.io
- Python (+some libs) https://www.python.org/
- Android Emulator or Genymotion

Make sure you have python installed. (Pre-installed on Macs)
Check Python version is atleast 2.7
$ python --version

python can be installed on linux using
$ sudo add-apt-repository ppa:fkrull/deadsnakes
$ sudo apt-get update
$ sudo apt-get install python2.7

Check if 'pip' module is installed.
$ pip

Install pip if not installed
$ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py > get-pip.py
$ sudo python get-pip.py
$ rm get-pip.py

Install Python 'selenium' module
$ sudo pip install selenium

Verify that selenium is installed
$ pip freeze | grep selenium

Install additional libs
$ sudo pip install nose_parameterized
$ sudo pip install nose

#
# RUNNING THE TEST
#

- Run Appium
$ appium

- Connect android phone to pc or run any Emulator
- Run command
$ adb devices
- Get your Android device name
```ivanello@t430u:~/project/appium calc$ adb devices
List of devices attached
*73ffacfe*	device
*emulator-5554*	device```
- And put it to script _desired_caps['deviceName']_
- Check and change _desired_caps['platformVersion']_
- Run the script
$ python calc.py
or
$ nosetests -v calc.py
