# SETTING UP YOUR MACHINE (for Linux/Ubuntu)
### You need to install:
- Latest Java JDK http://www.oracle.com/technetwork/java/javase/downloads/index.html
- Android Studio or SDK https://developer.android.com/studio/index.html
- NodeJS (+npm) https://nodejs.org/en/
- Appium http://appium.io
- Python (+some libs) https://www.python.org/
- Android Emulator or Genymotion https://www.genymotion.com/

Make sure you have python installed. (Pre-installed on Macs)
Check Python version is atleast 2.7
```sh
$ python --version\
```
python can be installed on linux using
```sh
$ sudo add-apt-repository ppa:fkrull/deadsnakes
$ sudo apt-get update
$ sudo apt-get install python2.7
```
Check if 'pip' module is installed.
```sh
$ pip
```
Install pip if not installed
```sh
$ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py > get-pip.py
$ sudo python get-pip.py
$ rm get-pip.py
```
Install Python 'selenium' module
```sh
$ sudo pip install selenium
```
Verify that selenium is installed
```sh
$ pip freeze | grep selenium
```
Install additional Nodejs libs
```sh
$ sudo pip install nose_parameterized
$ sudo pip install nose
```
# RUNNING THE TEST
- Run Appium
```sh
$ appium
```
- Connect android phone to pc or run any Emulator
- Run command
```sh
$ adb devices
```
- Get your Android device name
```sh
ivanello@t430u:~/project/appium calc$ adb devices
List of devices attached
**73ffacfe**	device
**emulator-5554**	device
```
- And put it to script _desired_caps['deviceName']_
- Check and change _desired_caps['platformVersion']_
- Run the script
```sh
$ python calc.py
or
$ nosetests -v calc.py
```