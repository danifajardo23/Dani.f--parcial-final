class nodo:
    def __init__(self,data):
        self.data =data
        self.data =None  #puntero q apunta al siguente

class colaEnlazada:
    def __init__(self):
        self.front =None
        self.rear =None
        self._size = 0
        
    def esta_vacia(self):
        return self.front is None
#nodo:elemento de la cola 
#lifo
    def encolar(self, item):
        nuevo_nodo = nodo(item) #define una instancia de un nodo
        if self.rear is None:
            self.front = self.rear = nuevo_nodo
        else:
            self.rear.next = nuevo_nodo
            self.rear = nuevo_nodo
        self._size += 1

#verifica si hay guarda y verifica el primero ve si puede continuar  
# importante 
    def desencolar(self):
        if self.esta_vacia():
            return None
        temp = self.front
        self.front =temp.next
        if self.front is None:
            self.rear =None
        self._size -= 1
        return temp.data 
    
    def frente(self):
        if self.esta_vacia():
            return None
        return self.front.data
    
    def size (self):
        return self._size
    
    def rotar(self, n=1):
        if self.esta_vacia() or self._size == 1 :
            return
        
        for _ in range(n):
            if self.esta_vacia():
                break
            elemento = self.desencolar()
            self.encolar(elemento)


#interfaz grafica
import tkinter as tk
from tkinter import messagebox

cola = colaEnlazada()

def agregar():
    cancion = entry.get()
    if cancion:
        cola.encolar(cancion)
        entry.delete(0, tk.END)  
        actualizar_estado()
        messagebox.showinfo("Agregada", f"Canción '{cancion}' agregada a la cola.")

def desencolar():
    cancion = cola.desencolar()
    if cancion is not None:
        actualizar_estado()
        messagebox.showinfo("Quitada", f"Canción '{cancion}' quitada de la cola.")    

def actualizar_estado():
    if cola.esta_vacia():
        estado_label.config(text="Cola vacía")
    else:
        estado_label.config(text=f"Reproduciendo: {cola.frente()} | Canciones en cola: {cola.size()}")


#root = tk.Tk()
#root.title("LISTA DE CANCIONES")
#root.geometry("400x300")

#tk.Label(root, text="Elemento a agregar:").pack(pady=5)
#entry = tk.Entry(root)
#entry.pack(pady=5)

#tk.Button(root, text="agregar elemento", command=agregar).pack(pady=5)
#tk.Button(root, text="actualizar lista", command=actualizar_estado).pack(pady=5)

#estado_label = tk.Label(root, text="Cola vacía")
#estado_label.pack(pady=10)

#root.mainloop()

root = tk.Tk()
root.title("LISTA DE REPRODUCCIÓN")
root.geometry("450x350")

tk.Label(root, text="Nombre de la canción:").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Agregar Canción", command=agregar).pack(pady=5)
tk.Button(root, text="Quitar Canción", command=desencolar).pack(pady=5)
#tk.Button(root, text="Ver Próxima", command=ver_frente).pack(pady=5)
#tk.Button(root, text="Reproducir", command=reproducir).pack(pady=5)
tk.Button(root, text="Salir", command=root.quit).pack(pady=5)

estado_label = tk.Label(root, text="Lista de reproducción vacía")
estado_label.pack(pady=10)


root.mainloop()