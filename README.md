[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)

## Creating Mobile Automation Testing Framework for IOS and Android Using Appium with Python


### Table of Contents:<br/>


### Main Objectives:<br/>
- Creating Mobile Automation Testing Framework for IOS and Android<br/>
- Build fast and readable automation using minimal code<br/>
- Showcase with effective way to identify app elements<br/>
- [Page Objects](https://github.com/SeleniumHQ/selenium/wiki/PageObjects) and [Element Objects](https://www.tutorialspoint.com/dom/dom_element_object) implementation<br/>
- Industry-ready test structure<br/>
- Ability to pass arguments from CLI (see [get_args_from_cli](https://github.com/ikostan/TEST_AUTOMATION_FRAMEWORK_USING_APPIUM_WITH_PYTHON/blob/master/utils/get_args_from_cli.py) file)
- Build readable test report using Allure Framework<br/>
- Test code should avoid violating principles like [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself), [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it), [SRP](https://en.wikipedia.org/wiki/Single_responsibility_principle) and [KISS](https://en.wikipedia.org/wiki/KISS_principle).
- Using built-in apps in order to accomplish all the above<br/>


### Documentation:
- [Appium API Documentation](http://appium.io/docs/en/about-appium/api/)<br/>
- [Appium Desktop](https://github.com/appium/appium-desktop)<br/>
- [Appium Python Client](https://github.com/appium/python-client)<br/>
- [Android Debug Bridge (adb)](https://developer.android.com/studio/command-line/adb)<br/>
- [Appium Desired Capabilities](http://appium.io/docs/en/writing-running-appium/caps/)<br/>
- [Appium Android Driver](https://github.com/appium/appium-android-driver)<br/>


**Additional Resources:**<br/>

- [Selenium Documentation](https://seleniumhq.github.io/selenium/docs/api/py/api.html)<br/>
- [Full Pytest documentation](http://doc.pytest.org/en/latest/contents.html)<br/>
- ['Selenium with Python' official documentation webpage](https://selenium-python.readthedocs.io)<br/>
- [PyCharm - Manage dependencies using requirements.txt](https://www.jetbrains.com/help/pycharm/managing-dependencies.html)<br/>
- [Allure Framework](https://docs.qameta.io/allure/)<br/>
- [CREATING A TEST AUTOMATION FRAMEWORK USING APPIUM WITH PYTHON](https://qaboy.com/2018/06/27/automation-framework-using-appium-python/)<br/>
- [How to Setup ADB/Fastboot on Windows](https://theunlockr.com/how-to-set-up-adb-usb-drivers-for-android-devices/)<br/>


### Dev Environment:<br/>
<a id="dev"></a>

- [Python 3.7.4](https://www.python.org/downloads/release/python-374/)<br/>
- [Appium](http://appium.io/)<br/>
- [Appium-Python-Client 0.47](https://pypi.org/project/Appium-Python-Client/)<br/>
- [PyTest 5.1.1](https://pypi.org/project/pytest/)<br/>
- [Allure Framework 2.12.1](http://allure.qatools.ru/)<br/>
- [Win 10 (64 bit)](https://www.microsoft.com/en-ca/software-download/windows10)<br/>
- [PyCharm 2019.2 (Community Edition)](https://www.jetbrains.com/pycharm/download/#section=windows)<br/>
- [GitHub Desktop 2.1.2](https://desktop.github.com/)<br/>
- [GIT 2.22.0.windows.1](https://git-scm.com/download/win)<br/>
- [Java SE Development Kit 8 Update 221 (64-bit)](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)<br/>
- [Node.js v10.6.3](https://nodejs.org/en/download/current/)<br/>
- [Appium Server GUI client v1.13.0](http://appium.io/)<br/>
- [nmp v6.9.0](https://nodejs.org/en/download/)<br/>
- [Maven 3.6.1](https://maven.apache.org/download.cgi)<br/>
- [Scoop](https://scoop.sh/)<br/>
- Android tablet (real device with Android v7.0)<br/>
- [Android Studio 3.5](https://developer.android.com/studio/?gclid=CjwKCAjw44jrBRAHEiwAZ9igKJZ4_eky4PfdbRM1P_T2XejHOYyRH1GIdTyLyAWmEUULF3Dmv6zi7xoCaOwQAvD_BwE)<br/>


### Python Packages:<br/>
Full list of dependencies see [here.](https://github.com/ikostan/TEST_AUTOMATION_FRAMEWORK_USING_APPIUM_WITH_PYTHON/blob/master/requirements.txt)


### Nice to have tools:
1. [Fiddler: The free web debugging proxy](https://www.telerik.com/fiddler)<br/>
2. [Kite: Code Faster in Python](https://kite.com/)<br/>
3. [Ragnorex: Smart Selector Generator](https://www.ranorex.com/selocity/browser-extension)<br/>
4. [Pynsource: Python source code into UML diagrams](https://www.pynsource.com/index.html)<br/>
5. [TeamViewer](https://www.teamviewer.com/en/?pcc_keyword=teamviewer&gclid=CjwKCAjw44jrBRAHEiwAZ9igKBBMHbZjxT2zAPCJFrK-Agcldw0iOKD_1TyEeKcbCN_uTZjvCnQaNxoCfuwQAvD_BwE)<br/>
6. [AirDroid](https://www.airdroid.com/)<br/>
7. [QuickSupport](https://play.google.com/store/apps/details?id=com.teamviewer.quicksupport.market&hl=en_CA)<br/>
8. [App Info, Application Info](https://play.google.com/store/apps/details?id=com.bestappfactory.appinfo&hl=en_CA)<br/>


### Tech Issues and Problem Solving:<br/>
<a id="tech_issues"></a>

<details>
  <summary><b>Changing the project interpreter in the PyCharm project settings</b></summary>

<br/>1. In the **Settings/Preferences dialog** (Ctrl+Alt+S), select **Project <project name> | Project Interpreter**.<br/>
2. Expand the list of the available interpreters and click the **Show All** link.<br/>
3. Select the target interpreter. When PyCharm stops supporting any of the outdated Python versions, the corresponding project interpreter is marked as unsupported.<br/>
4. The Python interpreter name specified in the **Name** field, becomes visible in the list of available interpreters. Click **OK** to apply the changes.<br/>

For more info please check [here](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html)<br/>

</details>


<details>
  <summary><b>PyCharm - Choosing Your Testing Framework</b></summary>
 
<br/>1. Open the Settings/Preferences dialog, and under the node Tools, click the page **Python Integrated Tools**.<br/>
2. On this page, click the **Default Test Runner** field.<br/>
3. Choose the desired test runner:<br/>

<br/>   
<div align="center"> 
<img width="60%" height="60%" src="https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/blob/master/testing_selenium_capabilities/img/py_choosing_test_runner.png" hspace="20">
</div>
<br/>

For more info please see [Enable Pytest for you project](https://www.jetbrains.com/help/pycharm/pytest.html)
</details>


<details>
  <summary><b>Setting up Python3 virtual environment on Windows machine</b></summary>
<br/>

1. open CMD<br/>
2. navigate to project directory, for example:<br/> 

```bash
cd C:\Users\superadmin\Desktop\Python\CodinGame
```

3. run following command:<br/> 

```bash 
pip install virtualenv
```

4. run following command:<br/> 

```bash 
virtualenv venv --python=python
```
    
</details>


<details>
  
  <summary><b>Activate Virtual Environment</b></summary>

  <br/>
  In a newly created virtualenv there will be a bin/activate shell script. For Windows systems, activation scripts are provided for CMD.exe and Powershell.
  <br/><br/>

  1. Open Terminal<br/>
  2. Run: \path\to\env\Scripts\activate 
  
  <br/>Source: https://pypi.org/project/virtualenv/1.8.2/
  
</details>


<details>
  <summary><b>Auto generate requirements.txt</b></summary>

<br/>Any application typically has a set of dependencies that are required for that application to work. The requirements file is a way to specify and install specific set of package dependencies at once.<br/>
Use pip’s freeze command to generate a requirements.txt file for your project:<br/>

   ```python
    pip freeze > requirements.txt
```

If you save this in requirements.txt, you can follow this guide: [PyCharm - Manage dependencies using requirements.txt](https://www.jetbrains.com/help/pycharm/managing-dependencies.html), or you can:<br/>
   
   ```python
    pip install -r requirements.txt
```   
Source: https://www.idiotinside.com/2015/05/10/python-auto-generate-requirements-txt/<br/>
</details>


<details>
  
  <summary><b>JAVA_HOME PATH</b></summary>

   <br/>A. In order to configure JAVA_HOME path do the following:</b><br/>
   1. Go to "Advanced System Settings" > Advanced Tab > Environment Variables<br/>
   2. Go to System Variables section > click on New... button<br/>
   3. Type Variable name: JAVA_HOME<br/>
   4. Enter Variable Value: C:\Program Files\Java\jdk1.8.0_221<br/>
   5. Press OK button<br/><br/>
  
  <div align="center"> 
  <img width="90%" height="90%" src="https://github.com/ikostan/AppiumTesting/blob/master/img/java_home.jpg" hspace="10">
  </div>
  
  <b>B. Edit environment variable:</b><br/>
  1. From System variables list select path > Press Edit... button<br/>
  2. Press on New button > type: %JAVA_HOME%\bin<br/>
  3. Press OK button<br/>
  
  <div align="center"> 
  <img width="90%" height="90%" src="https://github.com/ikostan/AppiumTesting/blob/master/img/java_home_2.jpg" hspace="10">
  </div>
  
</details>


<details>
  
  <summary><b>Maven PATH</b></summary>
  <br/>
  <b>A. In order to configure MVN_HOME path do the following:</b><br/>
  1. Go to "Advanced System Settings" > Advanced Tab > Environment Variables<br/>
  2. Go to System Variables section > click on New... button<br/>
  3. Type Variable name: MVN_HOME<br/>
  4. Enter Variable Value: C:\Users\username\AppData\Local\Android\Sdk<br/>
  5. Press OK button<br/><br/>
  <div align="center"> 
  <img width="90%" height="90%" src="https://github.com/ikostan/AppiumTesting/blob/master/img/maven_home.jpg" hspace="10">
  </div>
  
  <b>B. Edit environment variable:</b><br/>
  1. From System variables list select path > Press Edit... button<br/>
  2. Press on New button > type: %MVN_HOME%\bin<br/>
  3. Press OK button<br/>
  
  <div align="center"> 
  <img width="90%" height="90%" src="https://github.com/ikostan/AppiumTesting/blob/master/img/maven_home_2.jpg" hspace="10">
  </div>
  
  <b>C. Test:</b>
  1. Open CMD > run "mvn --version"<br/>
  2. If everifyng is configured properly you will something like this:<br/>
  
  <div align="center"> 
  <img width="50%" height="50%" src="https://github.com/ikostan/AppiumTesting/blob/master/img/maven_cmd.JPG" hspace="10">
  </div>
  
</details>


<details>
  
  <summary><b>Inspect devices with Chrome Developer</b></summary>
  <br/>
  1. Open Chrome web browser > new tab<br/>
  2. Paste following address: chrome:..inspect/#devices<br/>
  
  <br/>If evryfing connected properly you will see something like this:<br>
  <div align="center"> 
  <img width="90%" height="90%" src="https://github.com/ikostan/AppiumTesting/blob/master/img/inspect_devices.JPG" hspace="10">
  </div>
  
  Source: 
</details>


<details>
  
  <summary><b>Environment variables for Android ADB (ANDROID_HOME PATH)</b></summary>
   <br/>
<b>A. In order to configure ANDROID_HOME path do the following:</b><br/>
  1. Go to "Advanced System Settings" > Advanced Tab > Environment Variables<br/>
  2. Go to System Variables section > click on New... button<br/>
  3. Type Variable name: ANDROID_HOME<br/>
  4. Enter Variable Value: C:\Users\username\AppData\Local\Android\Sdk<br/>
  5. Press OK button<br/><br/>
  <div align="center"> 
  <img width="90%" height="90%" src="https://github.com/ikostan/AppiumTesting/blob/master/img/android_home.JPG" hspace="10">
  </div>
  
  <b>B. Edit environment variable:</b><br/>
  1. From System variables list select path > Press Edit... button<br/>
  2. Press on New button > type: %ANDROID_HOME%\tools<br/>
  3. Press OK button<br/>
  4. Press on New button > type: %ANDROID_HOME%\platform-tools<br/>
  5. Press OK button<br/>
  
  <div align="center"> 
  <img width="90%" height="90%" src="https://github.com/ikostan/AppiumTesting/blob/master/img/android_home_2.JPG" hspace="10">
  </div>
  
  <b>C. Test:</b>
  1. Open CMD > run "adb devices"<br/>
  2. If everifyng is configured properly you will something like this:<br/>
  
  <div align="center"> 
  <img width="50%" height="50%" src="https://github.com/ikostan/AppiumTesting/blob/master/img/adb_devices.JPG" hspace="10">
  </div>
  
</details>


<details>
  <summary><b>Connect to a device over Wi-Fi using Android Debug Bridge (adb)</b></summary>
  
  <br/>
  
  **adb** is included in the Android SDK Platform-Tools package. You can download this package with the [SDK Manager](https://developer.android.com/studio/intro/update.html#sdk-manager), which installs it at android_sdk/platform-tools/. Or if you want the standalone Android SDK Platform-Tools package, you can download it [here](https://developer.android.com/studio/releases/platform-tools.html).<br/>
    
   **Run Appium Tests On Real Android Device over Wifi:**<br/>
    
   1. Connect your device to computer via USB and check if it is connected using **‘adb devices’** which will list you the devices connected to your machine.<br/>
   2. We should make sure that android device and the Laptop are connected to the same Wifi network. In my case wifi is on for laptop and mobile device and not need to purchase any wireless wifi adapter.<br/>
   3. Restart adb and make it work over tcpip by specifying the port value (***adb tcpip 5555*). If no port number is specified, Port 5555 is used by default. This step will make your adb daemon to re-start on the specified port.
   4. We need to get the IP address of the the device. There are two ways to get IP address of your device by using below options:<br/>
       - Your device -> Settings -> Wifi -> Wifi Settings<br/>
       - adb shell ip -f inet addr show wlan0<br/>
   5. Run the below command to connect adb to your device over Wi-Fi using IP address of your device:<br/>
       - adb connect ip_address:tcpip_port<br/>
   6. Confirm that your host computer is connected to the target device:<br/>
       - adb devices<br/>
   
   Source: https://developer.android.com/studio/command-line/adb<br/>
   Source: https://rajeevkumarweb.wordpress.com/2017/06/03/run-appium-tests-on-real-android-device-over-wifi/<br/>

</details>


<details>
  <summary><b>Discover current Activity name with dumpsys</b></summary>
   <br/>
   
   **dumpsys** is a shell command. You can run it from the command line as follows:<br/>
        - adb shell dumpsys window windows | grep -E 'mCurrentFocus | mFocusedApp'<br/>
    
   If you have multiple devices connected, first get their IDs by executing:<br/>
        - adb devices<br/>
        
   Then, replace <your-device-id> with the relevant device ID:<br/>
        - adb -s <your-device-id> shell dumpsys window windows | grep -E 'mCurrentFocus | mFocusedApp'<br/>
   
   <br/> You should see something like that:
   <div align="center"> 
   <img width="60%" height="60%" src="https://github.com/ikostan/AppiumTesting/blob/master/img/adb_shell.JPG" hspace="10">
   </div>
   
   Source: https://developer.android.com/studio/command-line/dumpsys<br/>
   Source: https://stackoverflow.com/questions/43178672/dumpsys-window-windows-grep-e-mcurrentfocusmfocusedapp-command-is-not-retu/46545726#46545726<br/>
</details>


<details>
  <summary><b>Common Selenium errors</b></summary>

<br/>- **[How to fix common Selenium errors?](https://www.ultimateqa.com/common-selenium-webdriver-errors-fix/)**<br/>

</details>


<details>
  
  <summary><b>error: RPC failed; curl 56 Recv failure: Connection was reset</b></summary>
  <br/>
  1. Open Git Bash<br/>
  2. Run: "git config --global http.postBuffer 157286400" 
  
  <br/>Source: https://stackoverflow.com/questions/36940425/gitlab-push-failed-error
  
</details>


<details>
  <summary><b>How to fix in case .gitignore is ignored by Git</b></summary>

<br/>Even if you haven't tracked the files so far, Git seems to be able to "know" about them even after you add them to .gitignore.<br/> 

**NOTE:**<br/>
    - First commit your current changes, or you will lose them.<br/> 
    - Then run the following commands from the top folder of your Git repository:<br/> 
    
   ```bash 
    git rm -r --cached .
    git add .
    git commit -m "fixed untracked files"
   ```
    
</details>
