from .models import Estudiante, Profesor, Curso, Direccion, EstudianteCurso, ProfesorCurso
from datetime import date

def crear_curso(nombre, version):
    curso = Curso(
        nombre_curso=nombre,
        version_curso=version
    )
    curso.save()

def crear_profesor(rut, nombre, apellido, creado_por):
    profesor = Profesor(
        rut=rut,
        nombre_prof=nombre,
        apellido_prof=apellido,
        activo_prof = False,
        creacion_registro_prof = date.today(),
        modificacion_registro_prof = date.today(),
        creado_por_prof=creado_por
    )
    profesor.save()

def crear_estudiante(rut, nombre, apellido, fecha_nac, creado_por):
    estudiante=Estudiante(
        rut = rut,
        nombre = nombre,
        apellido = apellido,
        fecha_nac = fecha_nac,
        activo = False,
        creacion_registro = date.today(),
        modificacion_registro = date.today(),
        creado_por = creado_por
    )

    estudiante.save()

def crear_direccion(calle, numero, dpto, comuna, ciudad, region, rut):
    estudiante = Estudiante.objects.get(rut=rut)
    direccion = Direccion(
        calle = calle,
        numero = numero,
        dpto = dpto,
        comuna = comuna,
        ciudad = ciudad,
        region = region,
        rut = estudiante
    )
    direccion.save()

def obtiene_estudiante(rut):
    return Estudiante.objects.get(rut=rut)

def obtiene_profesor(rut):
    return Profesor.objects.get(rut=rut)

def obtiene_curso(curso_id):
    return Curso.objects.get(curso_id=curso_id)

def agregar_profesor_curso(rut, curso_id):
    profesor =Profesor.objects.get(rut=rut)
    curso = Curso.objects.get(curso_id=curso_id)
    curso.profesores.add(profesor)

def agregar_cursos_a_estudiante(rut, curso_id):
    estudiante = Estudiante.objects.get(rut=rut)
    curso = Curso.objects.get(curso_id=curso_id)
    estudiante.cursos.add(curso) 

def imprime_estudiante_cursos():
    estudiante_cursos = EstudianteCurso.objects.all()
    print("Listado de estudiantes")
    for estudiante_curso in estudiante_cursos:
        estudiante = estudiante_curso.rut
        curso = estudiante_curso.curso
        print(f"Estudiante: {estudiante.nombre}, Curso: {curso.nombre_curso}")


