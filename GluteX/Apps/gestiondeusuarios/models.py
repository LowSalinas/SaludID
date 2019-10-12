from django.db import models

# Create your models here.

class Usuario(models.Model):
    Nombre = models.CharField(max_length=20)
    Apellidos = models.CharField(max_length=20)
    Fechanacimiento = models.DateField()
    Sexos=(('F', 'Femenino'), ('M', 'Masculino'))
    Sexo = models.CharField(max_length=1, choices=Sexos, default='M')
    Peso = models.PositiveSmallIntegerField()
    Estatura = models.DecimalField(max_digits=3, decimal_places=2)
    tipos = (('A', 'A+'),('B', 'A-'), ('C', 'B+'), ('D','B-'), ('E','AB+'), ('F','AB-'), ('G','O+'), ('H','O-'))
    Tipodesangre = models.CharField(max_length=1, choices=tipos, default='G')
    Observaciones = models.CharField(max_length=500)
    Foto = models.TextField()

    def nombrecompleto(self):
        return "{0} {1}".format(self.Nombre, self.Apellidos)
    
    def __str__(self):
        return self.nombrecompleto()

class Doctor(models.Model):
    Nombre = models.CharField(max_length=20)
    Apellidos = models.CharField(max_length=20)
    Hospital = models.CharField(max_length=20)
    Cedula = models.PositiveIntegerField()
    Telefono = models.PositiveIntegerField()
    Correo = models.TextField()
    Foto = models.TextField()

    def __str__(self):
        return "Dr. {0} {1}".format(self.Nombre, self.Apellidos)

class Nutriologo(models.Model):
    Nombre = models.CharField(max_length=20)
    Apellidos = models.CharField(max_length=20)
    Institucion = models.CharField(max_length=20)
    Cedula = models.PositiveIntegerField()
    Telefono = models.PositiveIntegerField()
    Correo = models.TextField()
    Foto = models.TextField() 

    def __str__(self):
        return "Ntr. {0} {1}".format(self.Nombre, self.Apellidos)

class NumID(models.Model):
    IDnumber = models.AutoField(primary_key=True)
    Usuario = models.ForeignKey(Usuario, null = False, blank = False, on_delete=models.CASCADE)
    Doctor = models.ForeignKey(Doctor, null = False, blank = False, on_delete=models.CASCADE)
    Nutriologo = models.ForeignKey(Nutriologo, null = False, blank = False, on_delete=models.CASCADE)
    FechaRegistro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{0}".format(self.IDnumber)