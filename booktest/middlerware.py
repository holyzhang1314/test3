

class Mw1(object):

    def __init__(self):
        print ('Mw1 init')

    def process_request(self,request):
        print ('Mw1 process_request')

    def process_view(self,request,view_func,*view_args,**view_kwargs):
        print ('Mw1 process_view')

    def process_response(self,request,response):
        print ('Mw1 process_response')
        return response

