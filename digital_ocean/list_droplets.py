import digitalocean
import os

manager = digitalocean.Manager(token=os.getenv('DO_TOKEN'))
droplets = manager.get_all_droplets()


# list out contents for each droplet
for droplet in droplets:
    print("{0}  {1}".format(droplet.ip_address, droplet.name))
