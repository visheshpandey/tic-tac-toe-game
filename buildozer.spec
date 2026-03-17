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

# Minimum Android API
android.minapi = 21

# Enable AndroidX
android.enable_androidx = True

# Entry point
entrypoint = main.py

# Splash screen color
presplash.color = #FFFFFF
