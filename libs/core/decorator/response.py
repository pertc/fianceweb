import timefrom functools import wrapsfrom django.db import transactionfrom core.http.response import HttpResponsefrom utils.log import loggerfrom utils.exceptions import PubErrorCustomclass Core_connector:    def __init__(self,**kwargs):        self.transaction = kwargs.get('transaction',None)        self.pagination = kwargs.get('pagination',None)        self.serializer_class = kwargs.get('serializer_class',None)        self.model_class = kwargs.get('model_class',None)    def __request_validate(self,request,**kwargs):        if not self.serializer_class:            return kwargs        pk = kwargs.get('pk')        instance = None        if pk:            try:                instance = self.model_class.objects.get(pk=pk)            except TypeError:                raise PubErrorCustom('serializer_class类型错误')            except Exception:                raise PubErrorCustom('未找到')        serializer = self.serializer_class(data=request.data, instance=instance)        if not serializer.is_valid():            errors = [key + ':' + value[0] for key, value in serializer.errors.items() if isinstance(value, list)]            if errors:                error = errors[0]                error = error.lstrip(':').split(':')[1]            else:                for key, value in serializer.errors.items():                    if isinstance(value, dict):                        key, value = value.popitem()                        error = key + ':' + value[0]                        break            raise PubErrorCustom(error)        kwargs.setdefault('serializer',serializer)        kwargs.setdefault('instance', instance)        return kwargs    def __run(self,func,outside_self,request,*args, **kwargs):        if self.transaction:            with transaction.atomic():                res=func(outside_self, request, *args, **kwargs)        else:            res=func(outside_self, request, *args, **kwargs)        if not isinstance(res, dict):            res = {'data': [], 'msg': None, 'header': None}        if 'data' not in res:            res['data'] = None        if 'msg' not in res:            res['msg'] =  {}        if 'header' not in res:            res['header'] = None        return HttpResponse(data=res['data'], headers=res['header'], msg=res['msg'])    def __response__validate(self,outside_self,func,response):        logger.debug('[%s : %s]Training complete in %lf real seconds' % (outside_self.__class__.__name__, getattr(func, '__name__'), self.end - self.start))        return response    def __call__(self,func):        @wraps(func)        def wrapper(outside_self,request,*args, **kwargs):            try:                self.start = time.time()                kwargs=self.__request_validate(request,**kwargs)                response=self.__run(func,outside_self,request,*args, **kwargs)                self.end=time.time()                return self.__response__validate(outside_self,func,response)            except PubErrorCustom as e:                return HttpResponse(success=False, msg=e.msg, data=None)            # except Exception as e:            #     logger.error(e)            #     return HttpResponse(success=False, msg=str(e), data=None)        return wrapper