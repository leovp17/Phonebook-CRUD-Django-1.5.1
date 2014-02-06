from django.views.generic.base import TemplateView
from magazine.models import Noticia
import rbac.acl

class RoleManager(TemplateView):
    template_name = 'roles/manager.html'

    def get(self, request, action, *args, **kwargs):

        acl = rbac.acl.Registry()
        if action == 'generate-roles':
            print 'Generating roles...'
            acl.add_role("InternUsers")
            print "\t Added Role: InternUsers"
            acl.add_role("Directors",["InternUsers"])
            print "\t Added Role: Directors"
            acl.add_role("Writers",["InternUsers"])
            print "\t Added Role: Writers"
            acl.add_role("Auditors",["InternUsers"])
            print "\t Added Role: Auditors"
            acl.add_role("ExternUsers")
            print "\t Added Role: ExternUsers"
            print "\t\t[Done]"
            #TODO [POM] Agregar usuarios creados a roles como hojas del arbol

        elif action == 'generate-resources':
            print 'Generating resources...'
            acl.add_resource("noticia")
            print "\t Added Resource: Noticia"
            noticias = Noticia.objects.all()
            for noticia in noticias:
                acl.add_resource("noticia-"+noticia.title, ["noticia"])
                print "\t Added Resource: noticia-%s" % noticia.title
            print "\t\t[Done]"


        elif action == 'generate-rules':
            print 'Generating rules...'
            acl.allow("InternUsers","read","noticia")
            print "\tInternUsers can read noticia"
            acl.allow("Writers","write","noticia")
            print "\tWriters can write noticia"
            acl.allow("Auditors","update","noticia")
            print "\tAuditors can update noticia"
            acl.allow("Auditors","delete","noticia")
            print "\tAuditors can delete noticia"

            acl.deny("ExternUsers","write","noticia")
            print "\tExternUsers can not write noticia"
            acl.deny("ExternUsers","update","noticia")
            print "\tExternUsers can not update noticia"
            acl.deny("ExternUsers","delete","noticia")
            print "\tExternUsers can not delete noticia"

            print "\t\t[Done]"
            #TODO [POM] Permitir a usuarios que compartan la misma revista, que compartan el mismo permiso

        elif action == 'test-onthefly':
            print 'Generating roles...'
            acl.add_role("InternUsers")
            print "\t Added Role: InternUsers"
            acl.add_role("Directors",["InternUsers"])
            print "\t Added Role: Directors"
            acl.add_role("Writers",["InternUsers"])
            print "\t Added Role: Writers"
            acl.add_role("Auditors",["InternUsers"])
            print "\t Added Role: Auditors"
            acl.add_role("ExternUsers")
            print "\t Added Role: ExternUsers"
            print "\t\t[Done]"


            print 'Generating resources...'
            acl.add_resource("noticia")
            print "\t Added Resource: Noticia"
            noticias = Noticia.objects.all()
            for noticia in noticias:
                acl.add_resource("noticia-"+noticia.title, ["noticia"])
                print "\t Added Resource: noticia-%s" % noticia.title
            print "\t\t[Done]"

            print 'Generating rules...'
            acl.allow("InternUsers","read","noticia")
            print "\tInternUsers can read noticia"
            acl.allow("Writers","write","noticia")
            print "\tWriters can write noticia"
            acl.allow("Auditors","update","noticia")
            print "\tAuditors can update noticia"
            acl.allow("Auditors","delete","noticia")
            print "\tAuditors can delete noticia"

            acl.deny("ExternUsers","write","noticia")
            print "\tExternUsers can not write noticia"
            acl.deny("ExternUsers","update","noticia")
            print "\tExternUsers can not update noticia"
            acl.deny("ExternUsers","delete","noticia")
            print "\tExternUsers can not delete noticia"

            print "\t\t[Done]"

            if acl.is_allowed("Auditors","write","noticia"):
                print "Auditors can write noticia"
            else:
                print "Auditors can not write noticia"

        else:
            print 'Command unknown.'

        return super(RoleManager,self).get(self,request,*args,**kwargs)


