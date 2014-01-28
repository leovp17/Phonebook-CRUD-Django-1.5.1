#views.py
import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from inlines.forms import *
from inlines.models import Candidato, Formacion


def candidato_details(request, slug):

    #se obtiene los datos del proceso (ok)
    try:
        w_candidato = Candidato.objects.get(user=request.user, slug=slug)

    except ObjectDoesNotExist, e:
        raise Http404

    #formularios
    formeducation = CandidatoEstudioFormSet(instance=w_candidato, prefix="formset")

    return render_to_response('details_education_edit.html', locals(), RequestContext(request))


def show_edu(request):

    if request.is_ajax():
        jres = {}
        jres['ok'] = "ok"

        w_candidato = Candidato.objects.get(pk=request.POST.get('candidato'))


        if w_candidato.formacion_set.count() > 0:
            extra = 0
        else:
            extra = 1
        CandidatoEstudioFormSet2 = inlineformset_factory(Candidato, Formacion, extra=extra, max_num=10, can_delete=True, fields=('field_of_study', 'start_date', 'end_date', 'school_name'))

        formularioeducacion = CandidatoEstudioFormSet(instance=w_candidato, prefix='education_form', extra=extra)

        salida = render_to_string('details_education_edit.html', locals(), RequestContext(request))
        jres['data'] = salida
        jres['status'] = 'ok'

        return HttpResponse(json.dumps(jres))

    else:
        jres = {}

        jres['status'] = 'nok'
        return HttpResponse(json.dumps(jres))


def enter_edu(request):
    if request.is_ajax():
        jres = {}
        jres['ok'] = "ok"

        w_candidato=Candidato.objects.get(pk=request.POST.get('candidato'))

        CandidatoEstudioFormSet2 = inlineformset_factory(Candidato, Formacion)

        formularioeducacion = CandidatoEstudioFormSet(request.POST or None, instance=w_candidato, prefix='education_form')

        if formularioeducacion.is_valid():
            jres['status'] = 'ok'
            formularioeducacion.save()
            antecedentesacademicos = render_to_string('details_education.html', locals(), RequestContext(request))
            jres['data'] = antecedentesacademicos

        else:
            try:

                salida = render_to_string('details_education_edit.html', locals(), RequestContext(request))
                jres['data'] = salida
                jres['status'] = 'novalido'

                return HttpResponse(json.dumps(jres))
            except Exception, e:
                salida = str(e)
                jres['status'] = 'nok'
                return HttpResponse(json.dumps(jres))

        return HttpResponse(json.dumps(jres))

    else:
        jres = {}

        jres['status'] = 'nok'
        return HttpResponse(json.dumps(jres))