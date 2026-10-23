from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

def perfil_requerido(tipo):
    def decorador(view):
        @wraps(view)
        def wrapper(request, *args, **kwargs):
            perfil = getattr(request.user, "perfil_fdca", None)
            if perfil is None or perfil.tipo != tipo:
                raise PermissionDenied
            return view(request, *args, **kwargs)
        return login_required(wrapper)  
    return decorador