import pygame
import math

# Converte graus para radianos
def grad2radians(grad: float) -> float:
    return (grad * math.pi) / 180

# Converte radianos para graus
def radians2grad(radians: float) -> float:
    return (radians * 180) / math.pi

# Classe Vector2D
class Vector2D:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y
    
    def clone(self) -> "Vector2D":
        return Vector2D(self.x, self.y)
    
    def size(self) -> float:
        return math.sqrt((self.x * self.x) + (self.y * self.y))

    def scale(self, scalar: float):
        self.x *= scalar
        self.y *= scalar
    
    def add(self, other: "Vector2D") -> None:
        self.x += other.x
        self.y += other.y

    @staticmethod
    def sum(a: "Vector2D", b: "Vector2D") -> "Vector2D":
        return Vector2D(a.x + b.x, a.y + b.y)
    
    def multiply(self, other: "Vector2D") -> None:
        self.x *= other.x
        self.y *= other.y

    @staticmethod
    def multiply_vectors(a: "Vector2D", b: "Vector2D") -> "Vector2D":
        return Vector2D(a.x * b.x, a.y * b.y)
    
    def normalize(self) -> "Vector2D":
        s: float = self.size()
        return Vector2D(self.x / s, self.y / s)
    
    @staticmethod
    def by_size_and_angle(size: float, angle: float) -> "Vector2D":
        radians = math.radians(angle)  # Converte graus para radianos
        return Vector2D(math.cos(radians) * size, math.sin(radians) * size)
    
    def angle(self) -> float:
        return math.atan2(self.y, self.x) # Retorna o ângulo em radianos
    
    def rotate(self, angle: float):
        # Calculando o seno e o cosseno uma única vez
        s = math.sin(angle)
        c = math.cos(angle)

        # Fórmula de rotação
        new_x = (self.x * c) - (self.y * s)
        new_y = (self.x * s) + (self.y * c)

        # Atualizando as coordenadas do vetor
        self.x = new_x
        self.y = new_y

        return self  # Retorna o próprio objeto para encadeamento de métodos
                     # (ex: v.rotate(...).rotate(...))
        
    def dot(self, other: "Vector2D") -> float:
        """
        Calcula o produto escalar entre este vetor e outro vetor.
        Fórmula: A · B = Ax * Bx + Ay * By
        """
        return (self.x * other.x) + (self.y * other.y)
    
    def angle_between(self, other: "Vector2D") -> float:
        dp = self.dot(other)
        size_product = self.size() * other.size()
        # Evita divisão por zero caso um dos vetores tenha tamanho zero
        if size_product == 0:
            return 0.0  # ou talvez levantar exceção

        # Garantir que o valor do produto escalar esteja entre -1 e 1
        cos_angle = dp / size_product
        cos_angle = max(-1.0, min(1.0, cos_angle))  # clamp

        # Calcular o ângulo em radianos
        ang = math.acos(cos_angle)

        # Produto vetorial 2D para decidir o sinal
        cross = self.x * other.y - self.y * other.x

        # Retornar o ângulo positivo ou negativo dependendo do sinal do produto escalar
        return ang if cross >= 0 else -ang
    
    def get(self):
        return (self.x, self.y)
    
    def __repr__(self) -> str:
        return f"Vector2D(x={self.x:.2f}, y={self.y:.2f})"

    def show(self, surface: pygame.Surface, color=(255, 0, 0), origin=None, scale=1.0, width=2) -> None:
        if origin is None:
            origin = (surface.get_width() // 2, surface.get_height() // 2)

        end_x = origin[0] + self.x * scale
        end_y = origin[1] - self.y * scale  # invertido porque no pygame o y cresce pra baixo

        pygame.draw.line(surface, color, origin, (end_x, end_y), width)

        # Opcional: desenhar um pequeno círculo na ponta
        pygame.draw.circle(surface, color, (int(end_x), int(end_y)), 4)

