"""Pruebas automatizadas de la nómina semanal (escritas antes que el código, TDD)."""
import pytest

from nomina import MENSAJE_NO_VALIDO, calcular_pago, procesar_entrada


# Ciclo 1: tramo normal (0 a 40 hrs, $200 por hora)
@pytest.mark.parametrize(
    "horas, esperado",
    [
        (0, 0),          # límite inferior válido
        (1, 200),
        (20, 4000),
        (39, 7800),
        (40, 8000),      # límite superior del tramo normal
    ],
)
def test_tramo_normal(horas, esperado):
    assert calcular_pago(horas) == esperado


# Ciclo 2: tramo doble (41 a 56 hrs): 40 normales + extras al doble ($400)
@pytest.mark.parametrize(
    "horas, esperado",
    [
        (41, 8400),      # primer valor del tramo doble
        (48, 8000 + 8 * 400),
        (55, 8000 + 15 * 400),
        (56, 14400),     # límite superior del tramo doble
    ],
)
def test_tramo_doble(horas, esperado):
    assert calcular_pago(horas) == esperado


# Ciclo 3: tramo triple (57 a 64 hrs): 40 normales + 16 dobles + resto al triple ($600)
@pytest.mark.parametrize(
    "horas, esperado",
    [
        (57, 14400 + 600),   # primer valor del tramo triple
        (60, 14400 + 4 * 600),
        (64, 19200),         # límite superior permitido
    ],
)
def test_tramo_triple(horas, esperado):
    assert calcular_pago(horas) == esperado


# Ciclo 4: validación (solo 0 a 64 hrs)
@pytest.mark.parametrize("horas", [-1, -0.5, 64.5, 65, 100])
def test_horas_fuera_de_rango(horas):
    with pytest.raises(ValueError):
        calcular_pago(horas)


@pytest.mark.parametrize("horas", ["abc", None, "", float("nan"), True, [40]])
def test_horas_con_tipo_invalido(horas):
    with pytest.raises(ValueError):
        calcular_pago(horas)


def test_horas_decimales_validas():
    assert calcular_pago(40.5) == 8000 + 0.5 * 400


# Ciclo 5: captura de la entrada del usuario
@pytest.mark.parametrize(
    "texto, esperado",
    [
        ("40", "Pago semanal: $8,000.00"),
        (" 56 ", "Pago semanal: $14,400.00"),
        ("64", "Pago semanal: $19,200.00"),
        ("0", "Pago semanal: $0.00"),
    ],
)
def test_procesar_entrada_valida(texto, esperado):
    assert procesar_entrada(texto) == esperado


@pytest.mark.parametrize("texto", ["-5", "65", "abc", "", "4 0", "nan", "inf"])
def test_procesar_entrada_no_valida(texto):
    assert procesar_entrada(texto) == MENSAJE_NO_VALIDO
