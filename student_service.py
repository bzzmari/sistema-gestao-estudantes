import pickle
from datetime import datetime
from student import Student

students = []
buffer = []

def add_to_buffer(message):
    # Esta função regista uma ação na memória (buffer) juntamente com a data e hora exatas.
    # Não guarda no disco ainda, apenas na lista temporária.
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    buffer.append(f"[{timestamp}] {message}")

def register_student():
    # Esta função solicita os dados ao utilizador através do terminal.
    student_id = input("ID do Estudante: ")
    name = input("Nome: ")
    nota = input("Nota: ")
    turma = input("Turma: ")
    
    # Utiliza o "molde" (a classe Student) para criar um novo aluno com os dados inseridos.
    student = Student(student_id, name, nota, turma)
    
    # Guarda o aluno recém-criado na lista de estudantes.
    students.append(student)
    
    # Regista esta operação no histórico usando a função  acima.
    add_to_buffer(f"Student registered: {name}")
    print("\nEstudante registado com sucesso!\n")

# Repara que o "def" volta para a margem esquerda
def list_students():
    # O código dentro da função leva um recuo (espaço/Tab)
    print("\n--- Lista de Estudantes ---")
    if not students:
        print("Nenhum estudante registado.")
    else:
        for student in students:
            print(student)
    print("---------------------------\n")

def remove_student():
    # Pede o ID ao utilizador e procura esse ID na lista de estudantes para o remover.
    student_id = input("Insira o ID do estudante a remover: ")
    
    for student in students:
        if student.student_id == student_id:
            students.remove(student)
            
            # Regista a ação de remoção no histórico (buffer)
            add_to_buffer(f"Student removed: {student.name}")
            print(f"\nEstudante {student.name} removido com sucesso!\n")
            return # Sai da função imediatamente após encontrar e remover
            
    print("\nEstudante não encontrado!\n")

def save_buffer():
    # Guarda todas as operações que estão na memória num ficheiro de texto permanente.
    if not buffer:
        print("Não há novas operações para guardar.")
        return
        
    # Abre o ficheiro 'operations.log' no modo 'a' (append), que adiciona texto no final sem apagar o que já lá está.
    with open("operations.log", "a") as file:
        for operation in buffer:
            file.write(operation + "\n")
            
    # Limpa a memória (buffer) depois de guardar no disco.
    buffer.clear()
    print("Registo de operações guardado com sucesso!")

def export_students():
    # Guarda a lista de objetos estudante num ficheiro binário usando o pickle.
    # O modo 'wb' significa "write binary" (escrever em binário).
    with open("students.pkl", "wb") as file:
        pickle.dump(students, file)
    print("\nEstudantes exportados com sucesso!\n")

def import_students():
    # Carrega os estudantes do ficheiro binário de volta para a lista do programa.
    global students # Usamos 'global' para modificar a lista 'students' que criámos no topo do ficheiro.
    try:
        # O modo 'rb' significa "read binary" (ler em binário).
        with open("students.pkl", "rb") as file:
            students = pickle.load(file)
        print("\nEstudantes importados com sucesso!\n")
    except FileNotFoundError:
        # Impede que o programa dê erro se o ficheiro ainda não existir.
        print("\nFicheiro de estudantes não encontrado. Nenhum dado importado.\n")  
        