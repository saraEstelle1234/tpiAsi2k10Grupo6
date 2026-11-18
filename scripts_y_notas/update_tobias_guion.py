# -*- coding: utf-8 -*-
with open('guion_defensa_tpi.md', 'r', encoding='utf-8') as f:
    text = f.read()

old_tobias_part = """> *"En la diapositiva 7 especificamos formalmente el catálogo de **Requerimientos Funcionales** (Sección 2.4). Los estructuramos mediante desplegables interactivos que agrupan los 15 paquetes globales del TPI: administración de obras, materiales, salas, guías, estilos, tipos de incidentes, exposiciones, visitas, boletería, rondas, incidentes, restauración, informes y administración de sesión. Cada grupo puede abrirse para inspeccionar sus requerimientos asociados.*  
> *Pasando a la diapositiva 8, presentamos los **Requerimientos No Funcionales** determinantes de la arquitectura: el Módulo Web cliente-servidor accesible sin instalación (RNF 1), la interfaz móvil táctil adaptada para tablets de guardia (RNF 2), tiempos de respuesta menores a 2 segundos en transacciones críticas (RNF 3), seguridad por perfiles RBAC y sesiones cifradas (RNF 4), disponibilidad 24/7 con persistencia ACID (RNF 5) y registro inmutable de marcas de tiempo y auditoría de eventos (RNF 6)."*"""

new_tobias_part = """> *"En la diapositiva 7 especificamos formalmente el catálogo de **Requerimientos Funcionales** (Sección 2.4 del TPI). Para una visualización clara y cómoda, los organizamos en dos columnas independientes con comportamiento de acordeón exclusivo: al desplegar cualquiera de los 15 paquetes globales en negrita del TPI —como administración de obras, materiales, salas, guías, estilos o rondas— se abre únicamente el requerimiento seleccionado, manteniendo la columna contigua ordenada y sin espacios vacíos.*  
> *Pasando a la diapositiva 8, exponemos los **Requerimientos No Funcionales**. En la Sección 2.4 de nuestro TPI se definen taxativamente dos condiciones técnicas determinantes:*  
> *- **RNF 1 – Módulo Web de Soporte:** El sistema deberá implementarse bajo una arquitectura web cliente-servidor accesible desde navegadores web modernos sin requerir instalación de software en los puestos de trabajo.*  
> *- **RNF 2 – Interfaz móvil para rondas:** La aplicación deberá contar con una interfaz responsiva y táctil adaptada para tablets, permitiendo la visualización del plano interactivo de salas y el reporte inmediato durante las rondas de vigilancia."*"""

assert old_tobias_part in text, "Could not find old Tobias script in guion_defensa_tpi.md"
text = text.replace(old_tobias_part, new_tobias_part)

with open('guion_defensa_tpi.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated guion_defensa_tpi.md successfully!")
