n = int(input())
res = 0
for i in range(n):
    polyhedron = input()
    if polyhedron == "Icosahedron":
        res += 20
    elif polyhedron == "Tetrahedron":
        res += 4
    elif polyhedron == "Cube":
        res += 6
    elif polyhedron == "Octahedron":
        res += 8
    elif polyhedron == "Dodecahedron":
        res += 12
print(res)
    