from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^thanks/$',TemplateView.as_view(template_name="notes/thanks.html"), name='thanks'),
    url(r'^ajax/validate/$','notes.utils.validate_generic',{'formclass': 'notes.forms.NoteForm'}),
    url(r'^$', 'notes.views.home', name='home'),
    # url(r'^ajax_modelform/', include('ajax_modelform.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
