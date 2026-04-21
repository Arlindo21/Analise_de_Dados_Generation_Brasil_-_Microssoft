#exemplo de como o pc le um banco de dados 
import getpass 
usuario={
    #o dicionario é um tipo dado que armazena chave - valor 
    "Luiz":"abcd",
    "fernanda":"1234",
    "paulo":"asdf"
}
#em geral um banco de dados Não esta no Pthon
#um banco de dados é conectado a um banco backend
#
#criando usuario 
usuarios={}

#função cadastro
def cadastrar():
  novo_usuario = input('informe o nome do usuario')
  nova_senha = getpass.getpass('informe a senha do usuario')

# para adicionar um valor no dicionario []
#dicionario [] = chave 
  usuarios[novo_usuario] = nova_senha
  print('usuarios cadastrado com sucesso')

def login():
  usuario=input('informe o usuario')
  senha=getpass.getpass('informe a senha')

  if usuario in usuarios and usuarios[usuario]==senha:
    print('login realizado com sucesso')
  else:
    print('usuario ou senha invalidos')

#executar o sistema
while True:
    print('\n1 - Cadastrar')
    print('2 - Login')
    print('3 - Sair')
    print('')
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        cadastrar()
    elif opcao == '2':
        login()
    elif opcao == '3':
        print('Encerrando sistema...')
        break
    else:
        print('Opção inválida!')
  
