# Criador         : Brayan vieira 
# função          : Gerador de cryptografia  
# versão          : 1.0
# data da criação : 24/2/2024
import hashlib
#-----------------------------------------------------------------------------
#                       Definindo a função para cryptografar
def criptografar_dados(tipo):
#-----------------------------------------------------------------------------
#                               Escolhendo o tipo de cryptografia 
    match tipo:
        case "md5":
            escolha_criptografica = hashlib.md5()
        case "sha512":
            escolha_criptografica = hashlib.sha512()
        case "sha1":
            escolha_criptografica = hashlib.sha1()
        case "sha224":
            escolha_criptografica = hashlib.sha224()
#-----------------------------------------------------------------------------
#                           Transformando texto em cryptografia 
    texto = input(" \n Insira a informação que deseja criptografar : ")
    escolha_criptografica.update(texto.encode("utf-8"))
#-----------------------------------------------------------------------------
#                                   transformando bits em objetos 
    total = escolha_criptografica.hexdigest()
    print(f"\n \n Texto antes de ser cryptografado : {texto} \n \n \n depois de ser cryptografado : {total} \n")
#-----------------------------------------------------------------------------
#                                   Menu principal 
MENU = '''
______________________________________________________
|                                                    |
|            Bem-vindo ao CryptoGuard!               |
|    Seu parceiro confiável para criptografia.       |
|____________________________________________________|

   ██████╗ ██╗   ██╗███████╗███████╗███████╗
  ██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝
  ██║  ███╗██║   ██║███████╗███████╗███████╗
  ██║   ██║██║   ██║╚════██║╚════██║╚════██║
  ╚██████╔╝╚██████╔╝███████║███████║███████║
   ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝
   
      Proteja seus dados com facilidade!

------------------------------------------------------
|                  Menu de Criptografia              |
------------------------------------------------------
| 1. Md5                                             |
| 2. Sha512                                          |
| 3. Sha256                                          |
| 4. Sha1                                            |
| 5. Sha224                                          |
------------------------------------------------------

Insira uma opção : '''
#-----------------------------------------------------------------------------
#                           Menu do programa 
opcao_menu = input(MENU)
match opcao_menu:
    case "1":
        criptografar_dados("md5")
    case "2":
        criptografar_dados("sha512")
    case "3":
        criptografar_dados("sha256")
    case "4":
        criptografar_dados("sha1")
    case "5":
        criptografar_dados("sha224")
#-----------------------------------------------------------------------------
#                           tratando erros 
    case _:
        print("\n Erro você inseriu um caracter invalido \n ")
