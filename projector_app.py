# -*- coding: utf-8 -*-

from gpiozero import Button
from time import sleep
import os
import numpy as np
import cv2
from pypjlink import Projector

# variables
touch = Button(27)  # Gpio assigned to touch sensor
tempo = 0
flag = 0
boold = True     # used for debugging
path = "images"  # folder in which there are the images we want to project
images = []
index_imm = 0  # index of the image we want to project
timeout = 100  # time interval in ms to wait to change image


# functions
def salva_immagine(nome):
    """ Function that saves the images
    """

    img = cv2.imread(nome, 1)  # it reads an image and returns it back as an array

    return img


def cambia_immagine(nome):
    """ Function that visualizes the images
    """

    while True:
        cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)  # it creates a windows in which the full sreen image will be displayed using cv2 library
        cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)   # it adapts the image to the screen maintaining the screen size
        cv2.imshow("window", nome)  # it shows the window with the image
        cv2.waitKey(timeout)  # it waits for timout before receiving next instruction
        break

    return None


# main
if __name__ == "__main__":
    print("Connecting the projector... Please wait...")
    projector = Projector.from_address("192.168.2.59")  # it begins the connection with the projector       YOU HAVE TO FILL IN THE PROJECTOR IP IN YOUR NETWORK HERE

    if not projector.authenticate("panasonic"):  # verify the projector password                            YOU HAVE TO FILL IN THE PROJECTOR PASSWORD HERE
        print("Authentication failed")
    else:
        print("Authentication successful")

    print("Saving images... Please wait...")
    for r, d, f in os.walk(path):  # create the list of images
        continue

    print("Creating images... Please wait...")
    for imm in f:  # select one images one at the time
        images.append(salva_immagine("images/" + imm))  # create the images one at the time

    print("Done! Now you can start to interact with the projector.")
    cambia_immagine(images[index_imm])  # visualize the first imamge
    index_imm += 1
    
    while True:  # infinite loop
        if touch.is_pressed:  # if the button (capacitive touch in this case) is not pressed
            flag = 0  # this flag avoids that the Pi receive more bouncing commands with a simple touch of the sensor
        else:  # if the button is pressed
            if flag == 0:
                if boold:
                    print("Pressed")
                tempo = 0  # set time to 0
                while tempo < 200:  # time to wait between a touch command and the next
                    if boold:
                        print("one second is passed", tempo + 1)
                    tempo += 1  # increase time
                    if touch.is_pressed:  # Botton not pressed
                        if tempo >= 35:  # if time is more than 35 change projector state
                            if boold:
                                projector = Projector.from_address("192.168.2.59")  # reopen LAN communication with projector            YOU HAVE TO FILL IN THE PROJECTOR IP IN YOUR NETWORK HERE

                                if not projector.authenticate("panasonic"):  # reauthentication                                          YOU HAVE TO FILL IN THE PROJECTOR PASSWORD HERE
                                    print("Authentication failed")
                                else:
                                    print("Authentication successful")
                                    if projector.get_power() == "on":  # check if projector is on
                                        print("Turning projector off... ")
                                        try:  # Avoid that the user tries to turn the projector off while it is already turning off
                                            projector.set_power("off")  # if projector is on than it is turned off
                                        except Exception:
                                            print("The projector is still turining off... ")
                                    else:
                                        print("Turning projector on...")
                                        try:  # avoid that the user tries to turn the projector on while it is already on
                                            cv2.destroyAllWindows()  # before the projector turns on this command destroys all the windows 
                                            cambia_immagine(images[index_imm])  # it changes the images when the projector turns on
                                            projector.set_power("on")  # if projector is off it turns it on
                                        except Exception:
                                            print("The projector is still turning on... ")
                            flag = 1
                            break
                        if tempo < 35:  # if time is less than 35ms so the "change image script" is started 
                            if boold:
                                print("change image")
                            try:  # it goes back at the beginning of the folder when the last image is reached
                                cambia_immagine(images[index_imm])
                                index_imm += 1
                            except Exception:
                                index_imm = 0
                                cambia_immagine(images[index_imm])
                            flag = 2
                            break
                        tempo = 0  # it sets time to 0
