pyclock
=======

Clock app in python / pygame, originally developed for the Raspberry Pi

![Screen1](http://rtigger.com/images/posts/pi-1.jpg)
![Screen2](http://rtigger.com/images/posts/pi-2.jpg)

I had a raspberry pi sitting around my house, as I'm sure many do, and I thought to myself 
"Boy I sure could use a $100 desk clock!"  So I went on ebay and bought a 7" touchscreen LCD that accepts 
HDMI input, setup AdaFruit's WebIDE on my raspberry pi, and started hacking.

I'm using the sample code from adafruit's pygame tutorial to open a pygame screen instance, 
and flickr's API to download a random public image every 30 seconds or so.  

When the images are downloaded from Flickr, we put them through a scaling method to ensure they'll fill 
the entire display.  They're then placed on a queue to be displayed next.

Once the app gets a new image in the queue, there's a one second(ish) fade transition to the next image.

If you didn't notice, it's designed after Windows 8's lock screen, using the same Segoe UI font and everything.

I tried to be all multithready so that the downloading and processing of each image doesn't block the main 
drawing thread and introduce slowdown.

This is my first actual attempt at Python, so be nice :P

## Classes

clock.py - the "main" class, handles redrawing of the screen
img.py - DTO that wraps an image downloaded from Flickr
imgthread.py - the process for downloading and resizing an image, run on a different thread
segoeui.ttf - font used to display date and time

## Future Enhancements
- Notification icons (again, like Windows 8) to indicate if you have unread mail / tweets / other notifications.
- More of a "slide-up-tile" transition
- Improve performance (right now the fade transition is a bit choppy)
