import ply.lex as lex

reservadas = ['P','A','T','D','BN','MB','NB']

tokens = reservadas+['CARACTERES',
    'LETRAS',
    'DIGITOS',
    'ARROBA',
    'DOMINIO',
    'TIPO',
    'PUNTO',
    'GUIONBAJO',
    'B',
	]

'''tokens  = (
    'CARACTERES',
    'LETRAS',
    'DIGITOS',
    'ARROBA',
    'DOMINIO',
    'TIPO',
    'PUNTO',
    'GUIONBAJO',
    'B',
    'P'
)'''

t_CARACTERES = r'[%$#-+;!]'
t_LETRAS = r'[a-zA-Z]'
t_DIGITOS = r'[0-9]'
t_ARROBA = r'@'
t_GUIONBAJO = r'_'
t_DOMINIO = r'\b(?:gmail|outlook|yahoo|hotmail)\b'
t_TIPO = r'\b(?:mx|com)\b'
t_PUNTO = r'.'
t_B = r'\b(?:0|1)\b'

def t_error(t):
    print("Error de lexico -> "+str(t.value))
    t.lexer.skip(1)

analizador = lex.lex()