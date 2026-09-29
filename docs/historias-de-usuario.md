# Historias de usuario

Inventario completo del alcance, derivado pantalla por pantalla del prototipo. Es la base
sobre la que se calculó la estimación: cada historia tiene puntos de esfuerzo, y de la suma
sale el precio.

**Cómo leer los puntos.** Miden tamaño relativo, no horas. Una historia de 8 es cuatro veces
una de 2. Estimar en relativo es más confiable que estimar en horas porque no arrastra
optimismo; la conversión a horas se hace después, una sola vez, con un factor calibrado.

| Puntos | Equivale más o menos a |
|---:|---|
| 1 | Algo trivial |
| 2 | Un rato |
| 3 | Media jornada |
| 5 | Una jornada |
| 8 | Dos o tres jornadas |
| 13 | Una semana, y trae riesgo |

**Actores:** el **tutor** (papá o mamá que contrata), **Healthy Tummies** (quien opera el
negocio), la **escuela** y la **cocina central**. En la Fase 1 escuela y cocina no entran al
sistema: reciben sus hojas por correo.

---

## Fase 1 — 40 historias · 214 puntos

### Base técnica y accesos · 37 puntos

| # | Historia | Puntos |
|---|---|---:|
| **HT-01** | Como equipo, necesitamos el proyecto, los entornos, el despliegue continuo y el monitoreo en pie, para poder entregar cambios sin romper lo que ya funciona. | 8 |
| **HT-02** | Como equipo, necesitamos el modelo de datos y sus migraciones, para que inscripciones, cobros y salidas operativas compartan una sola fuente de verdad. | 8 |
| **HT-03** | Como tutor, quiero entrar con un enlace que llega a mi correo, para no inventar ni recordar otra contraseña. | 5 |
| **HT-04** | Como tutor, quiero entrar con mi cuenta de Google, para no escribir nada. | 3 |
| **HT-05** | Como tutor, quiero entrar con mi cuenta de Microsoft, porque es la que ya uso con el colegio. | 3 |
| **HT-06** | Como tutor nuevo, quiero dar mis datos una sola vez y aceptar el aviso de privacidad, para empezar a inscribir a mis hijos. | 3 |
| **HT-07** | Como Healthy Tummies, quiero que cada persona del equipo entre con su propia cuenta, para saber quién hizo cada movimiento. | 5 |
| **HT-08** | Como persona del equipo, quiero recuperar mi contraseña sin depender de alguien más, para no quedarme fuera del panel. | 2 |

> **HT-06 no es opcional.** El sistema guarda nombres de menores y sus alergias, lo que en
> México exige aviso de privacidad y consentimiento del tutor. Sin esa casilla no se pueden
> guardar los datos del niño.

### Catálogo · 42 puntos

| # | Historia | Puntos |
|---|---|---:|
| **HT-09** | Como Healthy Tummies, quiero dar de alta una escuela y obtener su enlace propio, para que la escuela lo circule entre sus papás. | 5 |
| **HT-10** | Como Healthy Tummies, quiero cargar el padrón de alumnos de cada escuela, para poder verificar que un tutor da de alta a un niño que sí estudia ahí. | 8 |
| **HT-11** | Como Healthy Tummies, quiero desactivar una escuela sin borrarla, para conservar sus pagos y facturas y seguir sirviendo el mes ya cobrado. | 3 |
| **HT-12** | Como Healthy Tummies, quiero administrar los servicios y sus precios por grado, para que cada tutor vea el catálogo que le corresponde. | 5 |
| **HT-13** | Como Healthy Tummies, quiero que un cambio de precio aplique hasta el mes siguiente, para que a quien ya pagó no se le altere su monto. | 5 |
| **HT-14** | Como Healthy Tummies, quiero desactivar un servicio sin borrarlo, para dejar de ofrecerlo sin afectar a quienes ya lo pagaron. | 3 |
| **HT-15** | Como Healthy Tummies, quiero subir el menú del mes y marcar a qué servicios aplica, para publicarlo tal como ya lo produzco. | 5 |
| **HT-16** | Como Healthy Tummies, quiero fijar la fecha de corte y el recargo de cada mes, para que el sistema cobre solo a quien se inscriba tarde. | 5 |
| **HT-17** | Como Healthy Tummies, quiero que el sistema no me deje publicar un mes incompleto, para que ningún tutor vea una oferta a medias. | 3 |

> **HT-10 depende de un tercero.** El padrón no lo genera la plataforma: cada escuela tiene
> que entregarlo, con matrícula y nombre completo. Es la dependencia externa que más puede
> retrasar el arranque.

### Inscripción · 36 puntos

| # | Historia | Puntos |
|---|---|---:|
| **HT-18** | Como tutor, quiero dar de alta a mi hijo con su nombre y matrícula, para que el sistema confirme contra la lista de la escuela que es correcto. | 8 |
| **HT-19** | Como tutor, quiero corregir los datos de mi hijo o darlo de baja, sin llamar a nadie. | 3 |
| **HT-20** | Como tutor, quiero ver el menú del mes, tanto el de los servicios que ya contraté como el catálogo completo, para decidir con información. | 5 |
| **HT-21** | Como tutor, quiero elegir los servicios de cada hijo y ver su precio, para saber cuánto voy a pagar antes de comprometerme. | 5 |
| **HT-22** | Como tutor, quiero elegir los dos días de la semana en los servicios por taller, porque dependen del taller al que va mi hijo. | 5 |
| **HT-23** | Como tutor, quiero que lo que elijo se guarde sin pagar todavía, para capturar a mis hijos en distintos momentos y pagar todo junto. | 5 |
| **HT-24** | Como tutor, quiero que la pantalla de inicio me diga en qué estado estoy —sin hijos, sin servicios, sin pagar, o al día—, para saber qué me falta. | 5 |

> **HT-22 es la historia con más consecuencias.** Que cada tutor elija libremente sus dos
> días convierte el conteo de la cocina en un cálculo por día de la semana, en lugar de un
> número mensual. Es lo que hace imposible llevarlo a mano.

### Cobro · 47 puntos

| # | Historia | Puntos |
|---|---|---:|
| **HT-25** | Como tutor, quiero pagar por transferencia SPEI con una referencia única, para pagar como siempre lo he hecho y que se registre solo. | 13 |
| **HT-26** | Como tutor, quiero pagar con tarjeta si lo prefiero, viendo cuánto más me cuesta esa comisión. | 5 |
| **HT-27** | Como tutor, quiero ver el desglose de lo que pago —servicios, recargo si entré tarde, comisión—, para entender el total. | 5 |
| **HT-28** | Como Healthy Tummies, quiero que el pago acreditado inscriba al niño automáticamente, para dejar de revisar comprobantes a mano. | 8 |
| **HT-29** | Como tutor, quiero una confirmación y un comprobante de mi pago, para tener constancia. | 3 |
| **HT-30** | Como tutor, quiero ver mis pagos anteriores agrupados por ciclo escolar y abrir el detalle de cualquiera, para resolver mis dudas sin llamar. | 5 |
| **HT-31** | Como Healthy Tummies, quiero ver los pagos que no cuadran —sin referencia, con monto distinto—, para resolverlos en lugar de que se pierdan. | 8 |

> **HT-25 es la historia más riesgosa del proyecto.** Es la única de 13 puntos: depende de un
> tercero, de un trámite bancario y de un flujo asíncrono. Si algo se atrasa, se atrasa aquí.

### Operación · 31 puntos

| # | Historia | Puntos |
|---|---|---:|
| **HT-32** | Como cafetería de la escuela, quiero recibir cada mañana la lista de a quién entregar, para no depender de que alguien la arme. | 8 |
| **HT-33** | Como cocina central, quiero recibir la orden de producción del día con todas las escuelas juntas, para cocinar una sola vez. | 8 |
| **HT-34** | Como Healthy Tummies, quiero esas salidas en PDF y hoja de cálculo, para imprimirlas o trabajarlas. | 5 |
| **HT-35** | Como Healthy Tummies, quiero que se envíen solas a la hora acordada, para no tener que acordarme cada día. | 5 |
| **HT-36** | Como Healthy Tummies, quiero ver las inscripciones del mes filtradas por escuela y estado, para saber cómo va el mes. | 5 |

> **HT-32 y HT-33 tienen unidades distintas.** La lista de cafetería es por escuela y por día,
> porque cada escuela entrega la suya. La orden de cocina es por día con todas las escuelas
> juntas, porque la cocina central cuece una sola vez para todos.

### Transversales · 21 puntos

| # | Historia | Puntos |
|---|---|---:|
| **HT-37** | Como usuario de cualquiera de las dos aplicaciones, quiero una interfaz cuidada y que funcione en el teléfono, porque la mayoría de los tutores entra desde ahí. | 8 |
| **HT-38** | Como tutor, quiero que me avisen del corte, del menú nuevo y de mi pago acreditado, para no perder la fecha. | 5 |
| **HT-39** | Como Healthy Tummies, necesitamos el aviso de privacidad y el manejo correcto de datos de menores, para cumplir con la ley. | 3 |
| **HT-40** | Como usuario, quiero que las pantallas vacías y los errores me digan qué hacer, en lugar de dejarme sin salida. | 5 |

---

## Fase 2 — 7 historias · 58 puntos

No entran en el precio de la Fase 1. En el prototipo aparecen marcadas en naranja.

| # | Historia | Puntos |
|---|---|---:|
| **F2-01** | Como escuela, quiero entrar al sistema para ver mi lista del día y marcar las entregas, en lugar de trabajar sobre una hoja impresa. | 13 |
| **F2-02** | Como cocina, quiero entrar al sistema para ver mis conteos y confirmar la producción. | 8 |
| **F2-03** | Como Healthy Tummies, quiero que el sistema lea y valide el calendario en Excel, para que me avise si falta un día antes de publicar. | 8 |
| **F2-04** | Como tutor, quiero ver en la app qué come mi hijo hoy, para no abrir un archivo. | 5 |
| **F2-05** | Como tutor, quiero capturar mis datos fiscales en mi cuenta, para recibir mi factura sin pedirla por correo. | 3 |
| **F2-06** | Como Healthy Tummies, quiero emitir el CFDI automáticamente a tutores y escuelas, para dejar de facturar a mano. | 13 |
| **F2-07** | Como escuela, quiero concentrar el cobro de mis papás y pagar un consolidado, porque así manejo yo la relación de cobranza. | 8 |

> **F2-04 depende de F2-03.** Mientras el menú sea un archivo que el sistema no abre, no hay
> forma de saber qué platillo toca cada día.

---

## Fuera de alcance de ambas fases

- Aplicación móvil nativa. Las dos aplicaciones funcionan en el navegador
- Reportes de consumo y merma
- Conciliación automática contra el estado de cuenta bancario
- Prorrateo, devoluciones o reposición por ausencia — el negocio opera sin ellos

---

## Totales

| | Historias | Puntos |
|---|---:|---:|
| Fase 1 | 40 | **214** |
| Fase 2 | 7 | **58** |
