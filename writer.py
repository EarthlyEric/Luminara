import json

nodes = {'Public EU Main 01': {'host': 'lava.link',
                          'port': 80,
                          'rest_uri': 'http://lava.link:80',
                          'password': 'anything as a password',
                          'identifier': 'Public EU Main 01',
                          'region': 'europe'
                             },
        'Private EU Main 01': {'host': 'uk02.scarcehost.uk',
                          'port': 3073,
                          'rest_uri': 'http://uk02.scarcehost.uk:3073',
                          'password': 'Minecraft940911/@@@',
                          'identifier': 'Private EU Main 01',
                          'region': 'europe'
                             }
                }

tf = open("nodes.json", "w")

json.dump(nodes,tf)
tf.close()

tf = open("nodes.json", "r")
new_dict = json.load(tf)
print(new_dict)