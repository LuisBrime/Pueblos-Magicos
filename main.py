import json
import requests


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

    #### Sacar los pueblos de pueblos.txt ####
    file = open('lib/pueblos.txt', 'r')
    o1 = file.readline()
    d1 = file.readline()
    o2 = file.readline()
    d2 = file.readline()
    o3 = file.readline()
    d3 = file.readline()
    o4 = file.readline()
    d4 = file.readline()
    o5 = file.readline()
    d5 = file.readline()
    file.close()

    #### Armar las payloads para la API ####
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
    payload4 = {
        'origins': o4,
        'destinations': d4,
        'key': key,
        'mode': 'driving'
    }
    payload5 = {
        'origins': o5,
        'destinations': d5,
        'key': key,
        'mode': 'driving'
    }

    #### Obtener las distancias de Distance Matrix API ###
    r1 = sendpayload(url, payload1)
    r2 = sendpayload(url, payload2)
    r3 = sendpayload(url, payload3)
    r4 = sendpayload(url, payload4)
    r5 = sendpayload(url, payload5)



