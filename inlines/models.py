#models.py

# -*- encoding: utf-8 -*-
from re import UNICODE
import re

from django.contrib.auth.models import User

from django.db import models
import datetime


IMP_ANOS = (

    ('2013', '2013'),
    ('2012', '2012'),
    ('2011', '2011'),
    ('2010', '2010'),
    ('2009', '2009'),
    ('2008', '2008'),
    ('2007', '2007'),
    ('2006', '2006'),
    ('2005', '2005'),
    ('2004', '2004'),
    ('2003', '2003'),
    ('2002', '2002'),
    ('2001', '2001'),
    ('2000', '2000'),
    ('1999', '1999'),
    ('1998', '1998'),
    ('1997', '1997'),
    ('1996', '1996'),
    ('1995', '1995'),
    ('1994', '1994'),
    ('1993', '1993'),
    ('1992', '1992'),
    ('1991', '1991'),
    ('1990', '1990'),
    ('1989', '1989'),
    ('1988', '1988'),
    ('1987', '1987'),
    ('1986', '1986'),
    ('1985', '1985'),
    ('1984', '1984'),
    ('1983', '1983'),
    ('1982', '1982'),
    ('1981', '1981'),
    ('1980', '1980'),
    ('1979', '1979'),
    ('1978', '1978'),
    ('1977', '1977'),
    ('1976', '1976'),
    ('1975', '1975'),
    ('1974', '1974'),
    ('1973', '1973'),
    ('1972', '1972'),
    ('1971', '1971'),
    ('1970', '1970'),
    ('1969', '1969'),
    ('1968', '1968'),
    ('1967', '1967'),
    ('1966', '1966'),
    ('1965', '1965'),
    ('1964', '1964'),
    ('1963', '1963'),
    ('1962', '1962'),
    ('1961', '1961'),
    ('1960', '1960'),
    ('1959', '1959'),
    ('1958', '1958'),
    ('1957', '1957'),
    ('1956', '1956'),
    ('1955', '1955'),
    ('1954', '1954'),
    ('1953', '1953'),
    ('1952', '1952'),
    ('1951', '1951'),
    ('1950', '1950'),
    ('1949', '1949'),
    ('1948', '1948'),
    ('1947', '1947'),
    ('1946', '1946'),
    ('1945', '1945'),
    ('1944', '1944'),
    ('1943', '1943'),
    ('1942', '1942'),
    ('1941', '1941'),
    ('1940', '1940'),
    ('1939', '1939'),
    ('1938', '1938'),
    ('1937', '1937'),
    ('1936', '1936'),
    ('1935', '1935'),
    ('1934', '1934'),
    ('1933', '1933'),
    ('1932', '1932'),
    ('1931', '1931'),
    ('1930', '1930'),
    ('1929', '1929'),
    ('1928', '1928'),
    ('1927', '1927'),
    ('1926', '1926'),
    ('1925', '1925'),
    ('1924', '1924'),
    ('1923', '1923'),
    ('1922', '1922'),
    ('1921', '1921'),
    ('1920', '1920'),
)


class Candidato(models.Model):
    nombres                     = models.CharField(max_length=100)
    apellidos                   = models.CharField(max_length=100)
    fecha_nacimiento            = models.DateField(null=True, blank=True)
    summary                     = models.TextField(max_length=200, null=True, blank=True,default=None)
    #estado_civil                = models.CharField(max_length=30, choices=ESTADO_CHOICES)
    headline                    = models.CharField(max_length=200, null=True, blank=True,default=None)
    #imagen                      = models.FileField(upload_to=get_file_path, max_length=1000, blank=True,null=True,default=None)
    activo                      = models.BooleanField(default=True)
    fecha_creacion              = models.DateTimeField(editable=False)
    fecha_modificacion          = models.DateTimeField(editable=False)
    #todo JAK a eliminar
    #referencia                  = models.ForeignKey(ParamReferencia, null=True, blank=True)
    email                       = models.EmailField()
    telefono_casa               = models.CharField(max_length=100, null=True, blank=True,default=None)
    telefono_trabajo            = models.CharField(max_length=100, null=True, blank=True,default=None)
    telefono_fax                = models.CharField(max_length=100, null=True, blank=True,default=None)
    telefono_movilpersonal      = models.CharField(max_length=100, null=True, blank=True,default=None)
    telefono_moviltrabajo       = models.CharField(max_length=100, null=True, blank=True,default=None)
    twitter                     = models.URLField(max_length=100, null=True, blank=True,default=None)
    facebook                    = models.URLField(max_length=100, null=True, blank=True,default=None)
    linkedin_url                = models.URLField(max_length=100, null=True, blank=True,default=None)
    linkedin_flag               = models.BooleanField(default=False)
    linkedin_email              = models.EmailField(null=True, blank=True)
    num_linkedin_connections    = models.IntegerField( blank=True, null=True,default=None)
    slug                        = models.SlugField(max_length=255, unique=True, null=False, blank=True)
    user                        = models.ForeignKey(User)
    date_of_hire                = models.DateField(null=True, blank=True,default=None)
    #current_performance         = models.IntegerField(choices=RATE_1_5, blank=True, null=True)
    #mobility                    = models.CharField(max_length=10, choices=YON, default=YON[0][0])

    #todo JAK revisar, A ELIMINAR SE PASA A EMPRESA-POSICION
    # si un usuario no tiene no se pinta en el PDP, error al traer datos de los charts kpi.
    #todo JAK anadido una fk a posicion para tener el brand de esa posicion. si es que hay
    #brand                       = models.ForeignKey(to='Brand', blank=True, null=True)
    #general_data                = models.ForeignKey(to='Brand', null=True, blank=True, related_name='total2')
    #pais_nacimiento             = models.ForeignKey(to='ParamPais', related_name='pais_nacimiento',default=DEF_PARAMPAIS)
    #pais_residencia             = models.ForeignKey(to='ParamPais',related_name='pais_residencia', default=DEF_PARAMPAIS)

    dependence                  = models.ForeignKey('self', blank=True, null=True, related_name='child')



    class Meta:
        permissions = (
            ('readonly_Candidato','Readonly Candidato'),
        )

    FileDir = 'imagenes/perfil/'


    @property
    def slughtml(self):
        return str(self.slug) + str(".html")
    """
    @property
    def ultimoproceso(self):
        return self.proceso_set.latest('id')

    @property
    def ultimoprocesocandidato(self):
        return self.proceso_set.latest('id').procesocandidato_set.latest('id')

    @property
    def ultimoestudio(self):
        return self.formacion_set.latest('start_date')

    def ultimaexperiencia(self):
        return self.experiencia_set.latest('posting_date')
    """

    @property
    def edad(self):
        delta = datetime.date.today() - self.fecha_nacimiento
        if delta.days > 0:
            str = datetime.date.fromordinal(delta.days).year
        else:
            str = "0"
        return str


    #Conteo de las particiones del candidato en los procesos. No depende del usuarioya que va por el id del candidato

    """
    @property
    def participaciones(self):
        str = ProcesoCandidato.objects.filter(candidato__id=self.id).count()
        return str

    @property
    def agregadohace(self):
        today = datetime.date.today()
        if self.fecha_creacion != None:
            plazo = ((today - self.fecha_creacion.date()).days)
        else:
            plazo = None
        return plazo
    """


class Formacion(models.Model):
    #standart

    fecha_creacion              = models.DateTimeField(editable=False, default=datetime.datetime.today())
    fecha_modificacion          = models.DateTimeField(editable=False, default=datetime.datetime.today())
    #modelo linkedin_old
    school_name                 = models.CharField(max_length=400, null=True,blank=True) #the name of the school, as indicated by the member
    degree                      = models.CharField(max_length=400, null=True, blank=True) #a string describing the degree, if any, received at this institution
    field_of_study              = models.CharField(max_length=400) #the field of study at the school, as indicated by the member
    start_date                  = models.CharField(max_length=4,choices=IMP_ANOS) #a structured object a year field indicating when the education began
    end_date                    = models.CharField(max_length=4, choices=IMP_ANOS) #a structured object with a year field indicating when the education ended
    activities                  = models.CharField(max_length=400, null=True, blank=True) #a string describing activities the member was involved in while a student at this institution
    notes                       = models.CharField(max_length=400, null=True,  blank=True) #a string describing other details on the member's studies.
    #todo JAK no se qu es...
    #source                      = models.IntegerField(default=0, null=True, blank=True)
    #todo JAK eliminar, es el pais del centro donde se curso el estudio , estara parametrizado en param_pais.
    #place                       = models.CharField(max_length=400, null=True, blank=True) # es el pais del estudio

    candidato                   = models.ForeignKey(to='Candidato')
    #paisformacion               = models.ForeignKey(to='ParamPais', default=DEF_PARAMPAIS)
    #tipoformacion               = models.ForeignKey(to='TipoFormacion', default=DEF_PARAMPAIS)
    #perfilpersona               = models.ForeignKey(to='PerfilPersona',null=True,blank=True)
    class Meta:
        permissions = (
            ('readonly_Formacion','Readonly Formacion'),
        )

    class Meta:
        ordering = ['-start_date']
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.fecha_creacion = datetime.datetime.today()
        self.fecha_modificacion = datetime.datetime.today()
        super(Formacion, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.field_of_study
    class Admin:
        pass