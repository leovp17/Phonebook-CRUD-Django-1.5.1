from django.conf.urls import patterns, url

from magazine.views.views_noticias import NoticiaCreate, NoticiaList, NoticiaDetail, NoticiaUpdate, NoticiaDelete
from magazine.views.views_reportero import ReporteroCreate, ReporteroList
from magazine.views.views_editores import EditorCreate, EditorList
from magazine.views.views_directores import DirectorCreate, DirectorList
from magazine.views import views_common
from magazine.views.views_roles import RoleManager
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',

                       url(r'^noticia/add/$', login_required(NoticiaCreate.as_view()),name="noticia_add"),
                       url(r'^noticia/list/$', NoticiaList.as_view(), name="noticia_list"),
                       url(r'^noticia/detail/(?P<pk>[\d-]+)/$', NoticiaDetail.as_view(), name="noticia_detail"),
                       url(r'^noticia/update/(?P<pk>[\d-]+)/$', login_required(NoticiaUpdate.as_view()), name="noticia_update"),
                       url(r'^noticia/delete/(?P<pk>[\d-]+)/$', login_required(NoticiaDelete.as_view()), name="noticia_delete"),

                       url(r'^reportero/add/$', login_required(ReporteroCreate.as_view()), name="reportero_add"),
                       url(r'^reportero/list/$', ReporteroList.as_view(), name="reportero_list"),

                       url(r'^editor/add/$', login_required(EditorCreate.as_view()), name="editor_add"),
                       url(r'^editor/list/$', EditorList.as_view(), name="editor_list"),

                       url(r'^director/add/$', login_required(DirectorCreate.as_view()), name="director_add"),
                       url(r'^director/list/$', DirectorList.as_view(), name="director_list"),

                       url(r'^index/$', views_common.index, name="index"),


                       url(r'^role/manager/(?P<action>\D+)/$', RoleManager.as_view(), name="role_manager")

)

