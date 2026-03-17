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

# Android API settings
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools = 33.0.2

# Enable AndroidX
android.enable_androidx = True

# Entry point
entrypoint = main.py

# Splash color
presplash.color = #FFFFFF
