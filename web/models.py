from django.db import models


class Curso(models.Model):
    curso_id = models.AutoField(primary_key=True)
    nombre_curso = models.CharField(max_length=50, blank=True, null=True)
    version_curso = models.IntegerField(blank=True, null=True)
    profesores = models.ManyToManyField('Profesor', through='ProfesorCurso')

    class Meta:
        managed = False
        db_table = 'curso'

class Estudiante(models.Model):
    rut = models.CharField(primary_key=True, max_length=9)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    activo = models.BooleanField(blank=True, null=True)
    creacion_registro = models.DateField(blank=True, null=True)
    modificacion_registro = models.DateField(blank=True, null=True)
    creado_por = models.CharField(max_length=50, blank=True, null=True)
    cursos = models.ManyToManyField(Curso, through='EstudianteCurso')

    class Meta:
        managed = False
        db_table = 'estudiante'


class Profesor(models.Model):
    rut = models.CharField(primary_key=True, max_length=9)
    nombre_prof = models.CharField(max_length=50)
    apellido_prof = models.CharField(max_length=50)
    activo_prof = models.BooleanField(blank=True, null=True)
    creacion_registro_prof = models.DateField(blank=True, null=True)
    modificacion_registro_prof = models.DateField(blank=True, null=True)
    creado_por_prof = models.CharField(max_length=50, blank=True, null=True)
    cursos = models.ManyToManyField(Curso, through='ProfesorCurso')

    class Meta:
        managed = False
        db_table = 'profesor'
        
class Direccion(models.Model):
    direccion_id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    dpto = models.CharField(max_length=10, blank=True, null=True)
    comuna = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    rut = models.OneToOneField(Estudiante, models.DO_NOTHING, db_column='rut')

    class Meta:
        managed = False
        db_table = 'direccion'

class EstudianteCurso(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.ForeignKey(Estudiante, models.DO_NOTHING, db_column='rut')
    curso = models.ForeignKey(Curso, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estudiante_curso'
        unique_together = ('rut', 'curso') 


class ProfesorCurso(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.ForeignKey(Profesor, models.DO_NOTHING, db_column='rut', blank=True, null=True)
    curso = models.ForeignKey(Curso, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profesor_curso'
        unique_together = ('rut', 'curso') 
