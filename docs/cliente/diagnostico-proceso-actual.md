# Healthy Tummies — Diagnóstico del proceso actual

**Fecha:** septiembre 2026
**Preparado por:** monclair
**Unidad de análisis:** 100 alumnos inscritos en un servicio, en una escuela, durante un mes

---

## 1. Cómo funciona hoy

```
Healthy Tummies arma el menú del mes
        │
        ▼
Lo envía a cada escuela  ──────▶  La escuela lo circula entre los papás
                                          │
                                          ▼
                            El papá decide y transfiere por banco
                                          │
                                          ▼
                        Manda el comprobante a Healthy Tummies
                                          │
                                          ▼
              ⚠️  VERIFICACIÓN MANUAL  ⚠️   ← aquí está el cuello de botella
              Alguien coteja cada comprobante contra el estado de cuenta
              y anota a mano quién sí tiene servicio
                                          │
                        ┌─────────────────┴─────────────────┐
                        ▼                                   ▼
            Conteos para la cocina              Lista de nombres para la cafetería
            (cuántas órdenes por                (a quién sí se le entrega)
             servicio y escuela)
                        │                                   │
                        ▼                                   ▼
              Producción en cocina central  ────▶  Entrega al niño en la escuela
```

Todo lo que está debajo de la verificación manual **depende de que esa verificación
esté correcta y al día**. Si un pago se registra tarde, el niño no aparece en la lista.
Si un pago se deja de registrar, el niño sigue apareciendo y come sin haber pagado.

---

## 2. Dónde se va el dinero

Se identifican tres fugas. Van ordenadas de la más visible a la más costosa — que es
justo al revés de como se suelen percibir.

### Fuga 1 — Horas administrativas

El trabajo de recibir comprobantes, cotejarlos, perseguir los que no cuadran, armar la
lista de la cafetería y recalcular los conteos de la cocina todos los días.

| Tarea | Tiempo modelado |
|---|---|
| Recibir, clasificar y cotejar 100 comprobantes | 400 min |
| Seguimiento de los que no cuadran (15%) | 120 min |
| Armar y mantener la lista de cafetería | 290 min |
| Recalcular conteos de cocina | 200 min |
| **Total por cada 100 alumnos en un servicio** | **≈ 17 horas al mes** |

A un costo cargado de $90/hora: **≈ $1,515 al mes**, por cada 100 alumnos, por cada
servicio, por cada escuela. Y **crece en línea recta con el negocio**: el doble de
alumnos es el doble de horas.

### Fuga 2 — Servicio entregado por error

Niños que quedaron en la lista aunque dejaron de pagar, o que fueron dados de alta con
información incompleta. Modelado al 2% de los inscritos, con insumos al 40% del precio:
**≈ 0.8% del ingreso** de ese servicio.

### Fuga 3 — Servicio entregado y nunca cobrado ← la más grande

Es la consecuencia directa de verificar a mano: pagos que nunca se confirmaron,
inscripciones tardías a las que nadie les cobró la penalización del día 5, meses que se
sirvieron completos y se facturaron a medias.

Modelado al **3% del ingreso**, y es un supuesto conservador para un proceso manual.

> **Este número no lo sabemos: lo sabe Healthy Tummies.** Es la pregunta más importante
> de la conversación. Si la cifra real es 1%, el proyecto se justifica igual pero más
> lento. Si es 6%, se paga solo en menos de medio año. Todo lo demás en este documento es
> aritmética; esto es el negocio.

---

## 3. El costo por cada 100 alumnos, servicio por servicio

| Servicio | Precio | Ingreso /100 | Horas | Fuga 2 | Fuga 3 | **Costo total** | % del ingreso |
|---|---:|---:|---:|---:|---:|---:|---:|
| Preescolar · Lunch | $1,250 | $125,000 | $1,515 | $1,000 | $3,750 | **$6,265** | 5.0% |
| Preescolar · Comida | $1,250 | $125,000 | $1,515 | $1,000 | $3,750 | **$6,265** | 5.0% |
| Preescolar · Taller 2x | $550 | $55,000 | $1,155 | $440 | $1,650 | **$3,245** | 5.9% |
| Primaria · Lunch | $1,200 | $120,000 | $1,515 | $960 | $3,600 | **$6,075** | 5.1% |
| Primaria · Comida | $1,350 | $135,000 | $1,515 | $1,080 | $4,050 | **$6,645** | 4.9% |
| Primaria · Taller 2x | $600 | $60,000 | $1,155 | $480 | $1,800 | **$3,435** | 5.7% |
| Primaria · Almuerzo | $1,350 | $135,000 | $1,515 | $1,080 | $4,050 | **$6,645** | 4.9% |

**El proceso manual cuesta entre 4.9% y 5.9% del ingreso de cada servicio.** Los talleres
salen proporcionalmente peor: se cobran cuatro veces menos que un servicio diario, pero
verificar sus pagos cuesta prácticamente lo mismo.

---

## 4. La comisión que pagan los papás

Como la comisión del procesador la absorbe el papá, elegir bien la pasarela es dinero
que se le devuelve al cliente final. La diferencia entre cobrar con tarjeta y cobrar por
transferencia SPEI es grande, porque **en SPEI la comisión es fija, no porcentual**.

| Servicio | Con tarjeta /100 | Con SPEI /100 | Le ahorra a los papás |
|---|---:|---:|---:|
| Preescolar · Lunch | $4,800 | $812 | **$3,988** |
| Preescolar · Comida | $4,800 | $812 | **$3,988** |
| Preescolar · Taller 2x | $2,280 | $812 | **$1,468** |
| Primaria · Lunch | $4,620 | $812 | **$3,808** |
| Primaria · Comida | $5,160 | $812 | **$4,348** |
| Primaria · Taller 2x | $2,460 | $812 | **$1,648** |
| Primaria · Almuerzo | $5,160 | $812 | **$4,348** |

Sobre un servicio de $1,250, la tarjeta le cuesta al papá $48 y el SPEI $8.12.

Y lo más importante no es el ahorro: **los papás ya pagan por transferencia hoy.** Cobrar
por SPEI no les cambia el hábito en nada. Lo único que cambia es que el pago llega
identificado y conciliado solo, en lugar de llegar como un comprobante que alguien tiene
que revisar.

---

## 5. Qué recupera la plataforma

| Fuga | Qué la resuelve | Recuperación estimada |
|---|---|---|
| Horas administrativas | Conciliación automática por SPEI; listas y conteos generados solos | 85% |
| Servicio por error | Una sola fuente de verdad entre cobro, lista y conteo | 80% |
| Servicio no cobrado | No hay inscripción sin pago confirmado; penalización automática tras el día 5 | 90% |

**Recuperación por cada 100 alumnos, al mes:**

| Servicio | Recuperación mensual |
|---|---:|
| Preescolar · Lunch | $5,463 |
| Preescolar · Comida | $5,463 |
| Preescolar · Taller 2x | $2,819 |
| Primaria · Lunch | $5,296 |
| Primaria · Comida | $5,797 |
| Primaria · Taller 2x | $2,986 |
| Primaria · Almuerzo | $5,797 |

### Escenario ilustrativo

Tres escuelas, 200 alumnos-servicio cada una — 600 en total, con una mezcla de 70%
servicios diarios y 30% talleres:

| | |
|---|---:|
| Recuperación mensual | **≈ $28,600** |
| Recuperación anual | **≈ $343,000** |
| Recuperación de la inversión de la Fase 1 | **entre 6 y 11 meses**, según el alcance final |

Y el beneficio no se queda ahí: **hoy el costo administrativo crece en línea recta con
los alumnos.** Con la plataforma, deja de hacerlo. La cuarta escuela no cuesta lo mismo
que costó la primera.

---

## 6. Supuestos de este modelo

Todo lo anterior es un modelo, no una medición. Estos son los supuestos que lo sostienen,
y cada uno debe validarse con datos reales de Healthy Tummies:

| Supuesto | Valor usado |
|---|---|
| Días de servicio al mes | 20 (8 para talleres) |
| Tiempo por comprobante | 4 minutos |
| Pagos con incidencia | 15%, a 8 minutos cada uno |
| Costo cargado por hora administrativa | $90 MXN |
| Insumos como porcentaje del precio | 40% |
| Servicio entregado por error | 2% de los inscritos |
| **Servicio entregado y nunca cobrado** | **3% del ingreso** ← el más sensible |

Cambiar el último supuesto mueve el resultado más que todos los demás juntos. Con la
cifra real en mano, este documento pasa de ser un modelo a ser un caso de negocio.

---

## 7. Datos que hacen falta

1. Alumnos inscritos hoy, por escuela y por servicio
2. Cuánto servicio se entrega al mes sin cobrarse
3. Días de servicio reales al mes
4. Costo de insumos como porcentaje del precio de venta
5. Quién hace hoy la verificación de comprobantes y cuánto tiempo le dedica
