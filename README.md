# Flask Python Basic Template

This is a starter flask template for building web and hybrid desktop apps with support
for webview in desktop environment and web backend for mobile environment. There is a
build script for desktop `pyinstaller.spec` using pyinstaller and mobile `buildozer.spec`
using the buildozer package.

> This project does not come with any web framework included so you have a fresh project code base with no bloat code. This is intended as a new minimal project template

[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)
![alt text](https://www.python.org/static/community_logos/python-powered-w-100x40.png "Python")

## Pre-Organised Project Structure

The project's project directory is pre organised for flask development so the developers can just focus on their task

## Pre-Optimised Build Script

The build scripts are pre optimised for size and therefore contains a lot of excludes
in the build script. This means you need to check the excludes list to remove the packages
your using for the project.

## Dependencies

This project template contain the required basics such `SQLite` for database, `Flask` as the web framework

## Configure the project

The recommended way is to use a virtual environment and then install the packages
there instead of using system site packages

```shell
    python -m venv packages
```

To activate the virtual environment type the following command

```shell
    ./packages/Scripts/activate (if in windows)
    source /packages/bin/activate (if other platform)
```

To install the project dependies type the following

```shell
    pip install -r requirements.txt
```

To deactive the virtual environment type the following

```shell
    deactivate
```

## Preview the project

To start flask app as a desktop web app type the following command

```shell
    python main.py
```

To start flask app as a localhost server type the following command

in windows `set FLASK_APP=hello.py`
in linux `export FLASK_APP="hello.py"`

```shell
    flask run
```

## Android toolchain dependencies

Test to work in Ubuntu 18.04 (64-Bit)

```shell
    sudo apt update
    sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config \
    zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev
    pip3 install --user --upgrade cython virtualenv
    export PATH=$PATH:~/.local/bin/
```

For buildozer related troubleshooting refer https://buildozer.readthedocs.io/en/latest/installation.html

## Building the project

### Desktop

To build the project in desktop platform (windows, linux, mac, etc), type the following command

```shell
    pyinstaller pyinstaller.spec
```

> There is a lot of excludes in the `pyinstaller.spec` file. Remember to uncomment libraries if your using it

> It is recommended not use UPX for reducing the size of the application as it is known to break the `vcruntime140.dll` used by pyinstaller in windows

### Mobile

> To build applications in mobile platform you need the linux platform because of some tools used by the toolchain not working in windows. If your in windows then use the windows subsystem for linux to get linux terminal in windows

> The first build time will be very long but later on will be cached to make it faster and also there will be a lot to download such as the necessary SDKs, etc

To build the project in mobile platform (android, ios) type the following command

```shell
    buildozer android debug run
```

> If errors occur in the android toolchain it is recommended to clean the project using the command `buildozer android clean`

> If you get build errror then go to `buildozer.spec` file and change `pka.fork` as `kivy` or `pygame` and and also type to change the android branch `pka.branch` as `develop` or `master`. You might need to try these combinations.

## Android Logging

To see the logs of your compiled android app enable `Developer Mode` and enable the `USB Debugging` option inside it. Then open a terminal and type the following command.

> To get the log you need adb (Android Debug Bridge) installed in your system

```shell
    adb -d logcat *:S python:D
```

## Type checking

It's a good practice to use type checking in your project. Python supports type annotations.
The `mypy` package can check if the project contains type issues. Run the following command

> Remember that type annotations is not strictly required. Which means your project will run just fine without it `mypy` will only show warning and error messages

```shell
    mypy .\source\ --ignore-missing-imports --strict
```
