from generate import *
'''stats
def moda(list : list,freq = False): # se True, retorna quantas vezes repetiu
 
def mediana(list : list)   
    match len(list)%2:
        case 0:
        
        case 5:
            
def desvio padrão(list : list)
 #aqui eu nem lembro a fórmula kkk

def
'''

def avg(lists : list):
    if not isinstance(lists,list):
        raise TypeError('Must be a list')
    
    if len(lists)==0:
        raise ValueError('Lists cannot be empty')
    
    return sum(lists)/(len(lists))

def above_avg(lists : list,inclusive: bool = False):
    m = avg(lists)
    return [element for element in lists if element>=m] if inclusive else [element for element in lists if element>m]

def below_avg(lists : list, inclusive : bool = False):
    m = avg(lists)
    return [element for element in lists if element<=m] if inclusive else [element for element in lists if element<m]

print(avg([1,2,3,4,5,6,7]))