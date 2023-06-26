from django.urls import path, include

from knox import views as knox_views, urls

from rest_framework.routers import DefaultRouter

from . import views



router = DefaultRouter()
router.register(r'users', views.UsersViewset, basename='user')
router.register(r'article-categories', views.ArticleCategoryViewset, basename='article-category')
router.register(r'articles', views.ArticleViewset, basename='article')
router.register(r'newsletters', views.NewsLetterViewset, basename='newsletter')
router.register(r'download-categories', views.DownloadCategoryViewset, basename='download-category')
router.register(r'downloads', views.DownloadViewset, basename='download')
router.register(r'journal-categories', views.JournalCategoryViewset, basename='journal-category')
router.register(r'journal-authors', views.JournalAuthorViewset, basename='journal-author')
router.register(r'journals', views.JournalViewset, basename='journal')
router.register(r'journal-purchases', views.JournalPurchaseViewset, basename='journal-purchase')
router.register(r'quizes', views.QuizViewset, basename='quize')
router.register(r'quiz-posts', views.QuizPostViewset, basename='quiz-post')
router.register(r'pic-of-week-images', views.PicOfWeekImageViewset, basename='pic-of-week-image')
router.register(r'pic-of-week', views.PicOfWeekViewset, basename='pic-of-week')

 
urlpatterns = [
    path('', include(router.urls)),


    path(r'auth/login/', views.LoginView.as_view()),
    path(r'auth/logout/', views.LogoutView.as_view()),
    path(r'auth/loginall/', views.KnoxLogoutAllView.as_view()),
]