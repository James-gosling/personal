# Actividad 17: Programa usando TDD — Nómina semanal

## 1. Análisis del problema
El programa captura **solo las horas trabajadas** y calcula el pago semanal.

| Tramo de horas | Regla de pago | Pago acumulado al límite |
|---|---|---|
| 0 – 40 | $200 por hora | $8,000 |
| 41 – 56 | 40 hrs normales + extras al doble ($400) | $14,400 |
| 57 – 64 | 40 normales + 16 dobles + resto al triple ($600) | $19,200 |
| < 0 o > 64 | Mensaje de número no válido | — |

Fórmula: `200 × (normales + 2 × dobles + 3 × triples)`, donde `normales = min(h, 40)`,
`dobles = min(max(h − 40, 0), 16)` y `triples = max(h − 56, 0)`.

## 2. Técnica aplicada: TDD (Rojo → Verde → Refactorizar)
Primero se escribió `test_nomina.py` y se ejecutó sin código: falló con
`ModuleNotFoundError` (**rojo**). Luego se escribió `nomina.py` con lo mínimo para pasar
(**verde**: 35 pruebas aprobadas) y se simplificó el cálculo a la fórmula única de arriba
(**refactor**), con las pruebas como red de seguridad.

Ciclos realizados, cada uno con sus pruebas:
1. **Tramo normal**: 0, 1, 20, 39 y 40 hrs.
2. **Tramo doble**: 41, 48, 55 y 56 hrs.
3. **Tramo triple**: 57, 60 y 64 hrs.
4. **Validación**: −1, −0.5, 64.5, 65, 100 (fuera de rango) y texto, `None`, vacío, `NaN`, booleano, lista (tipo inválido).
5. **Captura de entrada**: texto válido con espacios y formato de moneda; texto no válido (`abc`, `65`, `-5`, `inf`, …) devuelve el mensaje de error.

## 3. Interpretación de evidencias y justificación de resultados
Se usó **análisis de valores límite**, porque los errores de cálculo se concentran en las
fronteras de cada tramo (40/41, 56/57, 64/65, 0/−1). Resultados esperados verificados:

| Horas | Pago | Justificación |
|---|---|---|
| 0 | $0 | Límite inferior válido |
| 40 | $8,000 | 40 × 200 |
| 41 | $8,400 | 8,000 + 1 × 400 |
| 56 | $14,400 | 8,000 + 16 × 400 |
| 57 | $15,000 | 14,400 + 1 × 600 |
| 64 | $19,200 | 14,400 + 8 × 600 |
| 65 | Número no válido | Excede el máximo semanal |

Evidencia de ejecución: `35 passed`.

## 4. Cómo ejecutar
```
pip install pytest
python3 -m pytest -v     # pruebas automatizadas
python3 nomina.py        # programa interactivo
```
