# Ejercicio Desafio Condicionales
# El programa calcula y muestra en pantalla:
#   Subtotal de consumo.
#   Bonificaciones, si corresponde
#   Recargos, si corresponde
#   Subtotal, con recargos y bonificaciones.
#   IVA aplicado (21%), si corresponde.
#   Total final a pagar.

tipoDeCliente = input("Ingrese el tipo de cliente: ")
metrosCubicos = int(input("ingrese la cantidad de metros cubicos consumuidos: "))

# tipos de clientes: Residencial, Comercial o Industrial.
# Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.
# El costo por metro cúbico (m³) de agua es de $200/m³.
tieneBonificacion = False
tieneRecargo = False
iva = 0
casoEspecial = 0

subtotalConsumo = metrosCubicos * 200

if tipoDeCliente == "residencial": 
    #Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
    if metrosCubicos < 30:
        bonificacion = (subtotalConsumo*10)/100
        subtotalFinal = subtotalConsumo - bonificacion
        tieneBonificacion = True
    #Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.
    elif metrosCubicos > 80:
        recargo = (subtotalConsumo * 15 ) / 100
        subtotalFinal = subtotalConsumo + recargo
        tieneRecargo = True
    else:
        subtotalFinal = subtotalConsumo

    if subtotalConsumo < 35000:
     # Si el cliente residencial tiene un consumo menor a $35000, calcula un descuento especial del 5%
        casoEspecial = (subtotalConsumo * 21) / 100
        subtotalFinal = subtotalFinal - casoEspecial

elif tipoDeCliente == "comercial":
    #   Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
    if metrosCubicos > 150:
        bonificacion = (subtotalConsumo*8)/100
        subtotalFinal = subtotalConsumo - bonificacion
        tieneBonificacion = True
    #   Si el consumo es superior a 300 m³, se aplica una bonificación del 12% sobre el costo del consumo.
    elif metrosCubicos > 300:
        bonificacion = (subtotalConsumo*12)/100
        subtotalFinal = subtotalConsumo - bonificacion
        tieneBonificacion = True
    #   Si el consumo es superior a 50 m³, se aplica unarecarga del 5% sobre el costo del consumo.
    elif metrosCubicos < 50:
        recargo = (subtotalConsumo * 5 ) / 100
        subtotalFinal = subtotalConsumo + recargo
        tieneRecargo = True
    
elif tipoDeCliente == "industrial":
    # Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del 
    if metrosCubicos > 500:
        bonificacion = (subtotalConsumo*20)/100
        subtotalFinal = subtotalConsumo - bonificacion
        tieneBonificacion = True
    # Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.
    elif metrosCubicos > 1000:
        bonificacion = (subtotalConsumo*30)/100
        subtotalFinal = subtotalConsumo - bonificacion
        tieneBonificacion = True
    # Si el consumo es menor a 200 m³, se aplica un recargo del 10%.
    elif metrosCubicos < 200:
        recargo = (subtotalConsumo * 10 ) / 100
        subtotalFinal = subtotalConsumo + recargo
        tieneRecargo = True


iva= (subtotalFinal * 21) / 100
totalFinal= subtotalFinal + iva

# Mensajes de salida
print(f"Subtotal de consumo: {subtotalConsumo}")

# Si tuvo alguna bonificacion, dara mensaje
if tieneBonificacion:
    print(f"Bonificacion: {bonificacion}")
else:
    print("No corresponde la bonificacion")

# Si tuvo alguna recarga, dara mensaje
if tieneRecargo:
    print(f"Recargo: {recargo}")
else:
    print("No corresponde el recargo")
    
if casoEspecial != 0 :
    print(f"Por un consumo menor a $35000, obtuvo un descuento de {casoEspecial}")

print(f"Subtotal: {subtotalFinal}")
print(f"Iva: {iva}")
print(f"Total: {totalFinal}")