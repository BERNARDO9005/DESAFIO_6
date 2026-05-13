class Alumno:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion

class Grupo:
    def __init__(self, nombre_grupo):
        self.nombre_grupo = nombre_grupo
        self.estudiantes = []

    def inscribir_alumno(self, alumno):
        self.estudiantes.append(alumno)

    def obtener_promedio(self):
        if not self.estudiantes:
            return 0
        total = sum(est.calificacion for est in self.estudiantes)
        return total / len(self.estudiantes)

    def mostrar_reporte(self):
        promedio = self.obtener_promedio()
        print(f"Grupo: {self.nombre_grupo} | Promedio Actual: {promedio:.2f}")

# --- Ejecución ---
estudiante_1 = Alumno("GADIEL", 70)
mi_grupo = Grupo("ISC-201")
mi_grupo.inscribir_alumno(estudiante_1)
mi_grupo.mostrar_reporte()              # Promedio: 70.00

print("--- Actualizando calificación del alumno ---")
estudiante_1.calificacion = 100

mi_grupo.mostrar_reporte()              # Promedio: 100.00 (correcto)