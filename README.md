## Creating a Test Automation Framework Using Appium with Python


### Documentation:
- [Appium API Documentation](http://appium.io/docs/en/about-appium/api/)
- [Appium Desktop](https://github.com/appium/appium-desktop)
- [Appium Python Client](https://github.com/appium/python-client)
- [Android Debug Bridge (adb)](https://developer.android.com/studio/command-line/adb)


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
  <summary><b>Android Debug Bridge (adb)</b></summary>
  
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
       - adb connect <ip address>:<tcpip port><br/>
   6. Finally you got connected to the device over without USB cable as your device is getting listed.<br/>
    
   Source: https://rajeevkumarweb.wordpress.com/2017/06/03/run-appium-tests-on-real-android-device-over-wifi/<br/>

</details>


<details>
  <summary><b>dumpsys</b></summary>

<br/><br/>

</details>


<details>
  <summary><b></b></summary>

<br/><br/>

</details>


Source Tutorials: [CREATING A TEST AUTOMATION FRAMEWORK USING APPIUM WITH PYTHON](https://qaboy.com/2018/06/27/automation-framework-using-appium-python/)

