from cartas import Cartas
from clg import Vector_shuffle_set
from embaralhar import Embaralhar

if __name__ == "__main__":
    cartas = Cartas()
    vector_shuffle = Vector_shuffle_set()

    embaralhar = Embaralhar()
    resultado = embaralhar.embaralhar_cartas(cartas, vector_shuffle_set)
    print(resultado)
