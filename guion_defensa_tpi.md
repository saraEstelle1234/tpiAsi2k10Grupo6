# 🎙️ Guion Oficial de Defensa Oral — TPI ASI 2K10 (Grupo 6)

> **Cátedra:** Análisis de Sistemas de Información (ASI) • Curso 2K10 • UTN FRC  
> **Caso de Estudio:** Museo de Historia Natural  
> **Modalidad:** Defensa grupal oral • Duración máxima: **15 minutos** (1:30 a 1:45 min por expositor)  
> **Expositores:** 8 integrantes activos (Agustín Cufre asume apertura y cierre/trazabilidad).

---

## 👥 Tabla Oficial de Exposición por Integrante

| N° | Orador | Legajo | Diapositiva(s) | Tema Asignado | Tiempo Estimado |
| :-: | :--- | :-: | :---: | :--- | :-: |
| **1** | **Agustín Cufre** | 419166 | **Slide 01 y 02** | **Portada, Dominio bajo estudio y Objetivos del sistema** | 1:45 min |
| **2** | **Kevin Pereyra** | 418201 | **Slide 03** | **Mapa de Procesos de Negocio (Estratégicos, Esenciales, Soporte)** | 1:30 min |
| **3** | **Tobias Molina** | 419749 | **Slide 04** | **Plantilla de Descripción de Proceso: Gestionar Incidentes** | 1:30 min |
| **4** | **Tomas Marcuzzi** | 403382 | **Slide 05 y 06** | **Modelado BPMN Nivel Descriptivo y Operativo (4 Carriles)** | 2:00 min |
| **5** | **Lucas Moyano** | 410975 | **Slide 07 y 08** | **Requerimientos Funcionales (45 RFs) y No Funcionales (2 RNFs)** | 1:45 min |
| **6** | **Francisco Thomas Rapp** | 408990 | **Slide 09** | **Diagrama de Casos de Uso General (DCU y Actores)** | 1:30 min |
| **7** | **Francisco Abad** | 423269 | **Slide 10 y 11** | **Plantilla CU-15: Registrar Incidente y Prototipo de Interfaz UI** | 1:45 min |
| **8** | **Juan Sebastián Tarditti** | 400212 | **Slide 12** | **Diagrama de Clases del Dominio (DCD y Multiplicidades)** | 1:45 min |
| **9** | **Agustín Cufre** | 419166 | **Slide 13 y 14** | **Matriz de Trazabilidad Integral, Conclusiones y Cierre** | 1:30 min |

---

## 🎙️ Guion Verbal Exacto por Expositor

---

### 1. Agustín Cufre (Slide 01 y 02 · Portada, Dominio y Objetivos)
> *"Buenas tardes profesores. Somos el Grupo 6 del curso 2K10 y hoy presentamos nuestro Trabajo Práctico Integrador: el **Sistema de Gestión y Vigilancia Museológica para el Museo de Historia Natural**.*  
> *Pasando a la **diapositiva 2**, analizamos el dominio bajo estudio. El museo tiene como misión exponer colecciones de arte y paleontología de artistas locales e internacionales, sustentándose mediante el cobro de entradas generales y el arancel optativo de visitas guiadas.*  
> *Como pueden apreciar en la **fotografía oficial de las salas de exhibición**, el museo cuenta con objetos animados y piezas de alto valor patrimonial sensibles a la temperatura, humedad e iluminación según su material. Nuestro alcance se centra en dar soporte integral a las rondas de inspección física y al congelamiento inmediato del daño cuando ocurre un incidente, asegurando la preservación del patrimonio."*

---

### 2. Kevin Pereyra (Slide 03 · Mapa de Procesos de Negocio)
> *"Buenas tardes. En la **diapositiva 3** presentamos la vista externa organizacional a través del **Mapa de Procesos**.*  
> *Clasificamos los procesos en tres niveles:*  
> *- **Estratégicos:** Planificar la programación de exposiciones, Planificar visitas guiadas, Definir precios de guía y Definir precios de entrada.*  
> *- **Esencial:** **Exponer obras de arte**, que representa la razón de ser del museo y el cliente directo de nuestro proceso de estudio.*  
> *- **Soporte:** Gestionar ingreso de obras artísticas, Administrar RRHH y **Gestionar incidentes y restauración de obras**, que es el proceso crítico que hemos analizado a fondo.*  
> *Queremos resaltar una decisión de diseño metodológica: mantuvimos 'Definir precios de guía' y 'Definir precios de entrada' como procesos separados respetando la literalidad del enunciado; sin embargo, reconocemos que en un modelo optimizado de granularidad pueden unificarse en un único proceso estratégico de 'Definir tarifas y servicios', complementado con la diagramación de horarios de guías."*

---

### 3. Tobias Molina (Slide 04 · Plantilla de Proceso de Soporte)
> *"Continuando en la **diapositiva 4**, formalizamos la **Plantilla de Descripción del Proceso de Soporte: Gestionar incidentes y restauración de obras**.*  
> *El objetivo del proceso es gestionar los incidentes y la restauración mediante rondas de vigilancia, registrando en el Módulo Web para que los supervisores resuelvan el destino de las piezas. Su cliente es el proceso esencial 'Exponer obras de arte' y su producto es el informe de salas recorridas y las obras derivadas a reparación.*  
> *En este proceso operan dos **Reglas de Negocio fundamentales**:*  
> *- **Regla 1 (Reingreso obligatorio a depósito):** Toda obra enviada a restauración, se haya podido reparar o no, debe ingresar obligatoriamente al depósito antes de definir su destino final o baja.*  
> *- **Regla 2 (Registro inmediato de incidente):** El guardia debe registrar el incidente en caliente durante la ronda, documentando fecha, hora y sala de forma inmediata.*  
> *Asimismo, formalizamos el **Listado de actividades del proceso**: 1) Realizar ronda de vigilancia, 2) Registrar incidente, 3) Generar informe con salas recorridas, 4) Registrar tipo de incidente, 5) Verificar si requiere tareas de restauración y 6) Realizar tareas de restauración, junto con las restricciones y excepciones asociadas."*

---

### 4. Tomas Marcuzzi (Slides 05 y 06 · BPMN Nivel Descriptivo y Operativo)
> *"En las **diapositivas 5 y 6** modelamos la vista interna del proceso con el estándar BPMN.*  
> *La **diapositiva 5** muestra el nivel macro descriptivo, mientras que en la **diapositiva 6** apreciamos el **BPMN a Nivel Operativo**, estructurado rigurosamente en **4 carriles funcionales**:*  
> *1. **Guardia del museo:** Inicia el turno, consulta la planificación, marca la sala con 'observación pendiente' y, si hay daño, dispara **Registrar incidente** consumiendo datos de los almacenes **Salas** y **Obras**.*  
> *2. **Admin de sistema / Encargado Web:** En este carril administrativo se realiza la tipificación del incidente (deterioro provocado, caída accidental o deterioro natural) y el sistema consulta el material de la obra para **generar la respuesta de última acción sugerida**, transicionando la obra al estado explícito **'Inactivo'**.*  
> *3. **Encargado de Supervisión:** Evalúa el informe de daño y decide si la obra requiere intervención técnica o si puede volver al estado **'Activo'**.*  
> *4. **Encargado de Restauración:** Si requiere arreglo, el flujo deriva a la actividad explícita **Restaurar obra**, asegurando el posterior reingreso a depósito bajo la Regla de Negocio 1.*  
> *Todos los cambios de estado están explícitamente rotulados hacia qué estado pasan: 'observación pendiente', 'sin novedades', 'Incidente activo', 'Inactivo' y 'Activo'."*

---

### 5. Lucas Moyano (Slides 07 y 08 · Requerimientos Funcionales y No Funcionales)
> *"En las **diapositivas 7 y 8** detallamos la especificación de requerimientos del sistema.*  
> *En la **diapositiva 7** presentamos los **45 Requerimientos Funcionales**, organizados en paquetes cohesivos: administración de obras, materiales, salas, guías, venta de entradas, programación de exposiciones, planificación de rondas y el módulo de incidentes y restauración, donde destaca el **RF-35 (Registrar incidente)**.*  
> *En la **diapositiva 8** establecemos los **dos Requerimientos No Funcionales** rectores especificados en el TPI:*  
> *- **RNF 1 – Módulo Web de Soporte:** Arquitectura cliente-servidor accesible desde navegadores web modernos sin instalación en puestos locales, garantizando bajo costo de mantenimiento y despliegue centralizado.*  
> *- **RNF 2 – Interfaz móvil para rondas:** Interfaz responsiva y táctil para tablets, con plano interactivo de salas y botones de alta visibilidad para que el guardia registre incidentes in situ sin demoras."*

---

### 6. Francisco Thomas Rapp (Slide 09 · Diagrama de Casos de Uso)
> *"En la **diapositiva 9** presentamos el **Diagrama de Casos de Uso General**, que modela el límite del sistema y la interacción con los actores externos.*  
> *Identificamos **8 actores de negocio**: Responsable de ingreso, Administrador del museo, Responsable de atención al cliente, Administrador web (como actor temporal), Encargado de vigilancia, Encargado de supervisión, Admin de sistema y Usuario genérico para autenticación.*  
> *En el sector de vigilancia, el Encargado de vigilancia ejecuta el caso de uso base **CU-14 (Registrar revisión de la sala)**. Cuando detecta un daño material, este caso de uso se extiende mediante la relación `<<extend>>` hacia nuestro caso de estudio principal: el **CU-15 (Registrar incidente)**, cumpliendo con la regla de registro inmediato."*

---

### 7. Francisco Abad (Slides 10 y 11 · Plantilla CU-15 y Prototipo UI)
> *"En las **diapositivas 10 y 11** profundizamos en el caso de uso central: **CU-15 Registrar Incidente**.*  
> *En la **diapositiva 10** observamos la plantilla formal. Destacamos especialmente el cumplimiento estricto del **principio de integridad de datos**: en el **Paso 4 del Curso Normal**, no decimos 'mostrar datos' genéricos, sino que el sistema busca por código y muestra taxativamente: **título/nombre de la obra, sala asignada y ubicación física dentro de la sala**.*  
> *Esto se refleja con absoluta fidelidad en el **Prototipo de Interfaz de la diapositiva 11**: el guardia ingresa el código OBJ-408, el sistema valida la pieza en pantalla, permite seleccionar el tipo de incidente, toma la hora automática de la tablet y muestra el resumen de confirmación que transiciona la obra al estado 'Inactivo'."*

---

### 8. Juan Sebastián Tarditti (Slide 12 · Diagrama de Clases del Dominio)
> *"En la **diapositiva 12** exponemos el **Diagrama de Clases del Dominio (DCD)** correspondiente al caso de uso Registrar Incidente y soporte del museo.*  
> *Queremos resaltar la consistencia estructural y la corrección de las **multiplicidades formales solicitadas por la cátedra**:*  
> *- **Gestión de Incidentes:** La clase `Incidente` registra fecha, hora y descripción, con multiplicidad exacta **1 a 1 hacia `TipoIncidente`**, y asociación **1 a 1 con `Obra`**.*  
> *- **Vigilancia y Rondas:** La relación entre `Sala` y `Guardia` se modela a través de la clase asociativa **`SalaXGuardia`**, con multiplicidad **1 a muchos (1..*) desde Sala** y **1 hacia Guardia**, auditando fecha y hora de cada inspección.*  
> *- **Patrimonio y Estados:** La clase `Obra` encapsula autor, estilo, dimensiones y material, actualizando su relación con la clase `Estado` al valor 'Inactivo' ante el registro del daño.*  
> *El diagrama se encuentra en ultra alta resolución y cuenta con zoom interactivo para auditar cada atributo y método."*

---

### 9. Agustín Cufre (Slides 13 y 14 · Trazabilidad Integral y Cierre)
> *"Para concluir nuestra defensa, en la **diapositiva 13** presentamos la **Matriz de Trazabilidad Integral**.*  
> *Aquí demostramos cómo cada requerimiento se concreta técnicamente en una tubería de 3 niveles:*  
> *Por ejemplo, el **RF-35 (Registrar incidente)** se materializa en la interacción del **CU-15**, y se persiste en las entidades **`Incidente`**, **`TipoIncidente`** y **`Obra`** del modelo de clases, cambiando el puntero a estado 'Inactivo'. Pueden explorar en la consola interactiva cómo cada uno de los 45 requerimientos tiene su correlato en casos de uso y clases.*  
> *Pasando a la **diapositiva 14**, cerramos destacando que este sistema no solo cumple con las consignas académicas de la cátedra, sino que aporta una solución realista para preservar el patrimonio cultural mediante automatización y trazabilidad estricta.*  
> *Agradecemos a los profesores Cattaneo, Turanzas, Sánchez y Padilla por sus devoluciones formativas. Quedamos a su entera disposición para responder preguntas. ¡Muchas gracias!"*

---

## ⌨️ Atajos de Teclado y Controles de la Presentación Web

* `→` / `Espacio` / `Clic`: Avanzar a la siguiente diapositiva.
* `←`: Retroceder a la diapositiva anterior.
* `G`: Abrir el visualizador general de los 14 slides (Grid Overview).
* `F`: Alternar modo Pantalla Completa.
* `Clic en diagrama` o `Botón Ampliar`: Abrir visor de zoom en alta resolución con controles `+`, `-`, `Ajustar` y arrastre libre con mouse/touch.
* `Swipe táctil`: Deslizar horizontalmente en tablets y smartphones para navegar fluidamente.
