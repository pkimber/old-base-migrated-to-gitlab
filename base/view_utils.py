class BaseMixin(object):

    def get_context_data(self, **kwargs):
        context = super(BaseMixin, self).get_context_data(**kwargs)
        path = self.request.path
        if path == '/':
            path = 'home'
        context.update(dict(
            path=path,
        ))
        return context
