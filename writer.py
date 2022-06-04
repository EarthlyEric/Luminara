import json

nodes = {'Public EU Main 01': {'host': 'lava.link',
                          'port': 80,
                          'password': 'anything as a password',
                          'identifier': 'Public EU Main 01',
                          'region': 'eu_west'
                             },
        'Private Asia Main 01': {'host': 'lavalink.oops.wtf:2000',
                          'port': 2000,
                          'password': 'www.freelavalink.ga',
                          'identifier': 'Public Asia Main 01',
                          'region': 'singapore'
                             },
         'Private US Main 01': {'host': 'lavalink.darrenofficial.com',
                          'port': 80,
                          'password': 'anything as a password',
                          'identifier': 'Public US Main 01',
                          'region': 'us_east'
                             },
                }

tf = open("nodes.json", "w")

json.dump(nodes,tf)
tf.close()

tf = open("nodes.json", "r")
new_dict = json.load(tf)
print(new_dict)