from django.utils import simplejson
from django.http  import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import get_mod_func


class JsonResponse(HttpResponse):
	def __init__(self,data):
		HttpResponse.__init__(self,content=simplejson.dumps(data),mimetype='application/json')


@csrf_exempt
def validate_generic(request,formclass):
	mod_name, form_name = get_mod_func(formclass)
	formclass = getattr(__import__(mod_name, {}, {}, ['']), form_name)
	form = formclass(request.POST)
	if(request.GET.has_key('field')):
		errors = form.errors.get(request.GET['field'],[])
	else:
		errors = form.errors
	return JsonResponse({'valid': not errors, 'errors': errors})