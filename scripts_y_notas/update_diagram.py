import html

def escape_xml_attr(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&apos;")

def make_class(cid, name, x, y, w, attrs, meths):
    h_title = 28
    # Exact tight heights: 16px per line + 4px vertical padding
    h_attrs = len(attrs) * 16 + 4
    h_sep = 8
    h_meths = len(meths) * 16 + 4
    h_total = h_title + h_attrs + h_sep + h_meths

    raw_attrs_html = "".join([f'<p style="margin:0px;">{a}</p>' for a in attrs])
    raw_meths_html = "".join([f'<p style="margin:0px;">{m}</p>' for m in meths])

    val_attrs = escape_xml_attr(raw_attrs_html)
    val_meths = escape_xml_attr(raw_meths_html)
    val_name = escape_xml_attr(name)

    xml_parts = []
    xml_parts.append(f'''<mxCell id="{cid}" parent="1" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize={h_title};horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#000000;strokeWidth=1;" value="{val_name}" vertex="1">
<mxGeometry x="{x}" y="{y}" width="{w}" height="{h_total}" as="geometry" />
</mxCell>''')

    xml_parts.append(f'''<mxCell id="{cid}_attrs" parent="{cid}" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=6;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;fontSize=11;" value="{val_attrs}" vertex="1">
<mxGeometry y="{h_title}" width="{w}" height="{h_attrs}" as="geometry" />
</mxCell>''')

    xml_parts.append(f'''<mxCell id="{cid}_sep" parent="{cid}" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;strokeColor=inherit;" value="" vertex="1">
<mxGeometry y="{h_title + h_attrs}" width="{w}" height="{h_sep}" as="geometry" />
</mxCell>''')

    xml_parts.append(f'''<mxCell id="{cid}_meths" parent="{cid}" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=top;spacingLeft=6;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;whiteSpace=wrap;html=1;fontSize=11;" value="{val_meths}" vertex="1">
<mxGeometry y="{h_title + h_attrs + h_sep}" width="{w}" height="{h_meths}" as="geometry" />
</mxCell>''')

    return "\n".join(xml_parts), h_total

def make_edge(eid, src, tgt, mult, exit_x, exit_y, entry_x, entry_y):
    return f'''<mxCell id="{eid}" parent="1" style="endArrow=open;endFill=0;html=1;rounded=0;strokeWidth=1;strokeColor=#000000;exitX={exit_x};exitY={exit_y};exitDx=0;exitDy=0;entryX={entry_x};entryY={entry_y};entryDx=0;entryDy=0;" edge="1" source="{src}" target="{tgt}">
<mxGeometry relative="1" as="geometry" />
</mxCell>
<mxCell id="{eid}_lbl" parent="{eid}" style="resizable=0;html=1;align=right;verticalAlign=bottom;labelBackgroundColor=none;fontSize=11;fontStyle=1;" value="{mult}" vertex="1" connectable="0">
<mxGeometry relative="1" x="0.85" as="geometry">
<mxPoint x="-6" y="-6" as="offset" />
</mxGeometry>
</mxCell>'''

classes_xml = []
heights = {}

# 1. Incidente (attrs: 6, meths: 6)
c_xml, h = make_class(
    cid="cls_incidente",
    name="Incidente",
    x=560, y=310, w=230,
    attrs=[
        "- fecha",
        "- hora",
        "- descripcion",
        "- obra: Obra",
        "- tipoIncidente: TipoIncidente",
        "- sala: Sala"
    ],
    meths=[
        "+ crear()",
        "+ mostrarIncidente()",
        "+ registrarIncidente()",
        "+ conocerObra()",
        "+ conocerTipoIncidente()",
        "+ conocerSala()"
    ]
)
classes_xml.append(c_xml)
heights["cls_incidente"] = h

# 2. TipoIncidente (attrs: 2, meths: 2)
c_xml, h = make_class(
    cid="cls_tipo_incidente",
    name="TipoIncidente",
    x=200, y=360, w=210,
    attrs=[
        "- nombre",
        "- descripcion"
    ],
    meths=[
        "+ crear()",
        "+ mostrarTipoIncidente()"
    ]
)
classes_xml.append(c_xml)
heights["cls_tipo_incidente"] = h

# 3. Sala (attrs: 6, meths: 5)
c_xml, h = make_class(
    cid="cls_sala",
    name="Sala",
    x=560, y=690, w=230,
    attrs=[
        "- nroSala",
        "- nombre",
        "- tematica",
        "- capacidad",
        "- obra: Obra",
        "- salaXGuardia: SalaXGuardia"
    ],
    meths=[
        "+ crear()",
        "+ mostrarSala()",
        "+ conocerObra()",
        "+ conocerSalaXGuardia()",
        "+ buscarObra()"
    ]
)
classes_xml.append(c_xml)
heights["cls_sala"] = h

# 4. SalaXGuardia (attrs: 4, meths: 4)
c_xml, h = make_class(
    cid="cls_salaxguardia",
    name="SalaXGuardia",
    x=200, y=690, w=210,
    attrs=[
        "- fecha",
        "- horaRevision",
        "- estadoRevision",
        "- guardia: Guardia"
    ],
    meths=[
        "+ crear()",
        "+ mostrarSalaXGuardia()",
        "+ conocerGuardia()",
        "+ registrarRevision()"
    ]
)
classes_xml.append(c_xml)
heights["cls_salaxguardia"] = h

# 5. Guardia (attrs: 4, meths: 2)
c_xml, h = make_class(
    cid="cls_guardia",
    name="Guardia",
    x=205, y=960, w=200,
    attrs=[
        "- legajo",
        "- nombre",
        "- apellido",
        "- turno"
    ],
    meths=[
        "+ crear()",
        "+ mostrarGuardia()"
    ]
)
classes_xml.append(c_xml)
heights["cls_guardia"] = h

# 6. Obra (attrs: 13, meths: 11) - verificarCodigoObra removed per user request
c_xml, h = make_class(
    cid="cls_obra",
    name="Obra",
    x=1050, y=290, w=260,
    attrs=[
        "- codigo",
        "- nroId",
        "- titulo",
        "- dimensiones",
        "- valuacion",
        "- fechaIngreso",
        "- fechaCreacion",
        "- autor: Autor",
        "- estilo: Estilo",
        "- material: Material",
        "- tipoObra: TipoObra",
        "- tipoIngreso: TipoIngreso",
        "- estado: Estado"
    ],
    meths=[
        "+ crear()",
        "+ mostrarObra()",
        "+ conocerAutor()",
        "+ conocerEstilo()",
        "+ conocerMaterial()",
        "+ conocerTipoObra()",
        "+ conocerTipoIngreso()",
        "+ conocerEstado()",
        "+ solicitarEstadoObra()",
        "+ registrarObraInactiva()",
        "+ registrarObraActiva()"
    ]
)
classes_xml.append(c_xml)
heights["cls_obra"] = h

# 7. Estado (attrs: 2, meths: 6)
c_xml, h = make_class(
    cid="cls_estado",
    name="Estado",
    x=1080, y=50, w=200,
    attrs=[
        "- nombre",
        "- ambito"
    ],
    meths=[
        "+ crear()",
        "+ mostrarEstado()",
        "+ registrarObraInactiva()",
        "+ registrarObraActiva()",
        "+ esInactivo()",
        "+ esActivo()"
    ]
)
classes_xml.append(c_xml)
heights["cls_estado"] = h

# 8. Estilo (attrs: 2, meths: 2)
c_xml, h = make_class(
    cid="cls_estilo",
    name="Estilo",
    x=1500, y=50, w=180,
    attrs=[
        "- nombre",
        "- descripcion"
    ],
    meths=[
        "+ crear()",
        "+ mostrarEstilo()"
    ]
)
classes_xml.append(c_xml)
heights["cls_estilo"] = h

# 9. Autor (attrs: 3, meths: 2)
c_xml, h = make_class(
    cid="cls_autor",
    name="Autor",
    x=1500, y=210, w=190,
    attrs=[
        "- nombre",
        "- apellido",
        "- nacionalidad"
    ],
    meths=[
        "+ crear()",
        "+ mostrarAutor()"
    ]
)
classes_xml.append(c_xml)
heights["cls_autor"] = h

# 10. Material (attrs: 2, meths: 2)
c_xml, h = make_class(
    cid="cls_material",
    name="Material",
    x=1500, y=390, w=190,
    attrs=[
        "- nombre",
        "- reaccionEstimulos"
    ],
    meths=[
        "+ crear()",
        "+ mostrarMaterial()"
    ]
)
classes_xml.append(c_xml)
heights["cls_material"] = h

# 11. TipoObra (attrs: 2, meths: 6)
c_xml, h = make_class(
    cid="cls_tipo_obra",
    name="TipoObra",
    x=1500, y=550, w=190,
    attrs=[
        "- nombre",
        "- descripcion"
    ],
    meths=[
        "+ crear()",
        "+ mostrarTipoObra()",
        "+ tomarNombre()",
        "+ mostrarNombre()",
        "+ tomarDescripcion()",
        "+ mostrarDescripcion()"
    ]
)
classes_xml.append(c_xml)
heights["cls_tipo_obra"] = h

# Note for TipoObra
note_xml = '''<mxCell id="note_setters" parent="1" style="shape=note;whiteSpace=wrap;html=1;backgroundOutline=1;darkOpacity=0.05;fillColor=#fff2cc;strokeColor=#d6b656;size=14;fontSize=10;align=left;spacingLeft=5;spacingRight=5;" value="Los metodos de seteo de&#xa;esta clase son extensibles a&#xa;todas las clases del dominio" vertex="1">
<mxGeometry x="1760" y="605" width="180" height="70" as="geometry" />
</mxCell>
<mxCell id="e_note_tipo_obra" parent="1" style="endArrow=none;dashed=1;html=1;rounded=0;strokeWidth=1;strokeColor=#b58900;exitX=0;exitY=0.5;entryX=1;entryY=0.5;" edge="1" source="note_setters" target="cls_tipo_obra">
<mxGeometry relative="1" as="geometry" />
</mxCell>'''
classes_xml.append(note_xml)

# 12. TipoIngreso (attrs: 2, meths: 2)
c_xml, h = make_class(
    cid="cls_tipo_ingreso",
    name="TipoIngreso",
    x=1500, y=780, w=180,
    attrs=[
        "- nombre",
        "- descripcion"
    ],
    meths=[
        "+ crear()",
        "+ mostrarTipoIngreso()"
    ]
)
classes_xml.append(c_xml)
heights["cls_tipo_ingreso"] = h

# Associations
h_obra = heights["cls_obra"]

ey_estilo = round((320 - 290) / h_obra, 3)
ey_autor = round((380 - 290) / h_obra, 3)
ey_mat = round((460 - 290) / h_obra, 3)
ey_tipo = round((560 - 290) / h_obra, 3)
ey_ingreso = round((660 - 290) / h_obra, 3)
ey_inc_obra = round((414 - 290) / h_obra, 3)
ey_sala_obra = round((680 - 290) / h_obra, 3)

ey_sala_sxg = round((776 - 690) / heights["cls_sala"], 3)

edges_xml = [
    # Incidente -> TipoIncidente
    make_edge("a_inc_tipo", "cls_incidente", "cls_tipo_incidente", "1", 0, 0.44, 1, 0.5),
    # Incidente -> Sala
    make_edge("a_inc_sala", "cls_incidente", "cls_sala", "1", 0.5, 1, 0.5, 0),
    # Incidente -> Obra
    make_edge("a_inc_obra", "cls_incidente", "cls_obra", "1", 1, 0.44, 0, ey_inc_obra),
    # Sala -> SalaXGuardia
    make_edge("a_sala_sxg", "cls_sala", "cls_salaxguardia", "*", 0, ey_sala_sxg, 1, 0.5),
    # SalaXGuardia -> Guardia
    make_edge("a_sxg_guardia", "cls_salaxguardia", "cls_guardia", "1", 0.5, 1, 0.5, 0),
    # Sala -> Obra
    make_edge("a_sala_obra", "cls_sala", "cls_obra", "*", 1, 0.09, 0, ey_sala_obra),
    # Obra -> Estado
    make_edge("a_obra_estado", "cls_obra", "cls_estado", "1", 0.5, 0, 0.5, 1),
    # Obra -> Estilo
    make_edge("a_obra_estilo", "cls_obra", "cls_estilo", "1", 1, ey_estilo, 0, 0.5),
    # Obra -> Autor: Multiplicity is 1
    make_edge("a_obra_autor", "cls_obra", "cls_autor", "1", 1, ey_autor, 0, 0.5),
    # Obra -> Material
    make_edge("a_obra_material", "cls_obra", "cls_material", "1..*", 1, ey_mat, 0, 0.5),
    # Obra -> TipoObra
    make_edge("a_obra_tipo", "cls_obra", "cls_tipo_obra", "1", 1, ey_tipo, 0, 0.5),
    # Obra -> TipoIngreso
    make_edge("a_obra_ingreso", "cls_obra", "cls_tipo_ingreso", "1", 1, ey_ingreso, 0, 0.5)
]

all_content = "\n".join(classes_xml) + "\n" + "\n".join(edges_xml)

full_xml = f'''<?xml version="1.0" encoding="utf-8"?>
<mxfile host="app.diagrams.net" agent="Antigravity-ASI">
<diagram name="Diagrama de Clases del Dominio" id="dcd_2k10">
<mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="2050" pageHeight="1250" math="0" shadow="0">
<root>
<mxCell id="0" />
<mxCell id="1" parent="0" />
{all_content}
</root>
</mxGraphModel>
</diagram>
</mxfile>'''

with open('Diagramas/Diagrama_de_Clases.drawio', 'w', encoding='utf-8') as f:
    f.write(full_xml)

with open('Diagrama_de_Clases.drawio', 'w', encoding='utf-8') as f:
    f.write(full_xml)

print("Updated diagram successfully: verificarCodigoObra removed from Obra!")
