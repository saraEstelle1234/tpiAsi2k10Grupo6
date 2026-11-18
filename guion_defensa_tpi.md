# Guion de Defensa Oral — TPI ASI 2K10 (Grupo 6)
**Organización:** Museo de Historia Natural  
**Tema:** Sistema de Gestión y Vigilancia Museológica (Gestión de Incidentes y Restauración de Obras)  
**Archivo de la Presentación:** [`presentacion.html`](file:///c:/Users/thoma/Desktop/Facu%202026/ASI%202K10/TPI%20ASI/presentacion.html)  
**Total de Slides:** 14 slides interactivas en estética editorial azul marino oscuro (`#0A1628`).

---

## 👥 Distribución Oficial de los 9 Integrantes

| N° | Integrante | Legajo | Slides Asignadas | Temas de Exposición |
| :---: | :--- | :---: | :---: | :--- |
| **1** | **Francisco Abad** | 423269 | **01 y 02** | **Portada del Equipo, Dominio bajo Estudio y Objetivos Organizacionales** |
| **2** | **Agustín Cufre** | 419166 | **03** | **Mapa de Procesos de Negocio (Cadena de Valor: Estratégicos, Clave y Soporte)** |
| **3** | **Tomas Marcuzzi** | 403382 | **04** | **Plantilla de Proceso de Soporte (Sección 2.3) y Reglas de Negocio RN-1 y RN-2** |
| **4** | **Emiliano Jastrzebski** | 402760 | **05 y 06** | **Modelado BPMN Nivel 1 (Descriptivo Macro) y Nivel 2 (Detalle Operativo)** |
| **5** | **Tobias Molina** | 419749 | **07 y 08** | **Requerimientos Funcionales (15 grupos desplegables) y No Funcionales (RNFs)** |
| **6** | **Francisco Thomas Rapp (Fran)** | **408990** | **09** | **Diagrama de Casos de Uso (42 CUs, Sectorización por Actor y Concepción General)** |
| **7** | **Lucas Uriel Moyano** | 410975 | **10 y 11** | **Plantilla Formal de CU-15 (14 Pasos, A1-A3) y Prototipo de Pantalla en Tablet** |
| **8** | **Juan Sebastián Tarditti (Juan)** | **400212** | **12** | **Diagrama de Clases del Dominio (DCD): Concepción, Lógica Estructural y Clases** |
| **9** | **Kevin Pereyra** | 418201 | **13 y 14** | **Matriz de Trazabilidad Integral (RF ↔ CU ↔ DCD) y Cierre Final del Equipo** |

---

## 🎙️ Guion Verbal Exacto por Integrante

### 1. Francisco Abad (Slide 01 y 02 · Portada, Dominio y Objetivos)
> *"Buenas tardes profesores y ayudante. Damos inicio a la defensa de nuestro Trabajo Práctico Integrador para el Museo de Historia Natural de la ciudad. Como se describe textualmente en la sección 1.1 de nuestro TPI, la organización tiene como misión institucional exponer obras de artistas locales, nacionales e internacionales, garantizando su custodia y conservación activa mediante un sistema informático especializado.*  
> *En la diapositiva 2 presentamos el dominio bajo estudio: el museo cuenta con diversas salas de exposición temática y permanente, un depósito central de resguardo patrimonial, personal de vigilancia en sala y articulación con talleres externos de restauración. Se destacan tres objetivos organizacionales: primero, la difusión y acceso público a eventos culturales; segundo, la seguridad y vigilancia continua mediante rondas periódicas de guardia; y tercero, la conservación ágil de las obras mediante la detección temprana y registro inmediato de anomalías."*

---

### 2. Agustín Cufre (Slide 03 · Mapa de Procesos)
> *"Para situar el alcance del sistema dentro de la cadena de valor, en la diapositiva 3 exponemos el Mapa de Procesos de la organización, estructurado en tres niveles según la cátedra:*  
> *- **Estratégico:** 'Gestionar exposiciones artísticas', que planifica las temporadas y convocatorias.*  
> *- **Clave u Operativos:** 'Gestionar visitas guiadas' y 'Vender entradas', que constituyen la entrega de valor directa y el contacto con los visitantes.*  
> *- **Soporte o Apoyo:** 'Gestionar ingreso de obras artísticas' y 'Gestionar incidentes y restauración de obras'. Este último es el proceso crítico que hemos seleccionado y modelado a fondo en nuestro TPI, ya que garantiza la integridad física de las colecciones expuestas."*

---

### 3. Tomas Marcuzzi (Slide 04 · Plantilla de Proceso de Soporte)
> *"En la diapositiva 4 construimos la ficha técnica formal del proceso bajo estudio (Sección 2.3 del TPI). Su objetivo es gestionar los incidentes y la restauración de obras mediante las rondas de control realizadas por el personal de guardia, documentando los hechos en el Módulo Web para que los supervisores tomen decisiones informadas.*  
> *El cliente del proceso es el proceso esencial 'Exponer obras de arte', recibiendo como producto el informe consolidado y las piezas enviadas a reparación.*  
> *Destacamos especialmente las dos Reglas de Negocio rectoras: la **Regla 1**, de reingreso obligatorio al depósito, que establece que toda obra enviada a restauración —haya podido repararse con éxito o no— debe ingresar indefectiblemente al depósito del museo antes de definir cualquier nuevo destino o su baja; y la **Regla 2**, de registro inmediato de incidente, que obliga al guardia a documentar los detalles del hecho de manera inmediata en el sistema al constatar el daño."*

---

### 4. Emiliano Jastrzebski (Slide 05 y 06 · BPMN Nivel Descriptivo y Operativo)
> *"En la diapositiva 5 presentamos el Modelado BPMN a Nivel 1 Descriptivo. Su concepción se centra en reflejar la coreografía global entre los cuatro carriles formales de responsabilidad: **Guardia del museo**, **Admin de sistema**, **Encargado de supervisión** y **Encargado de restauración**. Muestra la secuencia macro desde que el guardia inicia su ronda de inspección física y detecta una anomalía, el administrador tipifica el incidente y define la respuesta sugerida, hasta que el supervisor evalúa las opciones y el restaurador interviene la obra.*  
> *Avanzando a la diapositiva 6, pasamos al Nivel 2 Operativo, donde el diagrama se encuentra desplegado a ancho completo para máxima legibilidad. Aquí incorporamos y resolvimos las observaciones clave de la cátedra:*  
> *1. **Alimentación y Almacenes:** La tarea 'Registrar incidente' se alimenta directamente de los almacenes maestros de **Incidente**, **Salas** y **Obras**, asociando las acciones sugeridas de acuerdo al material de la pieza.*  
> *2. **Estados Explícitos:** Cada compuerta y cambio de estado declara taxativamente hacia qué estado pasa la entidad: la compuerta bifurca entre 'Sin novedades' e 'Incidente activo', y la obra pasa a 'Inactivo' ante daño y retorna formalmente a 'Activo' tras la restauración.*  
> *3. **4 Carriles y Restauración Formal:** Separamos estrictamente las responsabilidades: el **Guardia del museo** solo reporta en su tablet móvil durante la ronda; el **Admin de sistema** tipifica el daño y evalúa la última acción sugerida; el **Encargado de supervisión** analiza el informe consolidado y decide la derivación; y en el carril del **Encargado de restauración** incorporamos la actividad explícita **'Restaurar obra'**, vinculada a la Regla de Negocio 1 de reingreso indefectible a depósito."*

---

### 5. Tobias Molina (Slide 07 y 08 · Requerimientos Funcionales y No Funcionales)
> *"En la diapositiva 7 especificamos formalmente el catálogo de **Requerimientos Funcionales** (Sección 2.4 del TPI). Para una visualización clara y cómoda, los organizamos en dos columnas independientes con comportamiento de acordeón exclusivo: al desplegar cualquiera de los 15 paquetes globales en negrita del TPI —como administración de obras, materiales, salas, guías, estilos o rondas— se abre únicamente el requerimiento seleccionado, manteniendo la columna contigua ordenada y sin espacios vacíos.*  
> *Pasando a la diapositiva 8, exponemos los **Requerimientos No Funcionales**. En la Sección 2.4 de nuestro TPI se definen taxativamente dos condiciones técnicas determinantes:*  
> *- **RNF 1 – Módulo Web de Soporte:** El sistema deberá implementarse bajo una arquitectura web cliente-servidor accesible desde navegadores web modernos sin requerir instalación de software en los puestos de trabajo.*  
> *- **RNF 2 – Interfaz móvil para rondas:** La aplicación deberá contar con una interfaz responsiva y táctil adaptada para tablets, permitiendo la visualización del plano interactivo de salas y el reporte inmediato durante las rondas de vigilancia."*

---

### 6. Francisco Thomas Rapp (Slide 09 · Diagrama de Casos de Uso)
> *"En la diapositiva 9 analizamos el **Diagrama de Casos de Uso (DCU)** completo, que modela la frontera del software a través de 42 casos de uso continuos y numerados de forma unívoca.*  
> *El diagrama se encuentra ampliado en pantalla sin márgenes residuales, y dispone de una barra superior de **sectorización por actor**: al hacer clic en 'Guardia', el visor enfoca automáticamente en CU-14 (revisión de sala) y CU-15 (registro de incidente); al seleccionar 'Supervisor', enfoca la generación de informes y seguimiento; al pulsar 'Ingreso y Obras', navega al ciclo de obras y depósito; y con 'Administrador', enfoca los catálogos y maestros.*  
> *El cuadro explicativo de la derecha sintetiza cómo se concibió el diagrama: una separación estricta entre la operación física en sala y las decisiones gerenciales, asegurando que el CU-15 funcione como nexo central de integración."*

---

### 7. Lucas Uriel Moyano (Slide 10 y 11 · Plantilla CU-15 y Prototipo UI)
> *"En la diapositiva 10 presentamos la **Plantilla Formal del Caso de Uso: Registrar Incidente (CU-15)**, estructurada idénticamente a la plantilla oficial de la sección 2.8 del TPI: con actor principal 'Encargado de vigilancia', tipo concreto, su objetivo y precondición de sesión activa y sala seleccionada.*  
> *Exponemos los 14 pasos secuenciales del Curso Normal —desde el ingreso del código del objeto, la confirmación de la pieza y la tipificación del daño, hasta el guardado con hora del servidor y el paso de la obra a estado 'Inactivo'—. También detallamos los cursos alternativos A1, A2 y A3 ante no confirmaciones o piezas no encontradas.*  
> *En la diapositiva 11 contrastamos este flujo con nuestro **Prototipo de Interfaz en Tablet**: cada paso del caso de uso se traduce fielmente en un componente visual: selector de sala prefiltrado, selector tipológico con validación instantánea y botón de confirmación de alto contraste diseñado ergonómicamente para su uso durante la ronda."*

---

### 8. Juan Sebastián Tarditti (Slide 12 · Diagrama de Clases del Dominio)
> *"En la diapositiva 12 presentamos el **Diagrama de Clases del Dominio** completo (Sección 2.10 del TPI). El modelo plasma las entidades del sistema y sus relaciones:*  
> *- **Patrimonio y Obras:** Clases `Obra`, `Autor`, `Estilo`, `Material`, `TipoObra`, `TipoIngreso` y `Estado`.*  
> *- **Incidentes y Seguridad:** La entidad `Incidente` vinculada a su `TipoIncidente` y a la `Obra` afectada.*  
> *- **Vigilancia y Rondas:** El `Guardia` y las `Salas` vinculados a través de la clase asociativa `SalaXGuardia`, que registra la fecha y hora de la revisión.*  
> *- **Operaciones y Servicios:** `Exposicion`, `VisitaGuiada`, `Guia`, `Entrada`, `Tarifa` y `Visitante`.*  
> *El diagrama se encuentra maximizado al mayor tamaño posible en pantalla con zoom interactivo, permitiendo apreciar nítidamente cada clase, atributo y método. A la derecha, una síntesis conceptual continua detalla la gestión de incidentes, el control de estados de la obra y la Regla de Negocio 1 de reingreso obligatorio a depósito tras la restauración."*

---

### 9. Kevin Pereyra (Slide 13 y 14 · Matriz de Trazabilidad y Cierre)
> *"En la diapositiva 13 presentamos la **Trazabilidad de Requerimientos**. El objetivo es mostrar de manera directa cómo cada requerimiento funcional solicitado en el TPI se materializa en uno o más casos de uso del DCU —según el alcance y los flujos operativos— y cómo ese caso de uso impacta en las clases del modelo de dominio.*  
> *En la consola podemos filtrar por módulo y seleccionar cualquier requerimiento. Por ejemplo, al elegir el **RF 35 (Registrar incidente)**, vemos su vinculación directa con el **CU-15 (Registrar incidente)** y su persistencia en las clases `Incidente`, `TipoIncidente`, `Obra` y `Estado`.*  
> *Y finalmente, en la diapositiva 14 cerramos nuestra presentación formal: agradecemos a los profesores y al ayudante de cátedra por las devoluciones y el cursado en ASI 2K10, y quedamos a total disposición de la mesa evaluadora para responder sus preguntas."*

---

## 🛠️ Atajos de Teclado y Controles de la Presentación
- `→` o `Espacio`: Avanzar a la siguiente diapositiva.
- `←`: Retroceder a la diapositiva anterior.
- `O` o Botón de Rejilla: Abrir la **Vista General de las 14 Slides** para salto directo.
- `F`: Alternar modo **Pantalla Completa**.
- `A`: Revelar instantáneamente todos los bloques de contenido de la diapositiva actual.
- `Click en Diagrama` o `Ampliar diagrama`: Abrir el visor en alta resolución con **Zoom por Rueda del Mouse**, **Arrastre Panorámico** y **Presets de Enfoque**.
- `?`: Abrir modal de ayuda y atajos rápidos.
