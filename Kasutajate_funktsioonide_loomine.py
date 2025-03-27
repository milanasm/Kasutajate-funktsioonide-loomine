from ctypes.wintypes import LGRPID
from lib2to3.pgen2.driver import load_grammar
from math import lgamma


#1
def arithmetic(arv1:float,arv2:float,tehe:str)-> any :
    """Funktsioon töötab nagu lihtne kalkulaator
    + - liitmine,
    - - lahutamine,
    * - korrutamine,
    / - jagamine
    kui sisend ei ole järjendis [+,-,/,*],siis tagastab sõne "Tundmatu tehe"
    :param float arv1: Sisend ujukomaarvu tüübina
    :param float arv2: Sisend ujukomaarvu tüübina
    :param str tehe: sisend listist [+,-,/,*]
    :rtype: varMääramata tüüp (float või str)
    """
    if tehe in ["+","-","*","/"]:
        if arv2==0 and tehe=="/":
            vastus="DIV/0"
        else:
            vastus=eval(str(arv1)+tehe+str(arv2))
    else:
        vastus="Tundmatu tehe"
    return vastus 
#2
def is_year_leap(aasta:int)->bool:
    """
    Liigaasta leidmine.
    Tagastab True, kui aasta on liigaasta ja False, kui aasta on tavaline aasta.
    :param int aasta: Sisend kasutajalt
    :rtype: bool
    """
    if aasta%4==0:
     v-True
    else:
        v=False
    return v
#3
def square(külg:float)->any:
    """funkrioon tagastab 
    :param:Ruudu külg
    :rtype: float
    :return: Perimeeter, pindala ja diagonaal
    """
    S=külg**2
    P=4*külg
    d=(2)**(1/2)*külg
    return S,P,d
#4 
def season(param:int)->str:
    """
    param:Kuu number (1 - 13)
    :type month: int
    :return: Aastaeg, millele kuu kuulub ("talv", "kevad", "suvi" või "sügis")
    :rtype: str
    """
    if param in [1,2,12]:
        H="Talv"
    elif param in [3,4,5]:
        H="Kevad"
    elif param in [6,7,8]:
        H="Suvi"
    else:
        H="Sügis"
    return H
#5
def bank(summa: float,aastad:int)->float:
    """
    :param algkapital(eurodes)
    :param aastad: Investeerimise kestus(aastades)
    :type aastad: int
    :return: Lõppsumma pärast teatud aastat(arvestades 10% intressi)
    :rtype float
    """
    for aasta in range(aastad):
        summa*=1.1
    return summa 
#6
from random import *
def is_prime(a=randint(1,10000)):
    """
    :param: Arv, mida kontrollitakse.
    :param: Kõrgeim väärtus, mille vahemikus juhuslik arv genereeritakse
    :rtype: bool
    :return: True, kui arv on algarv, vastasel juhul False
    """
    print(a)
    v=True
    for jagaja in range(2,a):
        if a%jagaja==0:
            v=False
    return v
#7
def date(päev:int,kuu:int,aasta:int)->bool:
    """
    :param: Päev, mida kontrollitakse
    :rtype: bool
    :return: True, kui kuupäev on kehtiv, vastasel juhul False
    :param aasta: Aasta, mida kontrollitakse
    :param kuu: Kuu, mida kontrollitakse (1 kuni 12)
    :type: int
    """
    if päev in range(1,32) and kuu in [1,3,5,7,8,10,12] and aasta>0:
        v=True
    elif päev in range(1,30) and kuu==2 and is_year_leap(aasta):
        v=True
    elif päev in range(1,29) and kuu==2 and not is_year_leap(aasta):
        v=True
    elif päev in range(1,31) and kuu in [4,6,9,11,8] and aasta>0:
        v=True
    else:
        v=False
    return v