# -*- coding: utf-8 -*-
with open('guion_defensa_tpi.md', 'r', encoding='utf-8') as f:
    text = f.read()

idx_juan = text.find('### 8. Juan Sebastián Tarditti')
assert idx_juan != -1, "Could not find Juan Tarditti section"

new_ending = """### 8. Juan Sebastián Tarditti (Slide 12 · Diagrama de Clases del Dominio)
> *"En la diapositiva 12 presentamos el **Diagrama de Clases del Dominio** completo (Sección 2.10 del TPI). El modelo plasma las entidades del sistema y sus relaciones:*  
> *- **Patrimonio y Obras:** Clases `Obra`, `Autor`, `Estilo`, `Material`, `TipoObra`, `TipoIngreso` y `Estado`.*  
> *- **Incidentes y Seguridad:** La entidad `Incidente` vinculada a su `TipoIncidente` y a la `Obra` afectada.*  
> *- **Vigilancia y Rondas:** El `Guardia` y las `Salas` vinculados a través de la clase asociativa `SalaXGuardia`, que registra la fecha y hora de la revisión.*  
> *- **Operaciones y Servicios:** `Exposicion`, `VisitaGuiada`, `Guia`, `Entrada`, `Tarifa` y `Visitante`.*  
> *La imagen está ampliada en pantalla y dispone de zoom interactivo para enfocar cualquier clase, atributo o método si los profesores lo solicitan."*

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
"""

text = text[:idx_juan] + new_ending

with open('guion_defensa_tpi.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated guion_defensa_tpi.md successfully!")
