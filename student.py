class Student:
    def __init__(self, student_id, name, nota, turma): #A função def __init__ precisa estar "dentro" da class Student:
        self.student_id = student_id #Colocar as atribuições tudo na mesma linha com vírgulas vai gerar um erro de sintaxe.
        self.name = name
        self.nota = nota
        self.turma = turma

    def __str__(self):
        return f"ID: {self.student_id} | Nome: {self.name}"