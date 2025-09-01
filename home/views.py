from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Person
from .serializers import PersonSerializer, LoginSerializer, RegisterUserSerializer, LoginUserSerializer
from rest_framework.views import APIView

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication




# Create your views here.

class RegisterAPIUser(APIView):

    def post(self, request):
        data = request.data
        serializer = RegisterUserSerializer(data=data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginAPIUser(APIView):

    def post(self, request):
        data = request.data
        serializer = LoginUserSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        user = authenticate(
            username = serializer.validated_data['username'],
            password = serializer.validated_data['password'],
        )

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token' : token.key}, status=status.HTTP_200_OK)
        
        return Response({'message' : 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class PersonClassAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def get(self, request):
        return Response({'message' : 'This ia a get method'})
    
    def post(self, request):
        return Response({'message' : 'This is a post method'})
    
    def put(self, request):
        return Response({'message' : 'This is a put method'})
    
    def patch(self, request):
        return Response({'message' : 'This is a patch method'})
    
    def delete(self, request):
        return Response({'message' : 'This is a delete method'})


        











@api_view(['GET', 'POST', 'PUT'])
def index(request):
    courses = {
        'course_name': 'Python',
        'learn': ['Flask', 'Django', 'FastAPI'],
        'course_provider': 'Scalar',
    }

    if request.method == 'GET':
        query = request.GET.get('search')
        print(query)
        return Response(courses, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        data = request.data
        print(data['Name'])
        print(data['Age'])
        return Response('', status=status.HTTP_201_CREATED)
    
    elif request.method == 'PUT':
        return Response(courses, status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'PUT', 'PATCH'])
def person_list(request):
    if request.method == 'GET':
        objs = Person.objects.all()
        searilizer = PersonSerializer(objs, many=True)
        return Response(searilizer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        data = request.data
        searilizer = PersonSerializer(data = data)

        if searilizer.is_valid():
            searilizer.save()
            return Response(searilizer.data, status=status.HTTP_201_CREATED)
        
        return Response(searilizer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def person(request, pk):
    try:
        user = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PersonSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = PersonSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = PersonSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def add_person(request):
    data = request.data
    serializer = PersonSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data=data)

    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)



    


class PeopleViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def list(self, request):
        search = request.GET.get('search')
        queryset = self.queryset

        if search:
            queryset = queryset.filter(name__startswith = search)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        