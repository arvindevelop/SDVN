from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.link import TCLink

def create_sdvn_topology():
    net = Mininet(controller=Controller, switch=OVSSwitch, link=TCLink)

    # Add controller
    c0 = net.addController('c0')

    # Add switches
    s1 = net.addSwitch('s1')

    # Add hosts
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')

    # Add links
    net.addLink(h1, s1)
    net.addLink(h2, s1)

    return net

if __name__ == '__main__':
    sdvn_net = create_sdvn_topology()
    sdvn_net.start()
    sdvn_net.pingAll()
    sdvn_net.stop()

