import json
import requests
import sys

if __name__ == '__main__':
    key = 'AIzaSyB4JIdwOtl_8OLuw-NMr6EZ-3jz6emfKAc'
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

    # Sacar los pueblos de pueblos.txt
    file = open('lib/pueblos.txt', 'r')
    p1 = file.readline(1)
    p2 = file.readline(2)
    p3 = file.readline(3)
    p4 = file.readline(4)
    p5 = file.readline(5)
    file.close()

    m1 = len(p1)//2

    payload1 = {
        'origins': '',
        'destinations': '',
        'key': key,
        'mode': 'driving'
    }

    r = requests.get(url, params)