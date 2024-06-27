import os,time

class ToDoList:
    def __init__(self):
        self.todos = []
    def ajouterTodo (self,todo):
        self.todos.append(todo)
    def enleverTodo (self):
        nombre = int(input("Donner la place du Todo a enlever."))
        nombre = nombre-1
        del self.todos[nombre]
    def AfficherTodos (self):
        for todo in self.todos:
            todo.Afficher()
        print()
    def vider (self):
        self.todos = []
    def cocherTodo (self,nombre):
        self.todos[nombre].cocher()
    def decocherTodo (self,nombre):
        self.todos[nombre].decocher()
        
class Todo:
    def __init__(self):
        self.label = str(input("Donnez un nom au Todo"))
        self.fait = False
    def cocher (self):
        self.fait = True
    def decocher (self):
        self.fait = False
    def Afficher (self):
        print(f"{self.label} > {self.fait}")

todolist = ToDoList()

while True:
    todolist.AfficherTodos()
    menu = input("1: Ajouter\n2: Enlever\n3: Afficher\n4: Vider\n5: Cocher\n6: décocher\n")
    if menu == "1":
        todo = Todo()
        todolist.ajouterTodo(todo)
    elif menu == "2":
        todolist.enleverTodo()
    elif menu == "3":
        todolist.AfficherTodos()
        time.sleep(2)
    elif menu == "4":
        todolist.vider()
    elif menu == "5":
        nombre = int(input("Donner la place du Todo a cocher."))
        nombre = nombre-1
        todolist.cocherTodo(nombre)
    elif menu == "6":
        nombre = int(input("Donner la place du Todo a décocher."))
        nombre = nombre-1
        todolist.decocherTodo(nombre)
    else:
        exit()

    time.sleep(1)
    os.system("cls")