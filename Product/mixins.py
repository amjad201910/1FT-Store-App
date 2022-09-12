






class ProductQuerySetMixin():
    def get_queryset(self, *args, **kwargs):
        print(**kwargs)
        qs = super().get_queryset(*args, **kwargs)
        filter_value =self.request.query_params.get('id',None)
        if filter_value is not None:
         qs=qs.filter(pk=filter_value)
        return qs