# python informacoes IP
 <h2>Classe Ip_dados  </h2>
Essa classe trabalha com a API da plataforma https://ipinfo.io/
 para obter informacoes de IP

 A classe funciona da seguinte forma:

 importe a classe

    from Iptest import Ip_dados

Após importar a classe crie o objeto

    obj_ini = Ip_dados(IP)

Obs: 
    O parametro IP consiste em um objeto String do número de IP ao qual se deseja buscar as informações

Essa classe foi criada para ser bem intuitiva e simples:

Após o utilizador declarar e instanciar a classe passamos para os métodos de retorno de informações

__Métodos:__

    get_Ip() - Metodo que retorna o endereço IP

    get_Hostname() - Método que retorna o hostname do IP

    get_City() - Método que retorna a cidade do IP

    get_Region() - Método que retorna a Região do IP

    get_Country() - Método que reotorna o Pais do IP

    get_Loc() - Método que retorna a localização geo do IP

    get_Org() - Método que retorna os dados sobre o dominio ou organização

    get_Postal() - Método que retorna o codigo postal ou CEP da localidade

    get_Timezone() - Método que retorna sobre o fuso horario

    get_Readme() - Método que retorna um readme sobre a organização

__Atenção__

Algumas informações retornadas não terão valor porém não retorna erro graças ao tratamento usado pela classe para evitar transtornos, caso a informação não exista ela estará em branco.

Exemplo simples de funcionamento

    from Iptest import Ip_dados

    ip = input("Entre com o IP no formato : 0.0.0.0 :)
    
    dados = Ip_dados(ip)

    print(dados.get_Ip())
    
    print(dados.get_Hostname())

Caso queiram obter outras informaçôes é só chamar os metodos para uma varivel ou apresentar direto no print

Vou disponibilizar a documentação da classe para maior entendimento.





