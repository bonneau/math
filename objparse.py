import sys


def parse(filename):
    vertices = []
    faces = []

    for line in open(filename, 'r'):
        if line.startswith('#'):
            # This is a comment, ignore
            continue
        values = line.split()
        if not values:
            # Empty line, ignore
            continue

        cmd = values[0]
        if cmd == 'v':
            params = tuple(map(float, values[1:4]))
            vertices.append(params)
        elif cmd == 'f':
            # TODO: Add support for texture and vertext normal indexes as well: http://paulbourke.net/dataformats/obj/
            params = tuple(map(int, values[1:4]))
            faces.append(params)
        else:
            print('"{0}" is a currently unsupported command'.format(cmd))

    return vertices, faces


def main(args):
    print(args)
    v, f = parse(args[1])
    print('Vertices: {0}'.format(v))
    print('Faces:    {0}'.format(f))


if __name__ == '__main__':
    main(sys.argv)
