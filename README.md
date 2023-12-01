# ExamenFinalSoftware

## Pregunta 1

Para la API se uso FastAPI

Evidencia de funcionalidad:
/billetera/contactos?minumero=XXXX
![contactos](https://github.com/Diegospf12/ExamenFinalSoftware/blob/main/images/Captura%20de%20pantalla%202023-11-30%20a%20la(s)%2020.05.12.png)

/billetera/pagar?minumero=XXXX&numerodestino=YYYY&valor=ZZZZ
![pagar](https://github.com/Diegospf12/ExamenFinalSoftware/blob/main/images/Captura%20de%20pantalla%202023-11-30%20a%20la(s)%2020.05.45.png)

/billetera/historial?minumero=XXXX
![historial1](https://github.com/Diegospf12/ExamenFinalSoftware/blob/main/images/Captura%20de%20pantalla%202023-11-30%20a%20la(s)%2020.06.09.png)
![historial2](https://github.com/Diegospf12/ExamenFinalSoftware/blob/main/images/Captura%20de%20pantalla%202023-11-30%20a%20la(s)%2020.07.26.png)

## Pregunta 2

Para la realizacion de pruebas unitarias (Unit Test) se usó pytest

![historial2](https://github.com/Diegospf12/ExamenFinalSoftware/blob/main/images/Captura%20de%20pantalla%202023-11-30%20a%20la(s)%2020.13.34.png)


## Pregunta 3

Para soportar un valor máximo de 200 soles a transferir por día, necesitarías hacer los siguientes cambios:

1. **Clase Cuenta**:
  Agregaría un nuevo atributo para rastrear la cantidad total de dinero que se ha transferido en el día actual. También agregaría un        método para restablecer este atributo al final del día.

3. **Método pagar**:
  Modificaría este método para que compruebe si la transferencia haría que la cantidad total de dinero transferido en el día actual         exceda el límite diario. Si es así, el método debería rechazar la transferencia.

En cuanto a los nuevos casos de prueba, podrías agregar los siguientes:

1. Un caso de prueba que verifica que se puede transferir exactamente 200 soles en un día.

2. Un caso de prueba que verifica que no se puede transferir más de 200 soles en un día.

3. Un caso de prueba que verifica que, después de que se ha alcanzado el límite diario, no se puede transferir más dinero hasta el día siguiente.

En cuanto al riesgo de "romper" lo que ya funciona, si bien esta nueva funcionalidad si va a intervenir en la forma de realizar los pagos, el unico método que tenemos que modifica directamente la BD es el de **/billetera/pagar**, ya que los demás solo devuelven la información que ya se encuentra en la BD, por lo tanto si manejamos bien esta nueva verificación del saldo en ese método, las demás funcinalidades no deberían verse afectadas, por lo tanto la API tampoco.
