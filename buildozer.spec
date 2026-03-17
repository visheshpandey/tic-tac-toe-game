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


# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 31

# (int) Minimum API your APK supports
android.minapi = 21

# (str) Android SDK version to use
android.sdk = 20

# (str) Android NDK version
android.ndk = 23b

# (str) Android build tools version
android.build_tools = 30.0.3

# (bool) Use AndroidX
android.enable_androidx = True

# (str) Application entry point
entrypoint = main.py

# (str) Supported orientation
orientation = portrait

# (bool) Show splash screen
presplash.color = #FFFFFF

# (bool) Use fullscreen
fullscreen = 0
