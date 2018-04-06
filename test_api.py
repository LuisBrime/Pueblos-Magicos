import requests
import json

def sendpayload(url, payload):
    r = requests.get(url, params = payload)
    if r.status_code != 200:
        print('HTTP status code {} received, program terminated.'.format(r.status_code))
    else:
        try:
            result = json.loads(r.text)
            print(result)
            return result
        except ValueError:
            print('Error while parsing JSON response, program terminated.')

if __name__ == '__main__':
    key = 'AIzaSyB4JIdwOtl_8OLuw-NMr6EZ-3jz6emfKAc'
    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

    file = open('lib/test.txt', 'r')
    o1 = file.readline()
    d1 = file.readline()
    o2 = file.readline()
    d2 = file.readline()
    o3 = file.readline()
    d3 = file.readline()
    file.close()

    print(len(o1.split('|')))
    print(len(d1.split('|')))
    print()
    print(len(o2.split('|')))
    print(len(d2.split('|')))
    print()
    print(len(o3.split('|')))
    print(len(d3.split('|')))

    payload1 = {
        'origins': o1,
        'destinations': d1,
        'key': key,
        'mode': 'driving'
    }
    payload2 = {
        'origins': o2,
        'destinations': d2,
        'key': key,
        'mode': 'driving'
    }
    payload3 = {
        'origins': o3,
        'destinations': d3,
        'key': key,
        'mode': 'driving'
    }

    r1 = sendpayload(url, payload1)
    r2 = sendpayload(url, payload2)
    r3 = sendpayload(url, payload3)