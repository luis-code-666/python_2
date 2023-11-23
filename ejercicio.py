def message_creator():
    option_usuario = input('elige entre "computadora", "celular", "cable"  = ')
    option_usuario = option_usuario.lower()
    if option_usuario == 'computadora':
        print('Con mi computadora puedo programar usando Python')
    elif option_usuario == 'celular':
        print('mi celular puedo aprender usando la app de Platzi')
    elif option_usuario == 'cable':
        print('¡Hay un cable en mi bota!')
    else:
        print('Opción no válida')
    return ''
message_creator()