# los diccionarios son variables especiales que me permiten almacenar 
# multiples datos de diferente tipo en una sola variable

empleado={
    'nombre':"Juan",
    'cedula':1036655428,
    'cargo':"Analista de datos",
    'salaro':8000000,
    'horastrabajadas':40,
    'aplicasubsidiotrasporte':False,
    'deudas':[1500000,800000]
}
#print(empleado)
#print(empleado['nombre'])
#print(empleado['deudas'][1])
# recorriendo un diccionario: 
for observadoratributo,observadorvalor in empleado.items():
    print(observadoratributo)
    print(observadorvalor)
