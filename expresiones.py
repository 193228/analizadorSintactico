import ply.lex as lex

tokens  = (
    'P',
    'A',
    'D',
    'T',
    'LETRAS',
    'DIGITOS',
    'ARROBA',
    'DOMINIO',
    'TIPO',
    'PUNTO',
    'GUIONBAJO',
    'B',
    'CARACTERES',
    'MB',
    'BN',
    'NB',
)

t_P = r'<P>'
t_A = r'<A>'
t_D = r'<D>'
t_T = r'<T>'
t_CARACTERES = r'[%$#+;!-]'
t_LETRAS = r'[a-zA-Z]'
t_DIGITOS = r'[0-9]'
t_ARROBA = r'@'
t_GUIONBAJO = r'_'
t_DOMINIO = r'\b(?:gmail|outlook|yahoo|hotmail)\b'
t_TIPO = r'\b(?:mx|com)\b'
t_PUNTO = r'.'
t_B = r'\b(?:0|1)\b'
t_ignore = ' \t'
t_MB = r'<MB>'
t_BN = r'<BN>'
t_NB = r'<NB>'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Error de lexico -> "+str(t.value))
    t.lexer.skip(1)

analizador = lex.lex()