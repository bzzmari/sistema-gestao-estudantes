# Importa todas as funções de serviço do ficheiro student_service.py
from student_service import (
    register_student, 
    list_students, 
    remove_student, 
    export_students, 
    import_students, 
    save_buffer
)

def menu():
    # Cria um ciclo infinito para manter o menu ativo até o utilizador escolher sair
    while True:
        print("\n--- Sistema de Gestão de Estudantes ---")
        print("1: Registar Estudante")
        print("2: Listar Estudantes")
        print("3: Remover Estudante")
        print("4: Guardar Histórico (Buffer)")
        print("5: Exportar Estudantes (.pkl)")
        print("6: Importar Estudantes (.pkl)")
        print("0: Sair")
        
        option = input("Escolha uma opção: ")
        
        # Estrutura de decisão que chama a função correspondente à opção escolhida
        if option == "1":
            register_student()
        elif option == "2":
            list_students()
        elif option == "3":
            remove_student()
        elif option == "4":
            save_buffer()
        elif option == "5":
            export_students()
        elif option == "6":
            import_students()
        elif option == "0":
            print("\nA guardar histórico antes de fechar...")
            save_buffer() # Garante que nada se perde antes de fechar
            print("Programa terminado.\n")
            break # Quebra o ciclo while e encerra o programa
        else:
            print("\nOpção inválida, tente novamente.\n")

# Verifica se este é o ficheiro principal a ser executado e inicia o menu
if __name__ == "__main__":
    menu()