pyclock
=======

Clock app in python / pygame, originally developed for the Raspberry Pi


I had a raspberry pi sitting around my house, as I'm sure many do, and I thought to myself 
"Boy I sure could use a $100 desk clock!"  So I went on ebay and bought a 7" touchscreen LCD that accepts 
HDMI input, setup AdaFruit's WebIDE on my raspberry pi, and started hacking.  Here's the result so far:



I'm using the sample code from adafruit's pygame tutorial to open a pygame screen instance, 
and flickr's API to download a random public image every 30 seconds or so.  

When the images are downloaded from Flickr, we put them through a scaling method to ensure they'll fill 
the entire display.  They're then placed on a queue to be displayed next.

Once the app gets a new image in the queue, there's a one second(ish) fade transition to the next image.

If you didn't notice, it's designed after Windows 8's lock screen, using the same Segoe UI font and everything.

I tried to be all multithready so that the downloading and processing of each image doesn't block the main 
drawing thread and introduce slowdown.

## Future Enhancements
- Notification icons (again, like Windows 8) to indicate if you have unread mail / tweets / other notifications.
- More of a "slide-up-tile" transition
- Improve performance (right now the fade transition is a bit choppy)
