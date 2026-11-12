[app]
title = DroneTacticalGCS
package.name = dronetacticalgcs
package.domain = org.dronegcs
source.include_exts = py,png,jpg,kv,atlas,json
source.main_filename = main.py
requirements = python3,flet
orientation = portrait
version = 0.1
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,USB_PERMISSION
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
