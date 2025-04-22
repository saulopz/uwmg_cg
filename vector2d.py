import pygame
import math


def grad2radians(grad: float) -> float:
    """Converte de graus para radianos"""
    return (grad * math.pi) / 180


def radians2grad(radians: float) -> float:
    """Converte de radianos para graus"""
    return (radians * 180) / math.pi


# Classe Vector2D
class Vector2D:
    """
    Classe Vector2D

    Atributos
        ---------
        x: float
            Coordenada x do vetor.
        y: float
            Coordenada y do vetor.
    """

    def __init__(self, x: float, y: float):
        """Construtor da classe Vector2D."""
        self.x: float = x
        self.y: float = y

    def clone(self) -> "Vector2D":
        """Clona o vetor, retornando outro com os mesmos valores."""
        return Vector2D(self.x, self.y)

    def size(self) -> float:
        """
        Retorna o tamanho do vetor, ou seja, distância euclidiana
        da sua origem (0, 0) até o ponto (x, y).
        """
        return math.sqrt((self.x * self.x) + (self.y * self.y))

    def scale(self, scalar: float) -> None:
        """Redimensiona o vetor"""
        self.x *= scalar
        self.y *= scalar

    def add(self, other: "Vector2D") -> None:
        """Soma outo vetor ao objeto atual."""
        self.x += other.x
        self.y += other.y

    @staticmethod
    def sum(a: "Vector2D", b: "Vector2D") -> "Vector2D":
        """
        Método estático que soma dois vetores e retorna
        um novo com o resultado.
        """
        return Vector2D(a.x + b.x, a.y + b.y)

    def multiply(self, other: "Vector2D") -> None:
        """Multiplica esse vetor a outro."""
        self.x *= other.x
        self.y *= other.y

    @staticmethod
    def multiply_vectors(a: "Vector2D", b: "Vector2D") -> "Vector2D":
        """
        Método estático que multiplica dois vetores e retorna um novo
        com o resultado da operação.
        """
        return Vector2D(a.x * b.x, a.y * b.y)

    def normalize(self) -> "Vector2D":
        """
        Retorna um novo vetor, apartir do atual, normalizado, ou seja,
        de tamanho 1.
        """
        s: float = self.size()
        return Vector2D(self.x / s, self.y / s)

    @staticmethod
    def by_size_and_angle(size: float, angle: float) -> "Vector2D":
        """
        Método estático que cria um vetor com base no tamanho e
        ângulo que se quer para ele.
        """
        radians = math.radians(angle)  # Converte graus para radianos
        return Vector2D(math.cos(radians) * size, math.sin(radians) * size)

    def angle(self) -> float:
        """Retorna o ângulo do vetor em radianos."""
        return math.atan2(self.y, self.x)  # Retorna o ângulo em radianos

    def rotate(self, angle: float) -> "Vector2D":
        """Rotaciona um vetor conforme o ângulo (em radianos)."""

        # Calculando o seno e o cosseno uma única vez
        s = math.sin(angle)
        c = math.cos(angle)

        # Fórmula de rotação
        new_x = (self.x * c) - (self.y * s)
        new_y = (self.x * s) + (self.y * c)

        # Atualizando as coordenadas do vetor
        self.x = new_x
        self.y = new_y

        # Retorna o próprio objeto para encadeamento de métodos
        # (ex: v.rotate(...).rotate(...))
        return self

    def dot(self, other: "Vector2D") -> float:
        """Calcula o produto escalar entre este vetor e outro vetor."""
        return (self.x * other.x) + (self.y * other.y)

    def angle_between(self, other: "Vector2D") -> float:
        """
        Retorna o ângulo, em radianos, do vetor atual em relação
        a outro vetor.
        """
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

        # Retornar o ângulo positivo ou negativo dependendo do sinal
        # do produto escalar
        return ang if cross >= 0 else -ang

    def get(self) -> tuple:
        """Retorna a tupla (x, y) do vetor."""
        return (self.x, self.y)

    def __repr__(self) -> str:
        """Retorna uma representação do vetor no formato string."""
        return f"Vector2D(x={self.x:.2f}, y={self.y:.2f})"

    def show(self, surface: pygame.Surface, color=(255, 0, 0), origin=None, scale=1.0, width=2) -> None:
        """
        Desenha o vetor na tela.

        Parametros
        ----------
        surface: pygame.Surface
            Superfície onde o vetor será desenhado.
        color: pygame.Color
            Cor do vetor (padrão: vermelho).
        origin: tuple
            Ponto de origem do vetor (padrão: centro da superfície).
        scale: float
            Fator de escala do vetor (padrão: 1.0).
        width: int
            Largura da linha do vetor (padrão: 2).
        """
        if origin is None:
            origin = (surface.get_width() // 2, surface.get_height() // 2)

        end_x = origin[0] + self.x * scale
        end_y = (
            origin[1] - self.y * scale
        )  # invertido porque no pygame o y cresce pra baixo

        pygame.draw.line(surface, color, origin, (end_x, end_y), width)

        # Opcional: desenhar um pequeno círculo na ponta
        pygame.draw.circle(surface, color, (int(end_x), int(end_y)), 4)
