def somme_nombres(*args):
    for nombre in args:
        nombre += nombre
    return nombre
print(somme_nombres(1,2,3,17))