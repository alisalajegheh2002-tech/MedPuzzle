[app]

title = MedPuzzle
package.name = medpuzzle
package.domain = ir.heytoweb

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,mp3,wav,ogg,json,db

version = 1.0.0

requirements = python3,kivy,arabic-reshaper,python-bidi

orientation = portrait
fullscreen = 0

# Android
android.minapi = 28
android.api = 35
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

android.permissions = VIBRATE,POST_NOTIFICATIONS

# Build
p4a.bootstrap = sdl2

[buildozer]

log_level = 2
warn_on_root = 1
