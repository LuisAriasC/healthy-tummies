# Healthy Tummies — Diseño de la propuesta y de la Fase 1

**Fecha:** 2026-09-20
**Autor:** Luis Carlos Arias Camacho (monclair)
**Estado:** Diseño aprobado en brainstorming; pendiente de revisión

---

## 1. Contexto

Healthy Tummies es una empresa mexicana de preparación y servicio de catering en
escuelas de kinder y primaria. Opera hoy con un proceso mayormente manual y **no ha
contratado nada todavía**: este documento sustenta una propuesta comercial que se
presenta esta semana.

El cliente **no tiene claro qué quiere**. La propuesta tiene que hacer dos trabajos a
la vez: mostrarle que su problema es real y costoso, y darle un camino concreto que
empiece pequeño.

**Etapa:** propuesta para ganar el proyecto. Nada se construye hasta que haya un sí.

---

## 2. Cómo opera el negocio hoy

Healthy Tummies arma un menú mensual por servicio y lo envía a las escuelas con las que
trabaja. Cada escuela lo circula entre los papás, que deciden si contratan. El chef
revisa el menú, todo se cocina en una **cocina central** por día y por servicio, se
distribuye a cada escuela, y en la cafetería se entrega al niño.

La información está partida entre tres lugares:

| Quién | Qué sabe |
|---|---|
| Cocina central | Solo cantidades por servicio, por escuela |
| Cafetería de la escuela | Lista con nombres de niños, para saber a quién entregar |
| Healthy Tummies | Quién pagó — verificado **a mano**, contra comprobantes bancarios |

**Escala actual:** piloto de 1 a 3 escuelas.

### Servicios y precios mensuales

| Servicio | Preescolar | Primaria |
|---|---|---|
| Lunch | $1,250 | $1,200 |
| Comida | $1,250 | $1,350 |
| Comida 2x/semana por taller | $550 | $600 |
| Almuerzo | — | $1,350 |

Los precios están confirmados por el cliente, incluido que el Lunch de primaria
($1,200) sea más barato que el de preescolar ($1,250). No es error de captura.

### El flujo de dinero

**Hoy todas las escuelas operan en modo directo:** el papá le transfiere a Healthy
Tummies y manda el comprobante. Healthy Tummies lo verifica a mano.

En una respuesta anterior el cliente describió el cobro como mixto y después lo corrigió
a que todas están en directo. La lectura que se adopta es que **el modo concentrado
—que la escuela cobre y entregue un consolidado— es posible en el futuro pero no existe
hoy**. Decisión de diseño: el modelo de datos conserva un campo de modo de cobro a nivel
escuela, porque cuesta casi nada, pero **la Fase 1 no construye el flujo concentrado**.
Eso quita alcance sin cerrar la puerta.

**Facturación:** Healthy Tummies factura **tanto a los papás como a las escuelas**.

---

## 3. El problema, en una línea

Healthy Tummies verifica a mano, contra comprobantes bancarios, quién pagó cada
servicio de cada niño de cada escuela cada mes — y de esa verificación manual dependen
las listas de la cafetería y los conteos de la cocina.

---

## 4. Reglas de negocio confirmadas

Estas vienen del cliente y están cerradas:

| Regla | Definición |
|---|---|
| Fecha de corte | **Día 5 de cada mes.** Hasta ese día se inscribe sin penalización |
| Alta después del corte | Sin prorrateo. Se cobra **penalización** |
| Monto de la penalización | Configurable **por menú**: un porcentaje o una cantidad fija |
| Bajas | Sin devolución |
| Ausencias del niño | Se pierden. No se reponen ni se acreditan |
| Comisión del PSP | La absorbe **el papá** |
| Taller 2x/semana | Dos días cualesquiera de la semana, **elegidos por el papá** |
| Facturación | A papás **y** a escuelas |

**Consecuencia técnica importante, y es buena noticia para el costo:** sin prorrateo,
sin reembolsos y sin reposiciones, el cobro es un cargo mensual simple. No hay lógica
de créditos, devoluciones parciales ni saldos a favor — que es exactamente donde este
tipo de sistemas se vuelve caro y lento. Vale la pena decírselo al cliente: sus propias
reglas le están abaratando el desarrollo.

**Consecuencia en la interfaz:** como el papá absorbe la comisión, el precio en
pantalla no es $1,250 — es $1,250 más comisión, desglosada a la vista. Debe aparecer
así en el prototipo. Esto vuelve la elección de pasarela una decisión de producto, no
solo de infraestructura: define lo que el papá ve que paga de más. Ver sección 6.

**Consecuencia en el modelo:** que el papá elija libremente los dos días del taller
significa que la inscripción al servicio de taller **almacena los dos días elegidos**.
Los conteos de cocina de ese servicio ya no son un número por escuela: son un número por
escuela y por día de la semana, porque cada papá puede haber elegido una combinación
distinta. Es la parte menos trivial del modelo de datos.

**Consecuencia en el cobro:** la penalización se define por menú y puede ser porcentaje o
monto fijo, así que es **configuración, no código**. El panel de administración necesita
capturarla al publicar cada menú, y el cobro tiene que aplicarla automáticamente a quien
se inscriba después del día 5.

---

## 5. Preguntas que siguen abiertas

La mayoría se resolvieron. Quedan estas para la junta:

1. **Volumen real por escuela y por servicio.** Número de niños inscritos hoy. Es el dato
   que convierte el diagnóstico de la sección 13 en cifras reales en vez de un modelo.
2. **¿Ya tienen cuenta con algún PSP?** ¿Con qué banco está la cuenta de la empresa? De
   eso depende qué tan rápido se puede habilitar el cobro (ver sección 6).
3. **¿Cuánto servicio se entrega al mes sin haberse cobrado?** Niños que aparecen en la
   lista pero cuyo pago nunca se confirmó, o que pagaron tarde y nadie cobró penalización.
   **Es la pregunta más importante de la junta** — ahí está la mayor parte del retorno.
4. **Días de servicio al mes** y **costo de insumos como porcentaje del precio.** Se usan
   para el diagnóstico; ahora mismo están modelados con supuestos.

---

## 6. Enfoque elegido

Se evaluaron tres caminos:

| Enfoque | Qué es | Por qué no |
|---|---|---|
| **A — Plataforma completa** | Fase 1 incluye ya portales con acceso propio para escuela y cocina | Lo caro no son los datos, son los portales, logins y permisos. A tres escuelas es construir de más |
| **B — Ensamblado no-code** | Links de pago + base tipo Airtable + automatizaciones | Techo bajo, costo recurrente por usuario, se rompe justo al crecer |
| **C — Público a la medida** ✅ | Se construye bien solo la superficie donde entra el dinero; hacia adentro, exportables automáticos | **Elegido** |

### Por qué C

Una vez que el papá se inscribe y paga en el sistema, el roster **ya vive en la base de
datos**. Sacar la lista de la cafetería y los conteos de la cocina es casi gratis. Lo
verdaderamente caro de A son los portales con sus accesos y permisos — y a tres
escuelas, la persona de la cafetería probablemente prefiere su lista impresa antes que
aprenderse un sistema.

C entrega el mismo valor operativo que A, con bastante menos superficie que construir, y
es el "sí" más fácil de conseguir de un cliente que todavía no sabe qué quiere.

### Pasarela de pagos: Stripe cobrando por SPEI

Esta decisión merece su propio análisis porque **la comisión la paga el papá**, así que
elegir mal encarece el servicio a la vista del cliente final.

Comisiones vigentes a septiembre de 2026:

| Pasarela | Tarjeta | SPEI (transferencia) | OXXO |
|---|---|---|---|
| **Stripe** | 3.6% + $3 | **$7 + IVA ≈ $8.12 fijo** | — |
| Conekta (BBVA) | 3.4% + $3 + IVA | desde $12.50 + IVA | 2.6% + $3 + IVA |
| Mercado Pago | 3.49% + $4 + IVA | 3.49% + $4 (cobra como tarjeta) | — |
| Openpay (BBVA) | desde 2.9% + $2.50, negociable | — | — |

**El hallazgo: en SPEI la comisión es fija, no porcentual.** Sobre un servicio de $1,250,
la tarjeta cuesta $48 y el SPEI cuesta $8.12. Es seis veces menos, y lo paga el papá.

Y hay un argumento todavía más fuerte que el precio: **los papás ya pagan por
transferencia bancaria hoy.** Cobrar por SPEI no les cambia el hábito en absoluto — lo
único que cambia es que Healthy Tummies deja de verificar el comprobante a mano, porque
la conciliación llega resuelta. Se automatiza exactamente el proceso que ya existe, en
lugar de pedirle al papá que aprenda otro.

**Recomendación: Stripe, con SPEI como método principal y tarjeta como alternativa** para
quien la prefiera, mostrando la diferencia de comisión en pantalla.

Dos advertencias honestas: estas tarifas son de lista y **en volumen se negocian**, así
que conviene pedir cotización a Stripe y a Conekta antes de firmar; y si en algún momento
quieren cobrar en efectivo, Conekta con OXXO Pay entra mejor que Stripe.

### Nota comercial

**B se incluye en la propuesta como comparación explícita, aunque no se recomiende.**
Mostrarle al cliente que se evaluó la opción barata, y explicar con honestidad por qué
no le conviene a largo plazo, posiciona a monclair como alguien que cuida su dinero en
lugar de alguien que quiere venderle un desarrollo. Con un cliente indeciso, eso cierra
tratos.

---

## 7. Alcance de la Fase 1

### De cara al papá

- Sitio público con el menú del mes, filtrado por escuela y nivel
- Registro del tutor y alta de sus hijos (nombre, escuela, grado, grupo)
- Selección de servicio por niño, con catálogo y precio correctos según nivel
- **Para el servicio de taller, elección de los dos días de la semana** que le
  corresponden a ese niño
- Pago en línea del mes por SPEI o tarjeta, con la comisión desglosada a la vista y la
  diferencia entre ambos métodos visible
- Aplicación automática de la **penalización** a quien se inscriba después del día 5
- Confirmación y recibo

### De cara a Healthy Tummies

- Panel de administración: escuelas, precios, niños, inscripciones y estado de pago
- Carga del menú del mes, **con su penalización asociada** (porcentaje o monto fijo)
- Generación automática de la **lista de cafetería**, por escuela y día, con nombres
- Generación automática de los **conteos de cocina**, por escuela, servicio y día —
  respetando los días elegidos individualmente en el servicio de taller
- Entrega de ambos por correo o descarga, en PDF y hoja de cálculo
- Conciliación automática de los pagos SPEI, sin revisar comprobantes a mano

### Fuera de alcance de la Fase 1

Debe decirse explícitamente en la propuesta, para que nadie lo dé por hecho:

- Portales con acceso propio para escuela y cocina
- Constructor de menús (en Fase 1 el menú se carga como archivo)
- **Facturación / CFDI automatizada.** El cliente factura a papás y a escuelas; en Fase 1
  eso sigue haciéndose fuera del sistema. Automatizarlo es Fase 3
- **Modo de cobro concentrado** (que la escuela cobre y entregue un consolidado). Hoy
  ninguna escuela opera así; el campo queda en el modelo, el flujo no se construye
- Aplicación móvil

---

## 8. Modelo conceptual

Todo el sistema gira alrededor de **una sola unidad: la inscripción de un niño a un
servicio en un mes.** De ahí se derivan las tres salidas que hoy se hacen a mano.

```
Escuela ──┬── nivel(es): preescolar / primaria
          └── modo de cobro: directo   (concentrado reservado, sin usar)

Tutor ──── Niño ── escuela, grado, grupo

Catálogo de servicios ── tipo, nivel, precio

Menú del mes ──┬── nivel / escuela
               ├── fecha de corte: día 5
               └── penalización: porcentaje | monto fijo

INSCRIPCIÓN  =  niño × servicio × mes        ← la pieza central
      │         (+ los dos días elegidos, si el servicio es taller)
      │
      ├──→ Cobro            (monto + comisión + penalización si entró tarde)
      ├──→ Lista de cafetería   (por escuela, por día, con nombres)
      └──→ Conteos de cocina    (por escuela, por servicio, por día de la semana)
```

Si esa pieza está bien modelada, las tres salidas son consultas.

**El detalle que no se puede simplificar:** como cada papá elige libremente los dos días
del taller de su hijo, el conteo de ese servicio se calcula por día de la semana y no
como un total mensual repartido. Un servicio de taller con 100 niños puede producir
conteos muy distintos entre lunes y viernes.

---

## 9. El ciclo mensual

1. Healthy Tummies publica el menú del mes siguiente
2. La escuela lo circula entre los papás
3. Los papás se inscriben y pagan, hasta la **fecha de corte**
4. Se cierra el mes
5. Se generan listas de cafetería y conteos de cocina
6. Operación diaria: la cocina produce contra conteos, la cafetería entrega contra lista
7. Altas posteriores al corte entran con penalización

---

## 10. Fases siguientes

**Fase 2 — Portales.** Acceso propio para la escuela (ve su lista, marca entregas) y
para la cocina (ve sus conteos, confirma producción). Sustituye los exportables por
pantallas en vivo.

**Fase 3 — Madurez.** Constructor de menús con ciclos y repetición, reportes de consumo
y merma, facturación CFDI, y conciliación automática con el banco.

---

## 11. Riesgos

**Datos de menores.** El sistema almacena nombres de niños y las escuelas a las que
asisten. En México eso exige aviso de privacidad y cuidado con quién ve qué.
Declararlo en la propuesta juega a favor de monclair: casi nadie lo hace.

**Alta con el PSP.** El contrato y la cuenta bancaria son trámite del cliente, no de
monclair, y puede tardar más que el desarrollo mismo. Debe quedar como dependencia
explícita, con el riesgo de calendario a cargo del cliente.

**Reglas sin definir.** Si el cliente no cierra el monto de la penalización y la
política de bajas de cara al papá, el pago en línea le va a generar reclamos que hoy no
tiene.

**Cliente indeciso.** No sabe qué quiere. Riesgo real de que el alcance se mueva durante
el proyecto. Mitigación: la Fase 1 está escrita con un "fuera de alcance" explícito, y
los cambios se cotizan aparte.

---

## 12. Entregables de esta semana

**Diagnóstico del proceso actual.** Documento corto con el mapa del flujo de hoy y dónde
se fuga tiempo y riesgo. Es el documento que hace que el cliente *sienta* el problema
antes de ver el precio.

**Propuesta.** En español, Markdown → PDF. Estructura: resumen ejecutivo → entendimiento
del negocio → solución por fases → comparación honesta contra la opción no-code → qué NO
incluye → supuestos y dependencias del cliente → tiempos → inversión → siguientes pasos.

**Prototipo clickeable.** Publicado como Artifact: un link que se abre en la junta desde
cualquier laptop, sin instalar nada. Alrededor de 7 pantallas de alta fidelidad,
navegables pero no funcionales:

1. Sitio público con el menú del mes
2. Alta de tutor e hijos
3. Selección de servicio por niño
4. Pago, con comisión desglosada
5. Confirmación y recibo
6. Panel de Healthy Tummies con inscripciones por escuela
7. Las dos salidas impresas: lista de cafetería y conteos de cocina

---

## 13. Estimación de esfuerzo e inversión

> **Cómo leer esto.** Los rangos de precio son una estimación razonada a partir del
> tamaño del alcance y de tarifas típicas de desarrollo a la medida en México — **no son
> investigación de mercado ni las tarifas de monclair.** Luis debe validarlos contra su
> propio costo por semana antes de que entren a la propuesta. La estimación de esfuerzo
> es la parte defendible; el precio sale de multiplicarla por su tarifa.

### Esfuerzo de la Fase 1

| Componente | Semanas-persona |
|---|---|
| Infraestructura, despliegue y autenticación de tutores | 1.0 |
| Catálogo: escuelas, niveles, servicios, precios, talleres | 0.5 |
| Alta de tutor e hijos, inscripción por servicio y mes | 1.0 |
| Integración con el PSP, flujo de pago y estados | 1.0 |
| Panel de administración de Healthy Tummies | 1.5 |
| Generación y envío de listas y conteos (PDF y hoja) | 1.0 |
| Sitio público y menú del mes | 0.75 |
| QA, ajustes, despliegue y capacitación | 1.0 |
| **Total** | **≈ 7.75, con rango de 6 a 9** |

### Rangos sugeridos

| Concepto | Esfuerzo | Rango sugerido (MXN) |
|---|---|---|
| Fase 1 | 6–9 semanas | $180,000 – $320,000 |
| Fase 2 — portales | 3–4 semanas | $90,000 – $160,000 |
| Fase 3 — madurez | 4–6 semanas | $120,000 – $240,000 |
| Mantenimiento mensual | — | $6,000 – $12,000 / mes |

**Costos de terceros, a cargo del cliente:** comisión del PSP (≈3.6% + IVA por
transacción, que aquí absorbe el papá), hosting (≈$500–$1,500/mes a este volumen) y
dominio.

---

## 14. Plan de la semana

| Día | Trabajo |
|---|---|
| Lunes 21 | Diagnóstico del proceso actual |
| Martes 22 – Miércoles 23 | Prototipo clickeable |
| Jueves 24 | Propuesta completa, con números |
| Viernes 25 | Revisión, exportación a PDF y ensayo de la presentación |

---

## 15. Decisiones que no se tomaron aquí

- El precio final. Los rangos son referencia; los define Luis.
- El stack técnico. Se decide si el proyecto se gana, no antes.
- El monto de la penalización y la política de bajas de cara al papá. Son del cliente.
