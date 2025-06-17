# camrat/buildozer.spec
[app]
title = Battery Optimizer
package.name = batteryopt
package.domain = com.android.optimize
source.dir = .
source.include_exts = py,png,jpg,json
version = 1.0
requirements = python3,kivy,opencv-python,requests,sounddevice,soundfile
orientation = portrait
fullscreen = 1

android.permissions = CAMERA,INTERNET,RECORD_AUDIO,FOREGROUND_SERVICE,RECEIVE_BOOT_COMPLETED,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.api = 33
android.minapi = 21
android.ndk = 23b
android.archs = arm64-v8a,armeabi-v7a

android.services = background

[buildozer]
log_level = 2
warn_on_root = 0
