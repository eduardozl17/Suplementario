from abc import ABC, abstractmethod

# Clase base
class Empleado(ABC):
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    @abstractmethod
    def calcular_salario(self):
        pass


# Empleado a tiempo completo
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self.bono = bono

    def calcular_salario(self):
        return self.salario_base + self.bono


# Empleado a medio tiempo
class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre, salario_base=0)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora


# ---- PROGRAMA PRINCIPAL ----
empleados = [
    EmpleadoTiempoCompleto("Enzo", 482, 118),
    EmpleadoMedioTiempo("Aitana", 150, 2),
    EmpleadoTiempoCompleto("Lionel", 850, 150)
]

for empleado in empleados:
    print(f"{empleado.nombre} gana ${empleado.calcular_salario()}")
input("Presiona Enter para salir...")