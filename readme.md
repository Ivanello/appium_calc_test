# SETTING UP YOUR MACHINE (for Linux/Ubuntu)
### At least You need to install:
- Latest Java JDK http://www.oracle.com/technetwork/java/javase/downloads/index.html
- Android Studio or SDK https://developer.android.com/studio/index.html
- NodeJS (+npm) https://nodejs.org/en/
- Appium http://appium.io
- Python (+some libs) https://www.python.org/
- Android Emulator or Genymotion https://www.genymotion.com/

### Setup Python
Make sure you have python installed. (Pre-installed on Macs and Ubuntu)
Check Python version is atleast 2.7

    $ python --version\

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

Install additional Nodejs libs

    $ sudo pip install nose_parameterized
    $ sudo pip install nose

### Install NodeJS/Appium/JDK/Android SDK
[Install nodejs/npm](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager):

	$ sudo apt-get update
	$ sudo apt-get install -y python-software-properties python g++ make
	$ sudo add-apt-repository ppa:chris-lea/node.js
	$ sudo apt-get update
	$ sudo apt-get install nodejs

**[Install grunt-cli](http://gruntjs.com/getting-started):**

	$ npm install -g grunt-cli

If you run into an issue about it not being able to install in a directory, do [this](http://stackoverflow.com/a/21712034).

**[Install Appium](http://appium.io/getting-started.html#quick-start):**

	$ npm install -g appium

Set up a symlink in your `.bashrc` file for Appium:

	$ ln -s /path/to/appium.js /usr/bin/appium

Test to make sure it can run by running `appium` in your terminal. The output should be something like:

	info: Welcome to Appium v0.16.0 (REV 292d265edd9c7aaf96f165009285c814b218363d)
	info: Appium REST http interface listener started on 0.0.0.0:4723
	   info  - socket.io started

**[Install Java JRE 6](http://askubuntu.com/questions/48468/how-do-i-install-java)**

	$ sudo apt-get install openjdk-6-jre

**[Install Android SDK](https://developer.android.com/sdk/installing/index.html):**

Download the [SDK](https://developer.android.com/sdk/installing/index.html) and extract it to your home folder.

Launch the Android SDK Manager:

	$ ~/path/to/android-sdk/tools/android

Install the packages that you'll need in the new window:

* Android 4.X
* Android Support Library
* Android SUpport Repository
* Google Play services
* Everything under Tools
* Everything under Extras

You can also create a symlink for the Android SDK Manager by doing:

    $ ln -s /path/to/android-sdk/tools/android /usr/bin/android

### Install Genymotion
First install virtualbox

    $ sudo apt-get install virtualbox

Click below to register on Genymotion site and download either 32bit or 64bit version depending on your hardware architecture

[Register](https://cloud.genymotion.com/page/customer/login/)

Change directory to where you downloaded the bin file and run following commands. Accept the default install path

    $ chmod +x genymotion-2.2.2_x64.bin
    $ ./genymotion-2.2.2_x64.bin

Change directory to where genymotion was installed. The default is _/home/[username]/genymotion/_

    $ cd /home/[username]/genymotion/
    $ ./genymotion

* Click Yes to add your first virtual device
* Click Connect to login and install a device
* Select desired device and click Next
* Enter a name for your device and click Next
* Wait until your virtual device is downloaded and deployed
* Click Finish
* Click Play to start the emulator

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
73ffacfe	device
emulator-5554	device
```
- And put it to script _desired_caps['deviceName']_
- Check and change _desired_caps['platformVersion']_
- Run the script
```sh
$ python calc.py
or
$ nosetests -v calc.py
```

# Output example

* `ok` - test passed
* `FAIL` - test assertion error
* `ERROR` - apk crashed

```
ivanello@t430u:~/project/appium_calc_test$ python calc.py
test_1_arguments_check_0_positive (__main__.TestCalc) ... ok
test_1_arguments_check_1_negative (__main__.TestCalc) ... FAIL
test_1_arguments_check_2_fraction (__main__.TestCalc) ... FAIL
test_1_arguments_check_3_long_number (__main__.TestCalc) ... ok
test_1a_arguments_negativ_0_chars (__main__.TestCalc) ... ok
test_1a_arguments_negativ_1_symbol (__main__.TestCalc) ... FAIL
test_2_sub_operations_0_num_num_sub (__main__.TestCalc) ... ok
test_2_sub_operations_1_nul_num_sub (__main__.TestCalc) ... ERROR
test_2_sub_operations_2_num_nul_sub (__main__.TestCalc) ... ERROR
test_2_sub_operations_3_nul_nul_sub (__main__.TestCalc) ... ERROR
test_3_div_operations_0_num_num_div (__main__.TestCalc) ... ok
test_3_div_operations_1_nul_num_div (__main__.TestCalc) ... ERROR
test_3_div_operations_2_num_nul_div (__main__.TestCalc) ... ERROR
test_3_div_operations_3_nul_nul_div (__main__.TestCalc) ... ERROR
test_3_div_operations_4_num_0_div (__main__.TestCalc) ... ERROR
test_4_subtraction_0_positive_result (__main__.TestCalc) ... ok
test_4_subtraction_1_negative_result (__main__.TestCalc) ... ok
test_4_subtraction_2_fraction_result (__main__.TestCalc) ... FAIL
test_4_subtraction_3_subtract_nill (__main__.TestCalc) ... ok
test_4_subtraction_4_subtract_from_nill (__main__.TestCalc) ... ok
test_4_subtraction_5_sub_from_negativ_number (__main__.TestCalc) ... FAIL
test_4_subtraction_6_subtract_negative_number (__main__.TestCalc) ... FAIL
test_5_division_0_positive (__main__.TestCalc) ... ok
test_5_division_1_2_digits (__main__.TestCalc) ... ok
test_5_division_2_3_digits (__main__.TestCalc) ... ok
test_5_division_3_fraction_result (__main__.TestCalc) ... FAIL
test_5_division_4_fraction_argument1 (__main__.TestCalc) ... FAIL
test_5_division_5_negative_argument1 (__main__.TestCalc) ... FAIL
test_5_division_6_20_dig_numbers (__main__.TestCalc) ... ERROR
test_6_rotation (__main__.TestCalc) ... FAIL

======================================================================
Ran 30 tests in 650.506s

FAILED (failures=10, errors=8)
```