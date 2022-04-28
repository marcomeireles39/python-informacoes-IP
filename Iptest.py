"""
Arquivo : Iptest.py
Data 28-04-2022
Classe Ip_dados(ip)
"""
import re
import json
from urllib.request import urlopen


class Ip_dados():

    IP = str('')
    HOSTNAME = ''
    CITY = ''
    REGIAO = ''
    COUNTRY = ''
    LOC = ''
    ORG = ''
    POSTAL = ''
    TIMEZONE = ''
    README = ''

    def __init__(self, ip):

        """
        from Iptest import Ip_dados

        Método contrutor ao qual será passado o ip ao qual será retornado a informação
        para isso é preciso passar um parametro

        :param IP : String

        Exemplo:

            obj_ini = Ip_dados('64.18.0.0')
        """
        try:
        # Parte de organização dos dados colocando os ip na url
            
            url = 'https://ipinfo.io/{}/json'.format(ip)
            resposta = urlopen(url)
            dados = json.load(resposta)
        
        # Feito a adequação. conectado e tendo as imformações de retorno passa para
        # a proxima fase que consiste em verificar a existencia dos dados um a um
        # e após verificado a sua existencia elas são organizadas em variveis
    
            for da in dados:
                if (da == 'ip'):
                    self.IP = dados['ip']

                if (da == 'hostname'):
                    self.HOSTNAME = dados['hostname']

                if (da == 'city'):
                    self.CITY = dados['city']
                
                if (da == 'region'):
                    self.REGIAO = dados['region']
                
                if (da == 'country'):
                    self.COUNTRY = dados['country']

                if (da == 'loc'):
                    self.LOC = dados['loc']
                
                if (da == 'org'):
                    self.ORG = dados['org']

                if (da == 'postal'):
                    self.POSTAL = dados['postal']

                if (da == 'timezone'):
                    self.TIMEZONE = dados['timezone']
                
                if (da == 'readme'):
                    self.README = dados['readme']
        except :

            print('erro')
    
    # Agora pego todos os dados e passados para as variveis daqui pra baixo
    # temos os metodos de retorno das informações uma a uma

    # Método que retorna do ip

    def get_Ip(self):
        """
        
        Metodo de retorno do IP
        
        Exemplo:

            var_retorno = obj_ini.getIp()
        """
        return self.IP

    # Método que retorna o hostname
    
    def get_Hostname(self):
        
        """
        
        Metodo de retorno do Hostname
        
        Exemplo:

            var_retorno = obj_ini.get_Hostname()
        """

        return self.HOSTNAME

    # Método de retorno da cidade

    def get_City(self):
        
        """
        
        Metodo de retorno da cidade
        
        Exemplo:

            var_retorno = obj_ini.get_City()
        """

        return self.CITY

    # Método de retorno da Região

    def get_Region(self):

                
        """
        
        Metodo de retorno da Região
        
        Exemplo:

            var_retorno = obj_ini.get_Region()
        """
        return self.REGIAO

    # Método de retorno do Pais

    def get_Country(self):
                
        """
        
        Metodo de retorno do Country
        
        Exemplo:

            var_retorno = obj_ini.get_Country()
        """

        return self.COUNTRY

    # Método de retorno da localização geografica

    def get_Loc(self):
                
        """
        
        Metodo de retorno do Loc
        
        Exemplo:

            var_retorno = obj_ini.get_Loc()
        """

        return self.LOC

# Método de retorno da Organização

    def get_Org(self):
                
        """
        
        Metodo de retorno do Org
        
        Exemplo:

            var_retorno = obj_ini.get_Org()
        """

        return self.ORG

    # Método de retorno do codigo postal
    def get_Postal(self):
             
        """
        
        Metodo de retorno do Postaç
        
        Exemplo:

            var_retorno = obj_ini.get_Postal()
        """

        return self.POSTAL

    # Método de retorno da zona

    def get_Timezone(self):
                
        """
        
        Metodo de retorno do Timezone
        
        Exemplo:

            var_retorno = obj_ini.get_Timezone()
        """

        return self.TIMEZONE

    # Método de retorno do readme

    def get_Readme(self):
                
        """
        
        Metodo de retorno do Readme
        
        Exemplo:

            var_retorno = obj_ini.get_Readme()
        """
        return self.README