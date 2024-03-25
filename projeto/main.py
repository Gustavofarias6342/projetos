# main.py
from funcoes import *

def menu():
    print("\n=== Sistema de Gestão de Veículos ===")
    print("1. Cadastrar Veículo")
    print("2. Consultar Veículo")
    print("3. Listar Veículos")
    print("4. Apagar Veículo")
    print("5. Atualizar Veículo")
    print("6. Cadastrar Motorista")
    print("7. Consultar Motorista")
    print("8. Listar Motoristas")
    print("9. Atribuir Veículo a Motorista")
    print("0. Sair")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            placa = input("Digite a placa do veículo: ")
            modelo = input("Digite o modelo do veículo: ")
            ano = input("Digite o ano do veículo: ")
            cadastrar_veiculo(placa, modelo, ano)
            print("Veículo cadastrado com sucesso!")

        elif opcao == '2':
            placa = input("Digite a placa do veículo: ")
            veiculo = consultar_veiculo(placa)
            if veiculo:
                print("Veículo encontrado:")
                print(veiculo)
            else:
                print("Veículo não encontrado.")

        elif opcao == '3':
            veiculos = listar_veiculos()
            if veiculos:
                print("Lista de Veículos:")
                for placa, info in veiculos.items():
                    print(f"Placa: {placa}, Modelo: {info['modelo']}, Ano: {info['ano']}")
            else:
                print("Nenhum veículo cadastrado.")

        elif opcao == '4':
            placa = input("Digite a placa do veículo que deseja apagar: ")
            if apagar_veiculo(placa):
                print("Veículo apagado com sucesso!")
            else:
                print("Veículo não encontrado.")

        elif opcao == '5':
            placa = input("Digite a placa do veículo que deseja atualizar: ")
            modelo = input("Digite o novo modelo do veículo (ou deixe em branco para manter o mesmo): ")
            ano = input("Digite o novo ano do veículo (ou deixe em branco para manter o mesmo): ")
            if atualizar_veiculo(placa, modelo, ano):
                print("Veículo atualizado com sucesso!")
            else:
                print("Veículo não encontrado.")

        elif opcao == '6':
            cpf = input("Digite o CPF do motorista: ")
            nome = input("Digite o nome do motorista: ")
            cadastrar_motorista(cpf, nome)
            print("Motorista cadastrado com sucesso!")

        elif opcao == '7':
            cpf = input("Digite o CPF do motorista: ")
            motorista = consultar_motorista(cpf)
            if motorista:
                print("Motorista encontrado:")
                print(motorista)
            else:
                print("Motorista não encontrado.")

        elif opcao == '8':
            motoristas = listar_motoristas()
            if motoristas:
                print("Lista de Motoristas:")
                for cpf, info in motoristas.items():
                    print(f"CPF: {cpf}, Nome: {info['nome']}, Veículo: {info['veiculo']}")
            else:
                print("Nenhum motorista cadastrado.")

        elif opcao == '9':
            cpf = input("Digite o CPF do motorista: ")
            placa = input("Digite a placa do veículo: ")
            if atualizar_veiculo_motorista(cpf, placa):
                print("Veículo atribuído ao motorista com sucesso!")
            else:
                print("CPF do motorista ou placa do veículo inválidos.")

        elif opcao == '0':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
