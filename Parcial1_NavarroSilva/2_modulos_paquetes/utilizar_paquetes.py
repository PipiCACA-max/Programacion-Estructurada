from paquete1 import modulos_paquete

modulos_paquete.borrarPantalla()
print(modulos_paquete.saludar("solomeo paredes"))

modulos_paquete.borrarPantalla()

nom,tel=modulos_paquete.solicitarDatos2()
print(f"\n\t..::Agenda telefonica::..\n\t\tNombre: {nom}\n\t\tTelefono: {tel}")

modulos_paquete.espereTecla()
modulos_paquete.borrarPantalla()