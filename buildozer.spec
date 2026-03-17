
[app]

title = Tic Tac Toe
package.name = tictactoe
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,wav

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

# Permissions
android.permissions = INTERNET

# Target Android API
android.api = 31

# Minimum API your APK supports
android.minapi = 21

# Android SDK version
android.sdk = 20

# Android NDK version
android.ndk = 23b

# Android build tools version
android.build_tools = 30.0.3

# Use AndroidX
android.enable_androidx = True

# Application entry point
entrypoint = main.py

# Splash screen color
presplash.color = #FFFFFF
