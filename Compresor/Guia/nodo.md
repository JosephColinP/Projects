# Componente nodo

Este componente define una clase en Python llamada `Nodo`, la cual se utiliza para representar los nodos de un árbol de Huffman. Un árbol de Huffman es una estructura de datos utilizada principalmente para la codificación de datos y compresión de archivos, donde cada nodo representa un carácter y su frecuencia en el conjunto de datos a comprimir.

La clase Nodo incluye:

- Un constructor (**init**), que inicializa un nodo con un carácter y su frecuencia correspondiente. También inicializa referencias None para posibles hijos izquierdo y derecho, lo cual indica que al principio, el nodo es una hoja del árbol sin hijos.

- Un método de comparación (**lt**), que permite que los nodos sean comparados en base a su frecuencia. Esto es útil para la construcción del árbol de Huffman, que a menudo requiere la comparación de nodos para determinar su posición en la estructura del árbol.

## Código completo

```python
  class Nodo:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.freq < otro.freq
```

## Explicación

Primero se define la clase nodo para representar los nodos del árbol de huffman.

```python
  class Nodo:
```

Posteriormente se define el constructor con sus parámetros. No se declara izquierda y derecha por que al principio el nodo no tiene hijos.

```python
   def __init__(self, char, freq):
```

`self` hacer referencia a la instancia u objeto actual. Y `__init__` es la palabra clave para iniciar un constructor en python.

Posteriormente se definen los atributos de la clase:

```python
  self.char = char # Representa el caracter del nodo
  self.freq = freq # Representa la frecuencia del caracter
  self.izquierda = None # Referencia al hijo izquierdo de la raiz
  self.derecha = None # Referencia al hijo derecho de la raiz
```

Por último se define el método de comparación `__lt__` Este método sobrecarga el operador `<` para definir su comportamiento. En Python, se tiene que especificar el comportamiento de un operador cuando son clases personalizadas.

```python
  def __lt__(self, otro):
```

`otro` se utiliza para pasar otra instancia de la misma clase para compararla.

```python
  return self.freq < otro.freq
```

Compara la frecuencia del nodo actual con la frecuencia de otro nodo. Si la frecuencia del nodo actual es menor devuelve "True".
