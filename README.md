# Turning-Projector-ON-OFF-and-Switching-images-with-Capacitive-Sensor-and-Raspberry-Pi
Using projector Panasonic PT-JW130 connected via HDMI to Raspberry Pi and using a cheap capacitive touch board based on chip TTP223 to turn Projector on and off and switch between some images projected


Hardware:

- Raspberry Pi 3B
- Panasonic PT-JW130 Projector
- TTP223 Capacitive Touch Sensor Butt

Connectivity:

- Raspberry Pi connected to the projector with HDMI cable
- Raspberry Pi connected to WLAN (Wifi) of local area network
- Projector connected via ethernet cable to the LAN of the loacal area network

THE PROJECTOR MUST SUPPORT COMMANDS THROUGHT THE PJLINK PROTOCOL TO WORK AS THESE COMMANDS ARE USED TO SWITCHED IT ON AND OFF
THE PROJECTOR MUST HAVE LAN CONNECTIVITY

Settings:
- set Raspberry Pi IP as static
- set the IP of the projector in your network
- check the manual to find the password of your projector, for Panasonic PT-JW130FBU model the password is "panasonic"

Personalization:
- customize the images you want to project
- customize the time between needed to turn the projector ON/OFF

Important libraries used in this project:
- cv2     library used for loading and having setting the images full screen
- pypjlink    library used for managing the PJlink commands to turn projector on and off remotely
