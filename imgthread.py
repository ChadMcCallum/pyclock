import threading
import pygame
import urllib, urllib2
import xml.etree.ElementTree as ET
import img as img
import os
import time

class imgthread(threading.Thread):
    queue = None

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    
    def run(self):
        while 1:
            api_key = 'GetYourOwnKey!'
            url = "http://api.flickr.com/services/rest/?method=flickr.photos.getRecent&per_page=10&api_key=" + api_key
            result = urllib2.urlopen(url)
            tree = ET.fromstring(result.read())
            img = tree.findall("./photos/photo[@secret]")[0]
            #imageURL = "http://farm%s.staticflickr.com/%s/%s_%s_o.%s" % (img.get('farm'), img.get('server'), img.get('id'), img.get('originalsecret'), img.get('originalformat'))
            imageURL = "http://farm%s.staticflickr.com/%s/%s_%s_b.jpg" % (img.get('farm'), img.get('server'), img.get('id'), img.get('secret'))
            urllib.urlretrieve(imageURL, 'temp.jpg')
            self.resize_img('temp.jpg')
            time.sleep(30)

    def resize_img(self, filename):
        surface = pygame.image.load(filename).convert()
        orig_width = float(surface.get_width())
        orig_height = float(surface.get_height())
        #figure out scale
        scale_width = 1 + ((1280 - orig_width) / orig_width)
        scale_height = 1 + ((720 - orig_height) / orig_height)
        offset_x = 0
        offset_y = 0
        if(scale_height > scale_width):
            surface = pygame.transform.scale(surface, (int(orig_width * scale_height), int(orig_height * scale_height)))
            offset_x = int(((orig_width * scale_height) - 1280) / 2)
        else:
            surface = pygame.transform.scale(surface, (int(orig_width * scale_width), int(orig_height * scale_width)))
            offset_y = int(((orig_height * scale_width) - 720) / 2)
        i = img.img(offset_x, offset_y, surface)
        self.queue.put(i)
