from pydactyl import PterodactylClient

api = PterodactylClient('https://panel.scarcehost.uk', 'NODgc4jyM5GsJvr3YWcLXBWzfZHfMjM9VdAO9uPJvGCPlhWF')

# Get a list of all servers the user has access to
my_servers = api.client.servers.get_server(server_id="33cf4871")
print(my_servers)