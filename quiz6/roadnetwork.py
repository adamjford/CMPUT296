import digraph
import math

# Probably would be better to switch this to Haversine
def latlon_distance(a, b):
    ((alat, alon), (blat, blon)) = (a, b)
    return math.hypot(alat - blat, alon - blon)

# This is a very cool helper function!
# It lets you iterate over consecutive pairs from a list.
import itertools
def pairwise(iterable):
    """s -> (s0,s1), (s2,s3), (s4, s5), ...

    >>> for pair in pairwise([1, 2, 3, 4, 5]): print(pair)
    (1, 2)
    (2, 3)
    (3, 4)
    (4, 5)
    """
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

class RoadNetwork:
    """
    Class for computing paths in road networks.

    >>> roads = RoadNetwork('simple_roads.txt')
    >>> roads.route((0.0, 0.0), (0.0, 0.0))
    [(0.0, 0.0)]
    >>> roads.route((-1.0, 0.0), (1.0, 0.0))
    [(-1.0, 0.0), (0.0, 2.0), (1.0, 0.0)]

    >>> roads.route_names((-1.0, 0.0), (1.0, 0.0))
    ['2 to 3', '3 to 4']

    >>> print(roads.route_directions((-1.0, 0.0), (1.0, 0.0)))
    Go East on 2 to 3.
    Go West on 3 to 4.
    """
    
    def __init__(self, mapfilename):
        self.V_coord = {}
        self.E_name = {}
        self.graph = digraph.Digraph()
        
        file = open(mapfilename, "r")
        for line in file:
            # strip all trailing whitespace
            line = line.rstrip()

            fields = line.split(",")
            type = fields[0]

            if type == 'V':
                # got a vertex record
                (id,lat,long) = fields[1:]

                # vertex id's should be ints
                id=int(id)

                # lat and long are floats
                lat=float(lat)
                long=float(long)
                
                self.V_coord[id] = (lat,long)
                self.graph.add_vertex(id)
        
            elif type == 'E':
                # got an edge record
                (start,stop,name) = fields[1:]

                # vertices are ints
                start=int(start)
                stop=int(stop)
                e = (start,stop)

                # get rid of leading and trailing quote " chars around name
                name = name.strip('"')

                # consistency check, we don't want auto adding of
                # vertices when adding an edge.
                if start not in self.V_coord or stop not in self.V_coord:
                    raise RuntimeError("Edge {} has an endpoint that is not a vertex".format(e)) 

                self.E_name[e] = name
                self.graph.add_edge(e)
            else:
                # weird input
                raise RuntimeError("Error: weird line |{}|".format(line))

    def _nearest_vertex(self, coord):
        return min(self.V_coord.keys(),
                   key = lambda v: latlon_distance(coord, self.V_coord[v]))

    def cost_distance(self, e):
        return latlon_distance(self.V_coord[e[0]], self.V_coord[e[1]])

    def route(self, start, end):
        path  = digraph.least_cost_path(self.graph,
                                        self._nearest_vertex(start),
                                        self._nearest_vertex(end),
                                        self.cost_distance)
        return [ self.V_coord[v] for v in path ]


    ###### CODE YOU HAVE TO WRITE #####
    def route_names(self, start, end):
        """
        This method should return the list of road names you travel on to
        get from start to end.  Paths often include edges that are the same
        road, as the path goes from block to block.  If you remain on the
        same road it should only output that road name once.

        So instead of:
        [ '111 Ave NW', 
          '111 Ave NW',
          '111 Ave NW',
          '99 St Ave',
          '99 St Ave',
          'Jasper Ave NW' ]

        It should return:
        [ '111 Ave NW', 
          '99 St Ave',
          'Jasper Ave NW' ]

        >>> n = RoadNetwork('simple_roads.txt')
        >>> n.route_names(1, 5)
        [ '1 to 4', '4 to 5' ]
        >>> n.route_names(5, 1)
        [ '5 to 1' ]
        >>> n.route_names(2, 5)
        [ '2 to 3', '3 to 4', '4 to 5' ]
        """
        pass

    def route_directions(self, start, end):
        """
        This method should return a string with directions to go from start
        to end.  Each road to be travelled on should result in another line
        in the directions.  The directions should be in the form of:

        Go East on 111 Ave NW.
        Go South on 99 St Ave.
        Go East on Jasper Ave.

        The directions should only cover the four cardinal directions.  A
        road travelling exactly NW could either appear as North or West.

        This specific implementation prefers North or South over East or
        West.

        >>> n = RoadNetwork('simple_roads.txt')
        >>> n.route_directions(1, 5)
        Go North on 1 to 4.
        Go South on 4 to 5.
        >>> n.route_directions(5, 1)
        Go East on 5 to 1.
        >>> n.route_directions(2, 5)
        Go North on 2 to 3.
        Go North on 3 to 4.
        Go South on 4 to 5.
        """
        pass

    ######################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
