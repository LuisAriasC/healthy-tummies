> **NOTA INTERNA — BORRAR ANTES DE ENVIAR.** La sección 8 usa una calibración de
> **2.0 horas por punto** y una tarifa de **$550/hora**, que dan $310,000 para la Fase 1.
> Son supuestos míos, no tus números. Ajústalos en la calculadora y sustituye los montos
> de la sección 8 y del calendario de pagos. Todo lo demás del documento no depende del
> precio.

---

# Plataforma de inscripción y cobro

### Propuesta para Healthy Tummies

**Preparada por monclair** · septiembre de 2026
**Vigencia de esta propuesta: 30 días naturales**

---

## 1. Resumen

Healthy Tummies verifica a mano, contra comprobantes bancarios, quién pagó cada servicio
de cada niño de cada escuela cada mes. De esa verificación manual dependen las listas de
la cafetería y los conteos de la cocina.

Estimamos que ese proceso cuesta **entre 4.9% y 5.9% del ingreso de cada servicio**, y que
el costo crece en línea recta conforme crecen los alumnos: hoy, la cuarta escuela cuesta
administrativamente lo mismo que costó la primera.

Proponemos una plataforma en dos partes. Los papás se inscriben y pagan en línea; Healthy
Tummies administra escuelas, servicios y menús, y recibe cada día la lista de la cafetería
y la orden de producción de la cocina, generadas solas.

| | |
|---|---|
| **Inversión Fase 1** | $310,000 MXN + IVA |
| **Plazo** | 16 semanas a partir del anticipo |
| **Recuperación estimada** | 10 a 11 meses |
| **Prototipo navegable** | 35 pantallas, disponible para revisar hoy |

Ya construimos el prototipo completo. No es una idea: es un producto diseñado pantalla por
pantalla, que puede abrirse desde cualquier navegador antes de aprobar un solo peso de
desarrollo.

---

## 2. Lo que entendimos de su operación

Healthy Tummies arma un menú mensual, lo envía a las escuelas, cada escuela lo circula
entre sus papás, y los papás deciden si contratan. Todo se cocina en una cocina central
por día y por servicio, se distribuye a cada escuela, y en la cafetería se entrega al niño.

La información vive hoy en tres lugares que no se hablan entre sí:

| Quién | Qué sabe |
|---|---|
| Cocina central | Cuántas órdenes produce, por servicio y escuela |
| Cafetería de la escuela | A qué niños les toca entregar |
| Healthy Tummies | Quién pagó — verificado a mano |

**Reglas que respetamos tal como operan hoy:** corte el día 5, recargo a quien se inscriba
después, sin prorrateo, sin devoluciones, sin reposición por ausencia, y la comisión del
procesador a cargo del papá. La plataforma no les pide cambiar su forma de trabajar.

---

## 3. Lo que cuesta el proceso actual

Por cada **100 alumnos inscritos en un servicio, en una escuela, durante un mes**:

| Servicio | Ingreso | Costo del proceso manual | % |
|---|---:|---:|---:|
| Preescolar · Lunch | $125,000 | $6,265 | 5.0% |
| Preescolar · Comida | $125,000 | $6,265 | 5.0% |
| Preescolar · Taller 2x | $55,000 | $3,245 | 5.9% |
| Primaria · Lunch | $120,000 | $6,075 | 5.1% |
| Primaria · Comida | $135,000 | $6,645 | 4.9% |
| Primaria · Taller 2x | $60,000 | $3,435 | 5.7% |
| Primaria · Almuerzo | $135,000 | $6,645 | 4.9% |

Ese costo se reparte en tres fugas: **horas administrativas** (≈17 al mes por cada 100
alumnos en un servicio), **servicio entregado por error**, y **servicio entregado que
nunca se cobró** — la más grande de las tres y consecuencia directa de verificar a mano.

> **La cifra que solo ustedes conocen.** Modelamos el servicio no cobrado en 3% del
> ingreso, un supuesto conservador para un proceso manual. Si el número real es 1%, el
> proyecto se justifica igual pero más lento; si es 6%, se paga solo en medio año. Es la
> primera pregunta que querríamos resolver con ustedes.

El documento *Diagnóstico del proceso actual* acompaña esta propuesta con el desglose
completo y los supuestos de cada cifra.

---

## 4. Lo que proponemos construir

### Para los papás

- Acceso sin contraseña, con Google, Microsoft o enlace por correo
- Alta de sus hijos, con verificación de nombre y matrícula contra el padrón de la escuela
- Menú del mes, publicado por servicio
- Selección de servicios por hijo, con el precio que corresponde a su grado, incluida la
  elección de los dos días en los servicios por taller
- Pago en línea por transferencia SPEI o tarjeta, con la comisión desglosada a la vista
- Confirmación, historial de pagos y detalle de cada cobro

Un solo tutor, una sola cuenta y un solo pago mensual, aunque tenga hijos en escuelas
distintas.

### Para Healthy Tummies

- Alta y edición de escuelas, cada una con su enlace propio para circular entre los papás
- Carga del padrón de alumnos de cada escuela
- Catálogo de servicios y precios por grado, con vigencia mensual
- Carga del menú del mes y configuración del corte y el recargo
- **Conciliación automática de los pagos SPEI**, sin revisar un solo comprobante
- Panel de inscripciones y panel de pagos, con las excepciones que no cuadran a la vista
- **Lista de cafetería** por escuela y día, generada y enviada sola cada mañana
- **Orden de producción de cocina** por día, con las tres escuelas juntas, respetando los
  días que eligió cada papá en los servicios por taller

### Por qué cobrar por SPEI

En transferencia SPEI la comisión es **fija**: $8.12 por pago, contra $48 que cuesta la
misma operación con tarjeta en un servicio de $1,250. Como la comisión la absorbe el papá,
esa diferencia es dinero que se le devuelve.

Y el argumento de fondo no es el precio: **los papás ya pagan por transferencia hoy.**
Cobrar por SPEI no les cambia el hábito. Lo único que cambia es que el pago llega
identificado y conciliado solo, en lugar de llegar como un comprobante que alguien revisa
a mano.

---

## 5. Lo que esta fase NO incluye

Lo decimos explícitamente para que nadie lo dé por supuesto. Todo esto es **Fase 2** y se
cotiza por separado:

- **Facturación.** Healthy Tummies seguirá facturando a papás y escuelas por fuera del
  sistema, exactamente como hoy. Ni se capturan datos fiscales ni se emite el CFDI
- **Portales con acceso propio para las escuelas y para la cocina.** En la Fase 1 ambas
  reciben su hoja por correo cada día, como hasta ahora, pero correcta y al día
- **Lectura automática del archivo del menú**, y con ella el menú del día dentro de la app
  del papá. En la Fase 1 el archivo se publica para que el papá lo abra
- **Cobro concentrado por la escuela.** Hoy las tres escuelas cobran en directo
- **Aplicación móvil nativa.** La plataforma funciona en el navegador del teléfono
- Reportes de consumo y merma, y conciliación automática con el banco (Fase 3)

---

## 6. Alternativas que evaluamos

| Opción | Qué es | Por qué no la recomendamos |
|---|---|---|
| **Armarlo con herramientas existentes** | Links de pago, una base tipo Airtable y automatizaciones | Se levanta en dos semanas y cuesta una fracción. Pero el costo recurrente crece por usuario, la operación queda partida entre varias herramientas, y se rompe justo cuando el negocio crezca. Es una opción razonable si el objetivo fuera validar; con la operación ya funcionando, no lo es |
| **Construir todo de una vez** | Incluir desde el arranque los portales de escuela y cocina | Lo caro no son los datos, son los portales con sus accesos y permisos. A tres escuelas, la persona de la cafetería probablemente prefiere su hoja impresa antes que aprender un sistema |
| **Lo que proponemos** | Construir bien la superficie donde entra el dinero; hacia adentro, salidas automáticas | Entrega el mismo valor operativo con bastante menos que construir, y deja el camino abierto para los portales cuando las escuelas lo pidan |

---

## 7. Lo que necesitamos de Healthy Tummies

El calendario depende de estos cuatro puntos. Conviene empezarlos antes de que arranque el
desarrollo:

1. **El padrón de alumnos de cada escuela**, con matrícula y nombre completo, en Excel o
   CSV. Sin él, las altas de los papás no se pueden verificar. Conseguirlo es una
   conversación de Healthy Tummies con cada escuela
2. **La cuenta con el procesador de pagos** (Stripe o el que prefieran) y la cuenta
   bancaria de la empresa. El trámite puede tardar más que el desarrollo
3. **El aviso de privacidad**, redactado por su abogado. El sistema guarda nombres de
   menores y sus alergias, lo que en México exige aviso y consentimiento del tutor
4. **Los archivos del menú mensual**, en el formato que ya producen

También necesitamos una persona de su lado disponible para resolver dudas durante el
proyecto, y las decisiones pendientes: el monto exacto del recargo y el volumen real de
inscripciones por escuela y servicio.

---

## 8. Inversión

| Concepto | Monto |
|---|---:|
| **Fase 1 — plataforma de inscripción, cobro y operación** | **$310,000 MXN** |
| Fase 2 — portales, lectura de menús y facturación CFDI | $85,000 MXN |
| Mantenimiento y soporte mensual, a partir de la entrega | $8,000 MXN / mes |

Los montos no incluyen IVA.

**Calendario de pagos de la Fase 1**

| Momento | % | Monto |
|---|---:|---:|
| A la firma | 40% | $124,000 |
| A la mitad del plazo, con el cobro funcionando | 30% | $93,000 |
| A la entrega y puesta en marcha | 30% | $93,000 |

**Costos de terceros, a cargo de Healthy Tummies:** comisión del procesador (≈3.6% + IVA
con tarjeta, $8.12 por transferencia SPEI — que en este modelo absorbe el papá), hosting
(aproximadamente $500 a $1,500 al mes a este volumen) y dominio.

---

## 9. Plazo y forma de trabajo

**16 semanas** a partir del anticipo, con entregas parciales revisables:

| Semanas | Entregable revisable |
|---|---|
| 1 – 4 | Catálogo funcionando: escuelas, padrones, servicios y precios |
| 5 – 9 | Los papás pueden inscribirse y pagar; conciliación SPEI operando |
| 10 – 13 | Listas de cafetería y órdenes de cocina generándose y enviándose |
| 14 – 16 | Pruebas con una escuela real, ajustes, capacitación y arranque |

Cada bloque termina con algo que se puede abrir y usar. No hay un único momento de entrega
al final.

Recomendamos **arrancar con una sola escuela** durante el primer mes de operación, y sumar
las otras dos una vez que el ciclo completo —inscripción, cobro, lista y producción— haya
corrido bien un mes entero.

---

## 10. Después de la entrega

El mantenimiento mensual cubre hospedaje, respaldos, monitoreo, correcciones y soporte
para la operación. No incluye desarrollo de funciones nuevas, que se cotizan aparte.

La plataforma queda a nombre de Healthy Tummies: el código, los datos y las cuentas de
servicio son suyos.

---

## 11. Siguientes pasos

1. **Revisar el prototipo juntos.** Está listo y se abre desde cualquier navegador. Es la
   forma más rápida de confirmar que entendimos su operación
2. **Resolver las cuatro preguntas abiertas** de la sección 7
3. **Firmar y arrancar.** Con el anticipo comenzamos de inmediato; el padrón y la cuenta
   del procesador pueden ir avanzando en paralelo

---

**monclair**
Luis Carlos Arias Camacho
luis.carlos.arias.camacho@gmail.com
