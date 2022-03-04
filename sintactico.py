import ply.yacc as yacc
from expresiones import tokens
lista = []

def p_S(p):
    '''S : Remitente P Password A Asunto D Destinatario T tipoMensaje'''

def p_Remitente(p):
    '''Remitente : Correo'''

def p_Asunto(p):
    '''Asunto : Letras transformacion2
                | Numeros transformacion2'''
    print("es asunto")

def p_Destinatario(p):
    '''Destinatario : Correo '''

def p_Password(p):
    '''Password : Letras restoPass
				| Numeros restoPass
				| Caracteres restoPass '''
    print("es password")


def p_restoPass(p):
    '''restoPass : Letras restoPass
				| Numeros restoPass
				| Caracteres restoPass
				| empty '''

def p_tipoMensaje(p):
    '''tipoMensaje : BN binarioNumero
                | MB mensajeBinario
                | NB numeroBinario'''

def p_Caracteres(p):
    '''Caracteres : CARACTERES'''

def p_Correo(p):
    '''Correo : Usuario ARROBA Dominio PUNTO Tipo'''
    print("Correo")

def p_Usuario(p):
    '''Usuario : Letras restoID
                | Numeros restoID '''

def p_restoID(p):
    '''restoID : Letras restoID
                | GUIONBAJO restoID
                | Numeros restoID
                | PUNTO restoID
                | empty '''

def p_Dominio(p):
    '''Dominio : DOMINIO '''

def p_Tipo(p):
    '''Tipo : TIPO '''

def p_Letras(p):
    '''Letras : LETRAS '''  # Aca se manda a llamar identificador, lo cual es una expresion regular que se definio en la clase lexico

def p_Numeros(p):
    '''Numeros : DIGITOS '''  # Aca se manda a llamar identificador, lo cual es una expresion regular que se definio en la clase lexico

def p_transformacion(p):
    '''transformacion : Letras transformacion
                | B transformacion
                | Numeros transformacion
                | empty '''

def p_transformacion2(p):
    '''transformacion2 : Letras transformacion2
                | Numeros transformacion2
                | empty '''

def p_binarioNumero(p):
    '''binarioNumero : Letras transformacion
                | B transformacion
                | Numeros transformacion '''
    print("binarioNumero")

def p_mensajeBinario(p):
    '''mensajeBinario : Letras transformacion2
                | Numeros transformacion2 '''
    print("mensaje binario")

def p_numeroBinario(p):
    '''numeroBinario : Letras transformacion2
                | Numeros transformacion2 '''
    print("numeroBinario")

def p_empty(p):
    'empty :'
    pass


def p_error(p):
    if p:
        estado = str(p.type), str(p.lineno), str(p.lexpos), str(p.value)
        print("Error De Sintaxis -> ", p.type, " Linea -> ", p.lineno, " Posicion -> ", p.lexpos, " Simbolo/s -> ",p.value)
        parser.errok()
        lista.append(estado)
    else:
        print("Error De Sintaxis EOF")

parser = yacc.yacc()

def ejecucionAlgoritmo(texto):
    lista.clear()
    parser.parse(texto)
    return lista