# Healthy Tummies · Plataforma de inscripción y cobro

Propuesta de plataforma para una empresa mexicana de catering escolar que da servicio de
alimentos en escuelas de preescolar y primaria.

Este repositorio no contiene la aplicación: contiene el **trabajo previo a construirla** —
el diagnóstico del proceso actual, un prototipo navegable de 35 pantallas, el inventario de
historias de usuario y el modelo con el que se calculó el precio.

## Enlaces

| | |
|---|---|
| **Prototipo navegable** · 35 pantallas | https://claude.ai/artifact/WEAsbYc22FXDJBjf51JPfN |
| **Calculadora de estimación** · interactiva | https://claude.ai/artifact/PQkCeRdh1KEMvknb32rgYd |

> Los enlaces apuntan a artifacts privados. Para que alguien más pueda abrirlos hay que
> compartirlos desde el menú de la propia página.

## El problema

La empresa verifica **a mano**, contra comprobantes bancarios, quién pagó cada servicio de
cada niño de cada escuela cada mes. De esa verificación dependen las listas de entrega de
cada cafetería y los conteos de producción de la cocina central.

El modelo del diagnóstico estima que ese proceso cuesta **entre 4.9% y 5.9% del ingreso de
cada servicio**, repartido en tres fugas: horas administrativas, servicio entregado por
error, y servicio entregado que nunca se cobró.

## Qué hay en el repositorio

```
docs/
├── historias-de-usuario.md          47 historias con puntos de esfuerzo
├── cliente/
│   ├── diagnostico-proceso-actual.md   costo del proceso manual, por servicio
│   ├── prototipo.html                  35 pantallas navegables
│   ├── propuesta.md                    propuesta comercial
│   └── propuesta.pdf                   la misma, lista para enviar
├── interno/
│   ├── estimacion.html                 calculadora de esfuerzo y precio
│   └── build_pdf.py                    genera el PDF desde el markdown
└── superpowers/specs/
    └── 2026-09-20-...-diseno.md        documento de diseño y decisiones
```

El prototipo cubre dos aplicaciones: la del **tutor** (17 pantallas: acceso, alta de hijos,
menú, inscripción, pago y cuenta) y el **panel de operación** (18 pantallas: inscripciones,
listas, conteos, pagos y catálogos), cada una con sus estados vacíos y sus estados llenos.

---

## Cómo se calculó la estimación

El objetivo era llegar a un precio que se pudiera defender renglón por renglón, no a un
número redondo puesto a ojo.

### 1 · Inventario de historias

Cada pantalla y cada comportamiento del prototipo se convirtió en una historia de usuario.
No se estimó "la aplicación completa" ni "el módulo de pagos": se estimaron **47 historias**
concretas, 40 de la primera fase y 7 de la segunda.

El inventario vive en [`docs/historias-de-usuario.md`](docs/historias-de-usuario.md).

### 2 · Puntos de esfuerzo, no horas

Cada historia recibe puntos en escala Fibonacci —1, 2, 3, 5, 8, 13— que miden **tamaño
relativo**: una historia de 8 es cuatro veces una de 2.

Se estima en relativo, y no directamente en horas, porque comparar dos tareas entre sí es
más confiable que predecir cuánto va a tardar una en el reloj. La estimación en horas
arrastra optimismo; la relativa, mucho menos.

| Fase | Historias | Puntos |
|---|---:|---:|
| Fase 1 | 40 | **214** |
| Fase 2 | 7 | **58** |

Repartidos por épica en la Fase 1:

| Épica | Puntos |
|---|---:|
| Base técnica y accesos | 37 |
| Catálogo | 42 |
| Inscripción | 36 |
| **Cobro** | **47** |
| Operación | 31 |
| Transversales | 21 |

La épica de cobro es la más pesada, y dentro de ella una sola historia —el pago por
transferencia SPEI con conciliación automática— se lleva 13 puntos. Es la única de ese
tamaño en todo el proyecto, y la que concentra el riesgo: depende de un tercero, de un
trámite bancario y de un flujo asíncrono.

### 3 · Conversión a horas

Los puntos se multiplican por un **factor de calibración** en horas por punto. Este es el
único número que no sale del alcance sino de la experiencia de quien va a construir, y es
también el que más mueve el resultado: pasar de 2.0 a 3.0 sube el precio 50% sin que cambie
una sola historia.

La forma honesta de fijarlo es mirar un proyecto anterior y comparar los puntos que se
estimaron contra las horas que realmente se registraron.

### 4 · El trabajo que no es programar

Sobre las horas de desarrollo se suman tres porcentajes:

| Concepto | % sobre desarrollo |
|---|---:|
| QA y corrección | 15% |
| Gestión, juntas y coordinación | 12% |
| Despliegue, capacitación y arranque | 5% |

Sin estos tres, cualquier estimación se queda corta entre un 25% y un 35%. Son trabajo real
y se cobran.

### 5 · Horas por tarifa

El resultado en horas se multiplica por la tarifa. **Los puntos son la parte defendible
frente al cliente**, porque salen de pantallas que puede ver; la tarifa es interna y no se
justifica renglón por renglón.

### La aritmética completa

```
214 puntos  ×  factor de calibración      =  horas de desarrollo
horas de desarrollo  ×  1.32              =  horas totales (con QA, gestión y arranque)
horas totales  ×  tarifa por hora         =  precio
```

La calculadora permite mover el factor, la tarifa y los tres porcentajes, y **desmarcar
historias una por una** para ver cuánto baja el precio al recortar alcance — que es la
conversación que de verdad se tiene cuando un cliente dice que es mucho.

### Por qué esto es más confiable que estimar a ojo

Una estimación hecha sobre una conversación suele errar por el doble. Ésta se hizo sobre
35 pantallas que existen y que el cliente puede abrir, con el comportamiento ya definido:
qué pasa si un papá se inscribe tarde, qué pasa si desactivan una escuela a media de mes,
qué ve la cafetería de un niño sin pago confirmado.

Durante el diseño del prototipo aparecieron cuatro contradicciones en el modelo de datos
—la escuela pertenece al hijo y no al tutor, el menú es el mismo para todas las escuelas,
el conteo de talleres varía por día— que habrían costado semanas de retrabajo si se
hubieran descubierto programando.

---

## Estado

Propuesta entregada. El proyecto no está contratado ni construido.
