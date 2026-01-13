[app]
title = Remote Service
package.name = remotesystem
package.domain = org.biskfw
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3, kivy, kivymd, pyTelegramBotAPI, requests, pillow, plyer
android.permissions = INTERNET, CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, RECORD_AUDIO, ACCESS_FINE_LOCATION, VIBRATE, WAKE_LOCK
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
android.services = monitor:bot_control.py

[buildozer]
log_level = 2
warn_on_root = 1
