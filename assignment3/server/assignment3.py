"""
CMPUT 297/115 - Assignment 3 Part 2 - Due 2013-03-08

Version 1.0 2013-03-07

By: Adam Ford

This assignment is a solo effort, and
any extra resources are cited in the code below.
"""

from digraph import Digraph
from least_cost_path import least_cost_path
from testcompare import tcompare
from euclidean_distance import euclidean_distance
import math
import sys
import serial
import argparse

global debug
debug = False

# Source: dumb_server.py provided with assignment details
def main():
    args = parse_args()

    s = Server()

    print("Welcome to Adam Ford's Assignment 3 Part 2 submission!")

    # Initialize some stuff...
    if args.serialport:
        print("Opening serial port: %s" % args.serialport)
        serial_out = serial_in =  serial.Serial(args.serialport, 9600)
    else:
        print("No serial port.  Supply one with the -s port option")
        exit()

    if args.verbose:
        debug = True
    else:
        debug = False

    s.import_file('edmonton_roads.txt')

    while True:
        args = receive(serial_in).rstrip().split(' ')
        if len(args) != 4: continue

        (lat1, long1, lat2, long2) = args

        debug and print('Finding path between {} and {}...'.format((lat1, long1), (lat2, long2)))

        path = s.find_shortest_path(int(lat1), int(long1), int(lat2), int(long2))

        send(serial_out, str(len(path)))

        for c in path:
            send(serial_out, '{} {}'.format(int(c[0]), int(c[1])))

# Source: dumb_server.py provided with assignment details
def send(serial_port, message):
    """
    Sends a message back to the client device.
    """
    print('message: ' + message)
    full_message = ''.join((message, "\n"))

    debug and print("server:" + full_message + ":")

    reencoded = bytes(full_message, encoding='ascii')
    serial_port.write(reencoded)


# Source: dumb_server.py provided with assignment details
def receive(serial_port, timeout=None):
    """
    Listen for a message. Attempt to timeout after a certain number of
    milliseconds.
    """
    raw_message = serial_port.readline()

    debug and print("client:", raw_message, ":")

    message = raw_message.decode('ascii')

    return message.rstrip("\n\r")


# Source: dumb_server.py provided with assignment details
def parse_args():
    """
    Parses arguments for this program.
    Returns an object with the following members:
        args.
             serialport -- str
             verbose    -- bool
             graphname  -- str
    """

    parser = argparse.ArgumentParser(
        description='Assignment 1: Map directions.',
        epilog = 'If SERIALPORT is not specified, stdin/stdout are used.')
    parser.add_argument('-s', '--serial',
                        help='path to serial port',
                        dest='serialport',
                        default=None)
    parser.add_argument('-v', dest='verbose',
                        help='verbose',
                        action='store_true')
    parser.add_argument('-g', '--graph',
                        help='path to graph (DEFAULT = " edmonton-roads-2.0.1.txt")',
                        dest='graphname',
                        default=' edmonton-roads-2.0.1.txt')

    return parser.parse_args()

class Server:
    def __init__(self):
        # contents: { vertex_id: ( lat, long ) }
        # lat and long values are stored in 100,000th of degrees
        self.vertex_locations = {}
        # contents: { ( v1, v2 ): name }
        self.edges = {}
        self.graph = Digraph()

    def import_file(self, filename):
        """
        Builds the graph and associated information from specified text file.
        """

        print('Importing {}...'.format(filename))
        scale = 100000
        count = 0
        for line in open(filename, 'r'):
            count += 1
            split_line = line.rstrip().split(',')
            line_type = split_line[0]

            if line_type == 'V':
                v = split_line[1]
                self.graph.add_vertex(v)
                self.vertex_locations[v] = (float(split_line[2]) * scale, float(split_line[3]) * scale)
            if line_type == 'E':
                t = (split_line[1], split_line[2])
                self.graph.add_edge(t)
                self.edges[t] = split_line[3]

        print('{} lines processed. Ready for input.'.format(count))

    def cost_distance(self, e):
        """
        cost_distance returns the straight-line distance between the two
        vertices at the endpoints of the edge e.

        >>> s = Server()
        >>> s.vertex_locations[29577354] = (400,-400)
        >>> s.vertex_locations[29770958] = (500,-500)
        >>> tcompare(100 * math.sqrt(2), s.cost_distance((29577354, 29770958)))
        True
        """
        #print('cost_distance: e = {}'.format(e))
        v1 = self.vertex_locations[e[0]]
        v2 = self.vertex_locations[e[1]]
        #print('cost_distance: v1 = {}; v2 = {}'.format(v1, v2))

        return euclidean_distance(v1, v2)

    def closest_vertex(self, lat, long):
        """
        Returns the id of the closest vertex to the specified lat and long
        >>> s = Server()
        >>> s.vertex_locations[29577354] = (5343099.6,-11349133.1)
        >>> s.vertex_locations[29770958] = (5357142.9,-11362729.9)
        >>> s.closest_vertex(5343099,-11349133)
        29577354
        """
        coords = (lat, long)
        closest = min(self.vertex_locations.items(), key=lambda x: euclidean_distance(coords, x[1]))
        return closest[0]

    def find_shortest_path(self, lat1, long1, lat2, long2):
        """
        Returns a least cost path of coordinates from (lat1, long1) to (lat1, long1)
        """
        v1 = self.closest_vertex(lat1, long1)
        v2 = self.closest_vertex(lat2, long2)

        #print('Closest vertices: {} and {}'.format(v1, v2))

        vertex_path = least_cost_path(self.graph, v1, v2, self.cost_distance)

        #print('vertex_path: {}'.format(vertex_path))

        path = []

        if vertex_path is not None:
            for v in vertex_path:
                path.append(self.vertex_locations[v])

        return path

if __name__ == "__main__":
    main()
