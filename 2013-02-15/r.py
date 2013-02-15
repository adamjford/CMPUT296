infile = open('edmonton-roads-digraph.txt', 'rt')
for line in infile:
    fields = line.rstrip().split(',')

    type = fields.pop(0)
    if type == "E":
        (start, stop, name) = fields

        name = name.strip('"')

        print("{}->{}:{}".format(int(start), int(stop), name))
