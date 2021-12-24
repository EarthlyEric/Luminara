import json

nodes = {'Public EU Main 01': {'host': 'lava.link',
                          'port': 80,
                          'rest_uri': 'http://lava.link:80',
                          'password': 'anything as a password',
                          'identifier': 'Public EU Main 01',
                          'region': 'europe'
                             },
        'Public EU Main 02': {'host': 'lavalink.pumpdev.org',
                          'port': 3876,
                          'rest_uri': 'http://lavalink.pumpdev.or:3876',
                          'password': 'pumpisfree',
                          'identifier': 'Public EU Main 02',
                          'region': 'europe'
                             }
                }

tf = open("nodes.json", "w")

json.dump(nodes,tf)
tf.close()

tf = open("nodes.json", "r")
new_dict = json.load(tf)
print(new_dict)