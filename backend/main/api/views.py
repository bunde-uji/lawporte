from . import models, serializers
from django.db.models import Count, Min, Max, Q
from django.contrib.auth import login, logout

from knox.views import LoginView as KnoxLoginView, LogoutView as KnoxLogoutView, LogoutAllView as KnoxLogoutAllView

from rest_framework import status, viewsets, decorators, response, authentication, permissions, generics, exceptions

def err_bad_request(title, msg):
    raise exceptions.NotAcceptable({title: msg}, status.HTTP_400_BAD_REQUEST)


def init_queryset(klass):
    return klass.models.filter(flag=True)


# Create your views here. 



class LoginView(KnoxLoginView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.AllowAny]


    def post(self, request, format=None):
        serializer = serializers.AuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        print(request.user and request.user.is_authenticated)
        return super().post(request, format)
    

    def get_post_response_data(self, request, token, instance):
        data = super().get_post_response_data(request, token, instance)

        staff = models.Staff.objects.filter(username=request.user.username).first()
        
        if staff:
            data['user']['organization'] = serializers.StaffSerializer(instance=staff).data['organization']

        return data




class LogoutView(KnoxLogoutView):
    def post(self, request, format=None):
        response = super().post(request, format)
        logout(request)
        return response
    





class UsersViewset(viewsets.ViewSet):
    queryset = init_queryset(models.User)
    serializer_class = serializers.UserSerializer






class ArticleCategoryViewset(viewsets.ViewSet):
    queryset = init_queryset(models.ArticleCategory)
    serializer_class = serializers.ArticleCategorySerializer






class ArticleViewset(viewsets.ViewSet):
    queryset = init_queryset(models.Article)
    serializer_class = serializers.ArticleSerializer







class NewsLetterViewset(viewsets.ViewSet):
    queryset = init_queryset(models.NewsLetter)
    serializer_class = serializers.NewsLetterSerializer






class DownloadCategoryViewset(viewsets.ViewSet):
    queryset = init_queryset(models.DownloadCategory)
    serializer_class = serializers.DownloadCategorySerializer






class DownloadViewset(viewsets.ViewSet):
    queryset = init_queryset(models.Download)
    serializer_class = serializers.DownloadSerializer






class JournalCategoryViewset(viewsets.ViewSet):
    queryset = init_queryset(models.JournalCategory)
    serializer_class = serializers.JournalCategorySerializer







class JournalAuthorViewset(viewsets.ViewSet):
    queryset = init_queryset(models.JournalAuthor)
    serializer_class = serializers.JournalAuthorSerializer






class JournalViewset(viewsets.ViewSet):
    queryset = init_queryset(models.Journal)
    serializer_class = serializers.JournalSerializer







class JournalPurchase(viewsets.ViewSet):
    queryset = init_queryset(models.JournalPurchase)
    serializer_class = serializers.JournalPurchaseSerializer







class QuizViewset(viewsets.ViewSet):
    queryset = init_queryset(models.Quiz)
    serializer_class = serializers.QuizSerializer







class QuizPostViewset(viewsets.ViewSet):
    queryset = init_queryset(models.QuizPost)
    serializer_class = serializers.QuizPostSerializer








class PicOfWeekImageViewset(viewsets.ViewSet):
    queryset = init_queryset(models.PicOfWeekImage)
    serializer_class = serializers.PicOfWeekImageSerializer






class PicOfWeekViewset(viewsets.ViewSet):
    queryset = init_queryset(models.PicOfWeek)
    serializer_class = serializers.PicOfWeekSerializer











