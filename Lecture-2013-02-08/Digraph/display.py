# an extension to the graph module that generates .dot files for graphviz
import graph
import time
import sys

def gen_dot_desc(G, attributes={}):
    """
    >>> g = ({1, 2, 3}, {(1, 2), (1, 3)} )
    >>> s = gen_dot_desc(g)
    >>> s
    
 
    """
    if "vertex_color" in attributes:
        vertex_color=attributes["vertex_color"]
    else:
        vertex_color={ }

    if "edge_color" in attributes:
        edge_color=attributes["edge_color"]
    else:
        edge_color={ }

    if "vertex_label" in attributes:
        vertex_label=attributes["vertex_label"]
    else:
        vertex_label={ }

    if "edge_label" in attributes:
        edge_label=attributes["edge_label"]
    else:
        edge_label={ }

    (V, E) = G

    # generate the header
    dot_desc = ( "digraph g {\n" + 
        "  ordering=out;\n" +
        "  node [shape=circle];\n" +
        "  edge [penwidth=3];\n" 
        )

    # now generate vertex and edges information
    if len(V) == 0:
       dot_desc += "Empty [shape=ellipse];\n"
    else:
        for n in V:
            color = "white"
            if n in vertex_color: 
                color = vertex_color[n]

            label = str(n)
            if n in vertex_label: 
                label = vertex_label[n]

            dot_desc += '  {v} [label="{l}", style=filled, fillcolor="{c}"];\n'.format(
                v=str(n), l=label, c=color)

        for e in E:
            (x, y) = e
            color = "black"
            if e in edge_color: 
                color = edge_color[e]
            label = ""
            if e in edge_label:
                label = ', label="{}"'.format(edge_label[e])

            dot_desc += '  {vx} -> {vy} [color="{c}" {l}];\n'.format(
                    vx=str(x), vy=str(y), c=color, l=label)


    # close off the description
    dot_desc += "}\n"

    return dot_desc

def write_dot_desc(G, file_name, attributes={}):
    # instead of f = open(file_name, 'w') inside a try block, use
    # the safe open that closes file on an exception, from
    # http://docs.python.org/3.2/tutorial/inputoutput.html

    with open(file_name, 'w') as f:
        f.write( gen_dot_desc(G, attributes) )

def pause(time=1,prompt="next?"):
    # pause for time sec, or if time=0 wait for a new line from the terminal
    if time > 0:
        time.sleep(time)
    else:
        x = input(prompt)
        
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()

