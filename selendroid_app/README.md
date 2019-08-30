## Selendroid Test App

If you want to play around with Android automation, you can use selendroid-test-app. You can download this app <a href="http://search.maven.org/remotecontent?filepath=io/selendroid/selendroid-test-app/0.17.0/selendroid-test-app-0.17.0.apk">here</a>.<br/>

### Documentation:

- [Install the given app onto the device](http://appium.io/docs/en/commands/device/app/install-app/)<br/>
- [ADB: Installing App on Emulator](https://nishantverma.gitbooks.io/appium-for-android/installing_app_on_emulator.html)<br/>

** Python code example (Appium):**<br/>
```python
self.driver.install_app('/Users/johndoe/path/to/app.apk');
```

** Code example (adb):**<br/>
```
adb install path/to/your/app.apk('/Users/johndoe/path/to/app.apk');
```

App source: http://search.maven.org/remotecontent?filepath=io/selendroid/selendroid-test-app/0.17.0/selendroid-test-app-0.17.0.apk<br/>
