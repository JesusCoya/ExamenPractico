from kanren import Relation, facts, run, conde, var

# Definir relaciones
padre = Relation()
hermano = Relation()

# Establecer hechos
facts(
    padre,
    ("Antonio Alejo", "Aida Alejo"),
    ("José Coya", "Gregorio Coya"),
    ("Benedicto Mamani", "María Mamani"),
    ("Juan Huiza", "Willy Huiza"),
    ("Juan Huiza", "Bertha Huiza"),
    ("Juan Huiza", "Rolando Huiza"),
    ("Juan Huiza", "Jhony Huiza"),
    ("Juan Huiza", "Monica Huiza"),
    ("Juan Huiza", "Hilda Huiza"),
    ("Gregorio Coya", "Arturo Coya"),
    ("Gregorio Coya", "Macario Coya"),
    ("Arturo Coya", "Mary Luz Coya"),
    ("Jesus Coya", "Rogelio"),
    ("Santusa", "Aida Alejo"),
    ("María Ramos", "Gregorio Coya"),
    ("Felicia", "María Mamani"),
    ("Aida Alejo", "Willy Huiza"),
    ("Aida Alejo", "Bertha Huiza"),
    ("Aida Alejo", "Rolando Huiza"),
    ("Aida Alejo", "Jhony Huiza"),
    ("Aida Alejo", "Monica Huiza"),
    ("Aida Alejo", "Hilda Huiza"),
    ("María Mamani", "Arturo Coya"),
    ("María Mamani", "Macario Coya"),
    ("Hilda Huiza", "Mary Luz Coya"),
    ("Hilda Huiza", "Jesus Coya"),
    ("Hilda Huiza", "Alessandra Coya"),
    ("Hilda Huiza", "Arturo Coya"),
    ("Aida Alejo", "Arturo Coya"),  # Corrección añadida para coherencia
)

facts(
    hermano,
    ("Bertha Huiza", "Willy Huiza"),
    ("Rolando Huiza", "Willy Huiza"),
    ("Jhony Huiza", "Willy Huiza"),
    ("Monica Huiza", "Willy Huiza"),
    ("Hilda Huiza", "Willy Huiza"),
    ("Willy Huiza", "Bertha Huiza"),
    ("Rolando Huiza", "Bertha Huiza"),
    ("Jhony Huiza", "Bertha Huiza"),
    ("Monica Huiza", "Bertha Huiza"),
    ("Hilda Huiza", "Bertha Huiza"),
    ("Willy Huiza", "Rolando Huiza"),
    ("Bertha Huiza", "Rolando Huiza"),
    ("Jhony Huiza", "Rolando Huiza"),
    ("Monica Huiza", "Rolando Huiza"),
    ("Hilda Huiza", "Rolando Huiza"),
    ("Willy Huiza", "Jhony Huiza"),
    ("Bertha Huiza", "Jhony Huiza"),
    ("Rolando Huiza", "Jhony Huiza"),
    ("Monica Huiza", "Jhony Huiza"),
    ("Hilda Huiza", "Jhony Huiza"),
    ("Willy Huiza", "Monica Huiza"),
    ("Bertha Huiza", "Monica Huiza"),
    ("Rolando Huiza", "Monica Huiza"),
    ("Jhony Huiza", "Monica Huiza"),
    ("Hilda Huiza", "Monica Huiza"),
    ("Willy Huiza", "Hilda Huiza"),
    ("Bertha Huiza", "Hilda Huiza"),
    ("Rolando Huiza", "Hilda Huiza"),
    ("Jhony Huiza", "Hilda Huiza"),
    ("Monica Huiza", "Hilda Huiza"),
)


# Definir funciones
def abuelo(x, z):
    y = var()
    return conde((padre(x, y), padre(y, z)))


def primo(x, z):
    y = var()
    w = var()
    return conde((padre(y, x), padre(w, z), hermano(w, y)))


def tio(x, z):
    y = var()
    return conde((padre(y, z), hermano(x, y)))


# Funciones para consultas
def abuelo_rel(x, z):
    return run(0, x, abuelo(x, z))


def primo_rel(x, z):
    return run(0, x, primo(x, z))


def tio_rel(x, z):
    return run(0, x, tio(x, z))


# Consultas
x = var()

# Consulta: Abuelos de 'Jesus Coya'
print("\nAbuelos de Jesus Coya:")
print(abuelo_rel(x, "Jesus Coya"))

# Consulta: Primos de 'Rogelio Coya'
print("\nPrimos de Rogelio:")
print(primo_rel(x, "Rogelio"))

# Consulta: Tíos de 'Rogelio Coya'
print("\nTios de Alessandra Coya:")
print(tio_rel(x, "Alessandra Coya"))
