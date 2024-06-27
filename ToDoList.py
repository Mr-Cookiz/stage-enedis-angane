import os,time

class ToDoList:
    def __init__(self):
        self.todos = []
    def ajouterTodo (self,todo):
        self.todos.append(todo)
    def enleverTodo (self,todo):
        nombre = input("Donner la place du Todo a enlever.")
        nombre = nombre+1
        del todolist[nombre]
    def AfficherTodos (self):
        for todo in self.todos:
            todo.Afficher()
    def vider (self):
        self.todos = []
class Todo:
    def __init__(self):
        self.label = str(input("Donnez un nom au Todo"))
        self.fait = False
    def cocher (self):
        self.fait = True
    def décocher (self):
        self.fait = False
    def Afficher (self):
        print(f"{self.label} > {self.fait}")

todolist = ToDoList()

while True:
    todolist.AfficherTodos()
    menu = input("1: Ajouter\n2: Enlever\n3: Afficher\n4: Vider\n> ")
    if menu == "1":
        todo = Todo()
        todolist.ajouterTodo(todo)
    elif menu == "2":
        todolist.enleverTodo(todo)
    elif menu == "3":
        todolist.AfficherTodos()
    elif menu == "4":
        todolist.vider()
    else:
        exit()

    time.sleep(1)
    os.system("cls")