from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET','POST'])
def index(request):
    courses = {
        'course_name':'python',
        'learn' : ['flask','Django','Tornado','FastApi'],
        'course_provider':'scaler',
    }
    return Response(courses)
