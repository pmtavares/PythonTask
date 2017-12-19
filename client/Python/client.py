#Base Python client for MEng in IoT Assignment
#consumes data from IoT Gateway
from urllib.request import urlopen
import requests
from html.parser import HTMLParser
import numpy as np
import matplotlib.pyplot as plt

## Pedro Tavares - B00100855
url = "http://localhost:8080/"
response = requests.get(url)
print("Response code is: " + str(response))
print("DATA from url is:")
print(response.text)

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0 
        self.time = []
        self.temperature = []
       
    def handle_endtag(self, tag):
        if tag == 'temperature':
            self.recording -=1            
        if tag == 'time':
            self.recording =1
            
            
    def handle_data(self, data):
        if self.recording:
            self.temperature.append(data)
        else:
            if data != '\n':
                self.time.append(data)

parser = MyHTMLParser()
parser.feed(response.text)

plt.plot(parser.time, parser.temperature,'ro' )
plt.ylabel('Temperature')
plt.xlabel('Time')
line, = plt.plot(parser.time, parser.temperature, '-')
line.set_antialiased(False) 
plt.show()




