with open('guion_defensa_tpi.md', encoding='utf-8') as f:
    text = f.read()

old_tarditti = '''### 8. Juan Sebastián Tarditti (Slide 12 · Diagrama de Clases del Dominio)
> *"En la diapositiva 12 presentamos el **Diagrama de Clases del Dominio** completo (Sección 2.10 del TPI). El modelo plasma las entidades del sistema y sus relaciones:*  
> *- **Patrimonio y Obras:** Clases `Obra`, `Autor`, `Estilo`, `Material`, `TipoObra`, `TipoIngreso` y `Estado`.*  
> *- **Incidentes y Seguridad:** La entidad `Incidente` vinculada a su `TipoIncidente` y a la `Obra` afectada.*  
> *- **Vigilancia y Rondas:** El `Guardia` y las `Salas` vinculados a través de la clase asociativa `SalaXGuardia`, que registra la fecha y hora de la revisión.*  
> *- **Operaciones y Servicios:** `Exposicion`, `VisitaGuiada`, `Guia`, `Entrada`, `Tarifa` y `Visitante`.*  
> *El diagrama se encuentra maximizado al mayor tamaño posible en pantalla con zoom interactivo, permitiendo apreciar nítidamente cada clase, atributo y método. A la derecha, una síntesis conceptual continua detalla la gestión de incidentes, el control de estados de la obra y la Regla de Negocio 1 de reingreso obligatorio a depósito tras la restauración."*'''

new_tarditti = '''### 8. Juan Sebastián Tarditti (Slide 12 · Diagrama de Clases del Dominio)
> *"En la diapositiva 12 presentamos el **Diagrama de Clases del Dominio** correspondiente al caso de uso Registrar Incidente y soporte museológico (Sección 2.10 del TPI). Destacamos especialmente la consistencia de multiplicidades:*  
> *- **Gestión de Incidentes:** La entidad `Incidente` documenta fecha, hora y descripción, con multiplicidad exacta **1 a 1** hacia `TipoIncidente` y **1** hacia `Obra`.*  
> *- **Vigilancia y Rondas:** La relación entre `Sala` y `Guardia` se modela mediante la clase asociativa `SalaXGuardia`, con multiplicidad **1 a muchos (1..*)** desde Sala y **1** hacia Guardia para auditar el historial de revisiones.*  
> *- **Patrimonio y Estados:** `Obra` encapsula autor, estilo, dimensiones y material, actualizando su puntero hacia el objeto de estado `'Inactivo'` ante un reporte de daño.*  
> *- **Regla de Negocio 1:** Toda pieza derivada a restauración ingresa obligatoriamente a depósito antes de definir su destino final.*  
> *El diagrama está maximizado en alta definición y con zoom interactivo para auditar cada atributo y método."*'''

if old_tarditti in text:
    text = text.replace(old_tarditti, new_tarditti)
    with open('guion_defensa_tpi.md', 'w', encoding='utf-8') as f:
        f.write(text)
    # also sync to artifact path
    art_path = r'C:\Users\thoma\.gemini\antigravity\brain\5086ba7a-0eba-448a-b21d-e90862728035\guion_defensa_tpi.md'
    with open(art_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print('Updated guion_defensa_tpi.md in workspace and artifact directory!')
else:
    print('old_tarditti not found')
