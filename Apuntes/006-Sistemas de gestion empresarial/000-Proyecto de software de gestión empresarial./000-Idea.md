Excelente elección. El alquiler por habitaciones (*coliving*) tiene una lógica de negocio más compleja y dinámica que el alquiler tradicional, lo que lo hace un proyecto perfecto para lucirte sin ser imposible de programar.

Vamos a llamar al proyecto **"RoomiePro"**. Aquí tienes el desarrollo funcional y la arquitectura del negocio.

### 1. La Jerarquía de Datos (El esqueleto)

A diferencia de una inmobiliaria normal, aquí no alquilas "casas", gestionas "espacios". Tu sistema debe entender esta jerarquía:

* **Nivel 1: La Unidad Inmobiliaria (El Piso).** Es el contenedor. Tiene gastos fijos (comunidad, IBI, Internet).
* **Nivel 2: La Unidad de Negocio (La Habitación).** Es lo que genera dinero. Tiene su propio precio y características (baño privado, exterior, cama doble).
* **Nivel 3: El Cliente (El Inquilino).** No se vincula al piso, se vincula a la habitación mediante un contrato temporal.

### 2. El Flujo de Trabajo Principal (Workflow)

Imagina el ciclo de vida de un usuario en tu software:

#### A. Fase de Configuración (Setup)

El propietario da de alta el **Piso C/ Colón 32**. El sistema le pide definir:

* Cuántas habitaciones tiene.
* Cómo se reparten los gastos (¿Por cabeza o por habitación?).
* Día de cobro (ej. día 1 de cada mes).

#### B. Fase de Entrada (Check-in)

Llega un estudiante. El software registra:

1. **Datos personales:** DNI, teléfono, contacto de emergencia.
2. **Asignación:** Se le vincula a la "Habitación 2".
3. **Fianza:** Se registra la entrada de dinero (ej. 500€) en una cuenta de "Pasivo" (dinero que no es tuyo, es deuda con el inquilino).
4. **Generación de Contrato:** El sistema genera un PDF (o texto) con fechas de inicio y fin.

#### C. Fase Mensual (El motor financiero)

Aquí está la magia. Cada mes, el sistema debe ejecutar dos procesos:

1. **El Cargo de Alquiler:** Genera automáticamente la deuda del alquiler base para todos los inquilinos activos.
2. **El Prorrateo de Suministros (La clave del negocio):**
* Llega la factura de la luz del piso (120€).
* El usuario (Admin) introduce el importe en el software.
* El sistema mira **quién estaba activo** en ese periodo.
* **Cálculo:** Si hay 4 habitaciones ocupadas, divide 120€ / 4 = 30€.
* Se suma ese cargo extra de 30€ a la cuenta de cada inquilino.



#### D. Fase de Salida (Check-out)

Cuando el inquilino se va, el sistema debe:

1. Revisar si tiene facturas pendientes (luz, agua) que aún no han llegado.
2. Permitir descontar dinero de la fianza por "Daños" o "Limpieza final".
3. Liberar la habitación para que pase a estado "Disponible" inmediatamente.

### 3. Funcionalidades Diferenciales (Valor añadido)

Si quieres que este software sea vendible a futuro, añade estas lógicas:

* **Gestión de "Parejas":**
Si en una habitación doble entra una pareja, el alquiler es el mismo, pero los gastos (luz/agua) **se duplican** en el reparto. Tu software debe saber diferenciar "Precio Habitación" de "Coste por Persona".
* **Control de Llaves:**
Un registro simple de quién tiene llaves de qué puertas (portal, casa, habitación).
* **Alertas de Renovación:**
En alquiler por habitaciones, la rotación es alta (estudiantes que se van en junio). El sistema debe avisar 30 días antes: *"El contrato de Juan termina pronto. ¿Renovar o publicar anuncio?"*.
* **Histórico de Rentabilidad:**
Un reporte que diga: "La Habitación 1 ha generado 4.000€ este año con una ocupación del 90%".

### 4. Resumen de Módulos para tu Menú Principal

Pensando en tu interfaz de consola o web simple:

1. **Dashboard:** (Resumen: Habitaciones ocupadas vs libres, Cobros pendientes este mes).
2. **Inmuebles:** (Alta de pisos y definición de habitaciones).
3. **Inquilinos:** (Alta, Baja, Historial).
4. **Contratos:** (Vincular Inquilino <-> Habitación).
5. **Tesorería:**
* Registrar Gasto (Luz/Agua del piso).
* Registrar Cobro (Inquilino paga renta).
* Generar Recibos.

