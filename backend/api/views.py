from rest_framework.response import Response
from rest_framework.decorators import api_view




@api_view(['GET'])
def getRoutes():
    routes = [
        'api/token',
        'api/token/refresh',
        'api/rescues/create',
        'api/recsues/all',
        'api/rescues/<int:id>',
        'api/user/login',
        'api/user/register',
        
    ]
    return Response(routes)