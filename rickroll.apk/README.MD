# How to install
Firstly, you need a Linux based operating system to compile the Python file to an Android Package (apk)

  Update your system
`sudo apt update`

  Install Buildozer from the `requirements.txt` file

  Install the following packages in a Linux system
  `sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev`

  `pip3 install --upgrade Cython==0.29.19` 

  Make sure your main file is named "main.py"

  After you installed all the following packages and waited for AN ETERNITY, wait for another!


  `buildozer init` to install the Android packages :D

  `buildozer -v android debug` to turn the file to an APK!

  AND NOW YOU'RE DONE