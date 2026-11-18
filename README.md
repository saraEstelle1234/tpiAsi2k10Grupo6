# Sistema de Gestión y Vigilancia Museológica – Museo de Historia Natural
## Trabajo Práctico Integrador (TPI) · Análisis de Sistemas de Información (ASI)
### Universidad Tecnológica Nacional – Facultad Regional Córdoba (UTN-FRC)
**Curso:** 2K10 &nbsp;|&nbsp; **Año:** 2026 &nbsp;|&nbsp; **Grupo:** 6

---

## 🏛️ Descripción del Proyecto
Este repositorio contiene la entrega y soporte digital para la defensa oral del **Trabajo Práctico Integrador (TPI)** de la cátedra de **Análisis de Sistemas de Información (ASI)**.

El dominio bajo estudio modela integralmente el **Sistema de Gestión y Vigilancia Museológica** del *Museo de Historia Natural*, abarcando:
* Cadena de valor y mapa de procesos (estratégico, clave y soporte).
* Proceso crítico de soporte: **Gestionar incidentes y restauración de obras**.
* Modelado BPMN a **Nivel Descriptivo (Nivel 1)** y **Nivel Operativo (Nivel 2)** incorporando las observaciones de la cátedra:
  - 4 carriles formalizados: *Guardia del museo*, *Encargado Web*, *Encargado de Supervisor* y *Encargado de Restauración*.
  - Consumo explícito de almacenes de datos maestros (*Incidente*, *Salas*, *Obras*) y consulta de acciones sugeridas según el material.
  - Estados explícitos de sala (*'Incidente activo'* / *'Sin novedades'*) y de obra (*'Inactivo'* / *'Activo'*).
  - Actividad explícita de *Restaurar obra* con reingreso obligatorio a depósito (**Regla de Negocio 1**).
* Especificación de Requerimientos Funcionales (15 paquetes) y Requerimientos No Funcionales (RNF-01 Módulo Web y RNF-02 Interfaz Táctil Móvil).
* **Frontera del Software:** Diagrama de Casos de Uso completo con 42 CUs continuos.
* **Caso de Uso Central:** Plantilla formal del **CU-15 (Registrar incidente)** y prototipo de interfaz ergonómica para tablet.
* **Modelo de Dominio:** Diagrama de Clases del Dominio completo con atributos, métodos, multiplicidades y clases asociativas (`SalaXGuardia`).
* **Matriz de Trazabilidad Integral:** Correspondencia directa y bidireccional entre Requerimientos Funcionales, Casos de Uso y Clases de Dominio.

---

## 🚀 Acceso Rápido y Despliegue
* 🌐 **Presentación Interactiva en Vivo (GitHub Pages):** [`index.html`](./index.html) o [`presentacion.html`](./presentacion.html)
* 📜 **Guion Oficial de Defensa Oral (9 integrantes):** [`guion_defensa_tpi.md`](./guion_defensa_tpi.md)

---

## 👥 Equipo de Trabajo · Grupo 6
| Integrante | Legajo | Rol en la Defensa Oral |
| :--- | :---: | :--- |
| **Abad, Francisco** | 423269 | Portada, Dominio bajo estudio y Objetivos |
| **Cufre, Agustín** | 419166 | Mapa de Procesos de la Organización |
| **Marcuzzi, Tomas** | 403382 | Plantilla de Descripción del Proceso y Reglas de Negocio |
| **Jastrzebski, Emiliano** | 402760 | Modelado BPMN Descriptivo y Operativo (4 carriles) |
| **Molina, Tobias** | 419749 | Requerimientos Funcionales y No Funcionales (RF y RNF) |
| **Thomas Rapp, Francisco** | 408990 | Diagrama de Casos de Uso (42 CUs) |
| **Moyano, Lucas Uriel** | 410975 | Plantilla Formal CU-15 y Prototipo de Pantalla Tablet |
| **Tarditti, Juan Sebastián** | 400212 | Diagrama de Clases del Dominio Completo |
| **Pereyra, Kevin** | 418201 | Matriz de Trazabilidad de Requerimientos y Cierre |

---

## 🎓 Equipo Docente Evaluador
* **Ing. Marcela F. Cattaneo**
* **Ing. Susana B. Turanzas**
* **Ing. Claudia E. Sanchez**
* **Tomas Lautaro Padilla** (Ayudante de Cátedra)

---

## 💻 Características Técnicas de la Presentación
* **Autocontenida:** Sin dependencias externas ni conexión a internet requerida (assets e imágenes vectoriales e incrustadas en Base64).
* **Estética Minimalista Navy:** Paleta unificada en azul marino oscuro (`#0A1628` / `#0D1B33` / `#2D7FF9`).
* **Visor Interactivo de Diagramas:** Zoom mediante rueda del ratón, arrastre panorámico libre y presets de enfoque por sector/actor.
* **Dock estilo macOS:** Transiciones elásticas, salto directo entre las 14 diapositivas y controles de navegación por teclado (`←`, `→`, `Espacio`, `F` para pantalla completa, `O` para vista en cuadrícula).
