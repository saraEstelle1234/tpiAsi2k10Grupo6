import os
import re
import json
import base64

def get_base64_img(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

# Ensure crops exist
b64_traza_bpmn = get_base64_img('media/traza_node_bpmn.png')
b64_traza_dcu = get_base64_img('media/traza_node_dcu.png')
b64_traza_proto = get_base64_img('media/traza_node_proto.png')
b64_traza_dcd = get_base64_img('media/traza_node_dcd.png')

print("Base64 crops loaded successfully.")

# Speaker notes dataset from guion_defensa_tpi.md
SPEAKER_NOTES = {
    1: {
        "speaker": "Agustín Cufre",
        "time": "1:45 min",
        "title": "Portada y Equipo del Grupo 6",
        "speech": "Buenas tardes profesores. Somos el Grupo 6 del curso 2K10 y hoy presentamos nuestro Trabajo Práctico Integrador: el Sistema de Gestión y Vigilancia Museológica para el Museo de Historia Natural. Nuestro equipo está compuesto por 8 integrantes activos, coordinando cada etapa metodológica desde el negocio hasta las clases del software.",
        "bullets": [
            "Presentación institucional del equipo y cátedra de ASI.",
            "Encuadre del proyecto: Sistema de Gestión y Vigilancia Museológica.",
            "Duración total de la defensa: 15 minutos cronometrados."
        ]
    },
    2: {
        "speaker": "Agustín Cufre",
        "time": "1:45 min",
        "title": "Dominio Bajo Estudio y Objetivos",
        "speech": "Analizamos el dominio bajo estudio. El museo expone colecciones de arte y paleontología de artistas locales e internacionales, sustentándose mediante el cobro de entradas generales y el arancel optativo de visitas guiadas. Como se observa en la fotografía oficial de las salas de exhibición, el museo cuenta con objetos animados y piezas de alto valor patrimonial sensibles a la temperatura, humedad e iluminación según su material. Nuestro alcance se centra en dar soporte integral a las rondas de inspección física y al congelamiento inmediato del daño cuando ocurre un incidente.",
        "bullets": [
            "Misión: Exponer obras y preservar el patrimonio con control de incidentes.",
            "Proceso Esencial: 'Exponer obras de arte' (cliente directo del software).",
            "Proceso de Soporte Bajo Estudio: 'Gestionar incidentes y restauración de obras'."
        ]
    },
    3: {
        "speaker": "Kevin Pereyra",
        "time": "1:30 min",
        "title": "Mapa de Procesos de Negocio",
        "speech": "Presentamos la vista externa organizacional a través del Mapa de Procesos. Clasificamos los procesos en tres niveles: Estratégicos (Planificar exposiciones, Planificar visitas, Definir precios de guía y Definir precios de entrada); Esencial (Exponer obras de arte, corazón del museo); y Soporte (Gestionar ingreso de obras, Administrar RRHH y Gestionar incidentes y restauración de obras). Mantuvimos 'Definir precios de guía' y 'Definir precios de entrada' separados respetando la literalidad del enunciado, pero señalamos que en un modelo optimizado de granularidad pueden unificarse en 'Definir tarifas y servicios', complementado con la diagramación de horarios de guías.",
        "bullets": [
            "Procesos Estratégicos, Esenciales y de Soporte según Porter.",
            "Alineación con la observación docente: Granularidad en tarifas de entrada y guía.",
            "Identificación del cliente del proceso de incidentes: Exponer obras de arte."
        ]
    },
    4: {
        "speaker": "Tobias Molina",
        "time": "1:30 min",
        "title": "Plantilla de Descripción de Proceso",
        "speech": "Formalizamos la Plantilla de Descripción del Proceso de Soporte: Gestionar incidentes y restauración de obras. El objetivo es gestionar incidentes y restauración mediante rondas de vigilancia, registrando en el Módulo Web para que los supervisores resuelvan el destino de las piezas. Su cliente es el proceso esencial 'Exponer obras de arte' y su producto es el informe de salas recorridas y las obras derivadas a reparación. Destacamos dos Reglas de Negocio fundamentales: RN-01 (Prioridad de rondas en salas críticas según sensibilidad del material) y RN-02 (Prohibición de registrar incidentes si la obra no pertenece a la sala asignada en la ronda).",
        "bullets": [
            "Ficha normalizada del proceso crítico bajo estudio.",
            "Regla de Negocio RN-01: Rondas prioritarias según material animado.",
            "Regla de Negocio RN-02: Integridad estricta entre Guardia, Sala y Obra."
        ]
    },
    5: {
        "speaker": "Tomas Marcuzzi",
        "time": "1:00 min",
        "title": "BPMN Nivel Descriptivo (4 Carriles)",
        "speech": "En las diapositivas 5 y 6 modelamos la vista interna del proceso con BPMN. Iniciamos con el Nivel Descriptivo, estructurado en cuatro carriles que reflejan fielmente los roles reales de la organización: Encargado de Vigilancia (ronda física y novedades), Encargado Web (registro administrativo y tipos de incidentes), Encargado de Supervisión (evaluación y destino) y Restaurador (reparación física de la obra). Cada rol tiene responsabilidades acotadas, evitando sobrecargar al guardia de tareas administrativas que corresponden a la supervisión.",
        "bullets": [
            "Estructura en 4 carriles: Guardia, Encargado Web, Supervisor y Restaurador.",
            "Separación clara entre ronda física y administración web.",
            "Comprensión de alto nivel del flujo de negocio sin detalles técnicos."
        ]
    },
    6: {
        "speaker": "Tomas Marcuzzi",
        "time": "1:00 min",
        "title": "BPMN Nivel Operativo Corregido",
        "speech": "Pasamos al Nivel Operativo, donde aplicamos las correcciones metodológicas solicitadas por el docente: 1) Actividad explícita 'Restaurar obra' en el carril del Restaurador cuando el supervisor resuelve la reparación; 2) Almacenes de datos 'Obras' y 'Salas' que alimentan la actividad de registro de incidentes; 3) Carril administrativo del 'Encargado Web' para tipos de incidentes; y 4) Notación estricta en las actividades de cambio de estado indicando el estado destino: 'Incidente activo' en Sala y 'En restauración' o 'Inactivo' en Obra.",
        "bullets": [
            "Corrección 1: Actividad 'Restaurar obra' en carril Restaurador.",
            "Corrección 2: Objetos de datos Obras y Salas alimentando el registro.",
            "Corrección 3: Estados destino explícitos en cada actividad ('Incidente activo', 'Inactivo').",
            "Usa los botones del Recorrido Guiado para hacer foco en cada sector."
        ]
    },
    7: {
        "speaker": "Lucas Moyano",
        "time": "1:00 min",
        "title": "Requerimientos Funcionales (45 RFs)",
        "speech": "Detallamos la especificación de Requerimientos Funcionales. Identificamos 45 RFs clasificados en 9 módulos del dominio: Rondas y Vigilancia, Gestión de Incidentes, Administración de Obras, Salas, Tipos de Incidentes, Exposiciones, Visitas Guiadas, Venta de Entradas y Seguridad. Destacamos especialmente los RFs del caso de estudio: RF43 (consultar planificación de ronda), RF44 (registrar revisión de sala), RF45 (registrar incidente con validación de pertenencia de obra), RF46 (sugerencia inmediata de acciones según material) y RF50 (cambio de estado de obra a inactiva y derivación a restauración).",
        "bullets": [
            "45 Requerimientos Funcionales categorizados en 9 módulos de negocio.",
            "Trazabilidad completa con las actividades del BPMN Operativo.",
            "Foco en RF43 a RF50 que sustentan el caso crítico de incidentes."
        ]
    },
    8: {
        "speaker": "Lucas Moyano",
        "time": "0:45 min",
        "title": "Requerimientos No Funcionales (RNF)",
        "speech": "Complementamos con los Requerimientos No Funcionales que garantizan la calidad del software según ISO/IEC 25010: RNF-01 (Seguridad y Control de Acceso basado en Roles: RBAC con token JWT y HTTPS, limitando qué pantallas puede operar el guardia frente al supervisor) y RNF-02 (Rendimiento y Disponibilidad en Rondas: tiempo de respuesta sub-segundo <1.5s y disponibilidad del 99.5% durante el horario de exhibición al público).",
        "bullets": [
            "RNF-01: Seguridad, RBAC y confidencialidad de novedades patrimoniales.",
            "RNF-02: Disponibilidad 99.5% y latencia <1.5s en rondas de vigilancia.",
            "Conformidad con el estándar internacional ISO/IEC 25010."
        ]
    },
    9: {
        "speaker": "Francisco Thomas Rapp",
        "time": "1:30 min",
        "title": "Diagrama de Casos de Uso General",
        "speech": "En la diapositiva 9 presentamos el Diagrama de Casos de Uso General que traduce los requerimientos funcionales en interacciones del usuario con el sistema. Identificamos 5 actores del sistema: Encargado de Vigilancia, Administrador Web, Encargado de Supervisión, Responsable de Atención al Cliente y Usuario General. El núcleo de nuestra solución articula el caso de uso base CU-14 'Registrar revisión de la sala' con una relación «extend» hacia el CU-15 'Registrar Incidente', el cual solo se dispara si el guardia detecta una anomalía o daño físico en su ronda.",
        "bullets": [
            "5 Actores organizacionales modelados en el sistema.",
            "Relación clave: CU-14 'Registrar revisión' extiende a CU-15 'Registrar incidente'.",
            "Separación entre vigilancia presencial y administración centralizada."
        ]
    },
    10: {
        "speaker": "Francisco Abad",
        "time": "1:00 min",
        "title": "Plantilla CU-15: Registrar Incidente",
        "speech": "Profundizamos en el caso de uso central: CU-15 Registrar Incidente. Especificamos el flujo normal paso a paso: el guardia selecciona la sala, busca el objeto dañado, el sistema muestra sus datos verificando que pertenezca a la sala, el guardia selecciona el tipo de incidente, el sistema presenta en solo lectura las acciones sugeridas de mitigación según el material y solicita confirmación. Como observó el docente en sus correcciones: eliminamos la ambigüedad de 'mostrar datos' especificando exactamente qué atributos se visualizan: Código, Título, Autor, Material y Ubicación.",
        "bullets": [
            "Plantilla detallada: Flujo básico de 11 pasos y flujos alternativos.",
            "Corrección docente aplicada: 'Mostrar datos' reemplazado por atributos concretos.",
            "Integridad de negocio: Verificación estricta de Obra perteneciente a la Sala."
        ]
    },
    11: {
        "speaker": "Francisco Abad",
        "time": "0:45 min",
        "title": "Prototipo de Pantalla UI (Página 13)",
        "speech": "Mostramos el Prototipo de Pantalla diseñado para el CU-15. La interfaz refleja el principio 'un control por paso': cuadro de búsqueda de objeto con botón Buscar, ficha de solo lectura con los datos confirmados del objeto (Nombre, Sala, Ubicación), selector desplegable de Tipo de Incidente, campo de hora automática y panel de acciones sugeridas con diálogo de confirmación final.",
        "bullets": [
            "Fiel reflejo de la maqueta oficial de la página 13 del TPI.",
            "Diseño ergonómico para uso ágil en dispositivos móviles o tablets de ronda.",
            "Controles bloqueados en solo lectura para preservar la integridad patrimonial."
        ]
    },
    12: {
        "speaker": "Juan Sebastián Tarditti",
        "time": "1:45 min",
        "title": "Diagrama de Clases del Dominio (DCD)",
        "speech": "Exponemos el Diagrama de Clases del Dominio completo, estructurado en torno al caso Registrar Incidente. La clase central 'Incidente' encapsula fecha, hora y descripción, asociándose con 'Obra', 'TipoIncidente' y 'Sala'. Destacamos las multiplicidades corregidas expresamente solicitadas por el docente: 1) Incidente ➔ (1) TipoIncidente: cada incidente tiene obligatoriamente un único tipo tipificado; 2) Sala ➔ (*) SalaXGuardia: una sala participa en múltiples asignaciones históricas de ronda con el guardia. 'Obra' delega en 'Material' para conocer las reacciones ante estímulos, y 'TipoIncidente' proporciona las acciones sugeridas.",
        "bullets": [
            "Corrección 1: Multiplicidad estricta Incidente ➔ (1) TipoIncidente.",
            "Corrección 2: Multiplicidad Sala ➔ (*) SalaXGuardia para histórico de rondas.",
            "Encapsulamiento de métodos: registrarObraInactiva() y registrarObraActiva().",
            "Usa los botones de Foco de Clases para navegar cada sector del DCD."
        ]
    },
    13: {
        "speaker": "Agustín Cufre",
        "time": "1:30 min",
        "title": "Trazabilidad Integral y Pipeline E2E",
        "speech": "Presentamos la Trazabilidad Integral del software. En el nuevo Hilo Conductor de 5 Estaciones pueden comprobar cómo cada decisión de diseño se encadena sin fisuras: 1) La tarea del BPMN Operativo 'Registrar tipo de incidente' da origen al 2) Requerimiento RF45 y la regla RN-02, que a su vez se implementa en el 3) Caso de Uso CU-15; este define cada control del 4) Prototipo UI y se materializa en las clases 5) Incidente, Sala, Obra y TipoIncidente del DCD. Como nota de alcance, el DCD modela con máxima granularidad este caso crítico por indicación de la cátedra, garantizando una arquitectura robusta y consistente.",
        "bullets": [
            "Hilo E2E de 5 Estaciones: BPMN ➔ RF ➔ CU ➔ UI ➔ DCD.",
            "Matriz de Cobertura con atenuación inteligente de módulos no relacionados.",
            "Nota de alcance: Foco exhaustivo en el caso crítico de incidentes."
        ]
    },
    14: {
        "speaker": "Agustín Cufre",
        "time": "1:00 min",
        "title": "Conclusiones y Cierre de la Defensa",
        "speech": "Para concluir, el Sistema de Gestión y Vigilancia Museológica brinda una respuesta tecnológica integral al Museo de Historia Natural, protegiendo su patrimonio y garantizando la trazabilidad entre el negocio y el código. Agradecemos a los profesores de la cátedra por sus observaciones y devoluciones, y quedamos a su entera disposición para responder cualquier pregunta.",
        "bullets": [
            "Cierre formal de la defensa oral grupal.",
            "Agradecimiento a los docentes y apertura de ronda de preguntas.",
            "Créditos finales a los 8 integrantes activos del Grupo 6."
        ]
    }
}

print(f"Notes dictionary prepared for {len(SPEAKER_NOTES)} slides.")
