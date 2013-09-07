class BaseMixin(object):

    def get_context_data(self, **kwargs):
        context = super(BaseMixin, self).get_context_data(**kwargs)
        context.update(dict(
            path=self.request.path,
        ))
        return context
