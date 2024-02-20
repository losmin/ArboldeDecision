class NodoDecision:
    def __init__(self, pregunta, opciones):
        self.pregunta = pregunta
        self.opciones = opciones  # Lista de opciones, cada una representada como (respuesta, siguiente_nodo)

# Definición del árbol de decisión
arbol_decision = NodoDecision("¿La empresa tiene un historial sólido?",
                              [("Sí", NodoDecision("¿La industria está en crecimiento?",
                                                 [("Sí", "Invertir en acciones"),
                                                  ("No", "Considerar bonos")])),
                               ("No", "No invertir")])

# Función para realizar la decisión
def tomar_decision(nodo_actual):
    print(nodo_actual.pregunta)
    
    for i, (opcion, _) in enumerate(nodo_actual.opciones, 1):
        print(f"{i}. {opcion}")
    
    seleccion = int(input("Seleccione una opción (1-" + str(len(nodo_actual.opciones)) + "): ")) - 1
    siguiente_nodo = nodo_actual.opciones[seleccion][1]
    
    if isinstance(siguiente_nodo, NodoDecision):
        return tomar_decision(siguiente_nodo)
    else:
        return siguiente_nodo

# Tomar la decisión basada en el árbol
decision = tomar_decision(arbol_decision)
print("Decisión final:", decision)
