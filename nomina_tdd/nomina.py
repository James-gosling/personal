"""Cálculo de la nómina semanal de empleados (desarrollado con TDD)."""
import math

PAGO_POR_HORA = 200
LIMITE_NORMAL = 40
LIMITE_DOBLE = 56
LIMITE_MAXIMO = 64
MENSAJE_NO_VALIDO = "Número no válido: ingrese horas entre 0 y 64."


def calcular_pago(horas):
    """Devuelve el pago semanal; lanza ValueError si las horas no son válidas."""
    if isinstance(horas, bool) or not isinstance(horas, (int, float)):
        raise ValueError("Las horas deben ser un número")
    if math.isnan(horas) or not 0 <= horas <= LIMITE_MAXIMO:
        raise ValueError("Las horas deben estar entre 0 y 64")

    normales = min(horas, LIMITE_NORMAL)
    dobles = min(max(horas - LIMITE_NORMAL, 0), LIMITE_DOBLE - LIMITE_NORMAL)
    triples = max(horas - LIMITE_DOBLE, 0)
    return PAGO_POR_HORA * (normales + 2 * dobles + 3 * triples)


def procesar_entrada(texto):
    """Convierte el texto capturado y devuelve el mensaje a mostrar."""
    try:
        pago = calcular_pago(float(texto))
    except ValueError:
        return MENSAJE_NO_VALIDO
    return f"Pago semanal: ${pago:,.2f}"


def main():
    print(procesar_entrada(input("Horas trabajadas en la semana (0-64): ")))


if __name__ == "__main__":
    main()
