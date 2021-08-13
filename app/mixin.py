from django.shortcuts import redirect
class PermisosUsuario(object):
    permission_required = ''
    url_redirect = None
    def get_url_redirect(self):
        if self.url_redirect is None:
            return '/login/'
        return self.url_redirect
    def getPermision(self):
        if isinstance(self.permission_required, str):
            perms = (self.permission_required,)
        else:
            perms = self.permission_required
        return perms
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perms(self.getPermision()):
            return super().dispatch(request, *args, **kwargs)
        return redirect(self.get_url_redirect())