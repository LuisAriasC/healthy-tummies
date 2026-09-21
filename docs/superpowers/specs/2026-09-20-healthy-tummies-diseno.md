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

> ⚠️ **Sin confirmar:** que el Lunch de primaria ($1,200) sea más barato que el de
> preescolar ($1,250). Se preguntó dos veces y quedó sin respuesta. Verificar antes de
> que entre al prototipo o a la propuesta.

### El flujo de dinero es mixto

El cobro **depende de cada escuela**, y esto es una restricción dura del diseño:

- **Modo directo:** el papá le transfiere a Healthy Tummies y manda comprobante.
- **Modo concentrado:** la escuela le cobra al papá y le paga a Healthy Tummies un
  consolidado. Healthy Tummies no trata dinero con el papá.

Cualquier sistema tiene que convivir con los dos desde el primer día.

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
| Alta a media de mes | Sin prorrateo. Se cobra una **penalización** |
| Bajas | Sin devolución |
| Ausencias del niño | Se pierden. No se reponen ni se acreditan |
| Comisión del PSP | La absorbe **el papá** |
| Taller 2x/semana | Dos días cualesquiera de la semana |

**Consecuencia técnica importante, y es buena noticia para el costo:** sin prorrateo,
sin reembolsos y sin reposiciones, el cobro es un cargo mensual simple. No hay lógica
de créditos, devoluciones parciales ni saldos a favor — que es exactamente donde este
tipo de sistemas se vuelve caro y lento. Vale la pena decírselo al cliente: sus propias
reglas le están abaratando el desarrollo.

**Consecuencia en la interfaz:** como el papá absorbe la comisión, el precio en
pantalla no es $1,250 — es $1,250 más comisión, desglosada a la vista. Debe aparecer
así en el prototipo.

---

## 5. Supuestos abiertos — preguntas para el cliente

Nada de esto se debe inventar. Va como lista para la junta:

1. **¿De cuánto es la penalización** por alta a media de mes? El sistema la cobra
   automáticamente, así que necesita un monto o una fórmula.
2. **Los dos días del taller: ¿los define el taller o los elige el papá?** Se asume que
   los define el taller — el niño asiste a un taller que cae, por ejemplo, martes y
   jueves, y come esos días. Si el papá los escoge libremente, cambia el modelo de datos
   y la pantalla de inscripción.
3. **Facturación / CFDI:** ¿Healthy Tummies factura al papá, a la escuela, o a ambos
   según el modo de cobro de esa escuela?
4. **Fecha de corte mensual:** ¿hasta cuándo puede inscribirse un papá para el mes
   siguiente?
5. **¿Qué escuelas están en modo directo y cuáles en modo concentrado, hoy?**
6. **PSP:** ¿ya tienen cuenta con alguno (Stripe, Mercado Pago, Conekta)? ¿Con qué banco
   está la cuenta de la empresa?
7. **Volumen real:** número de niños inscritos por escuela y por servicio. Sirve para
   dimensionar y para cuantificar el ahorro en el diagnóstico.

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
- **Dos modos de inscripción, configurables por escuela:**
  - *Modo directo* — el papá se inscribe y paga en línea
  - *Modo concentrado* — el papá se inscribe pero no paga; queda como inscrito y
    Healthy Tummies concilia con la escuela por fuera
- Pago en línea del mes, con la comisión desglosada a la vista
- Confirmación y recibo

### De cara a Healthy Tummies

- Panel de administración: escuelas, precios, talleres, niños, inscripciones, estado de pago
- Carga del menú del mes
- Generación automática de la **lista de cafetería**, por escuela y día, con nombres
- Generación automática de los **conteos de cocina**, por escuela, servicio y día
- Entrega de ambos por correo o descarga, en PDF y hoja de cálculo

### Fuera de alcance de la Fase 1

Debe decirse explícitamente en la propuesta, para que nadie lo dé por hecho:

- Portales con acceso propio para escuela y cocina
- Constructor de menús (en Fase 1 el menú se carga como archivo)
- Facturación / CFDI
- Aplicación móvil
- Conciliación automática con el banco

---

## 8. Modelo conceptual

Todo el sistema gira alrededor de **una sola unidad: la inscripción de un niño a un
servicio en un mes.** De ahí se derivan las tres salidas que hoy se hacen a mano.

```
Escuela ──┬── nivel(es): preescolar / primaria
          ├── modo de cobro: directo | concentrado
          └── talleres ── días de la semana

Tutor ──── Niño ── escuela, grado, grupo

Catálogo de servicios ── tipo, nivel, precio

INSCRIPCIÓN  =  niño × servicio × mes        ← la pieza central
      │
      ├──→ Cobro            (monto + comisión + penalización si aplica)
      ├──→ Lista de cafetería   (por escuela, por día, con nombres)
      └──→ Conteos de cocina    (por escuela, por servicio, por día)
```

Si esa pieza está bien modelada, las tres salidas son consultas.

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
