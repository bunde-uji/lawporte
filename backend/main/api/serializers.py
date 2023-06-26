from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, Serializer, CharField, ValidationError

from . import models

from django.contrib.auth import authenticate


ALL_FIELDS = '__all__'


def factory(Serializer, Model, fields=None, exclude=None):
    class _FactorySerializer(Serializer):
        class Meta:
            pass

    _FactorySerializer.Meta.model = Model
    _FactorySerializer.Meta.fields = fields
    _FactorySerializer.Meta.exclude = exclude

    return _FactorySerializer



def model_serializer_factory(Model, fields=None, exclude=None):
    return factory(ModelSerializer, Model, fields, exclude)



class UserSerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
        ]

        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}



class AuthSerializer(Serializer):

    username = CharField()
    password = CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )
    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        
        user = authenticate(
            request=self.context.get('request'),
            username=username,
            password=password
        )

        if not user:
            msg = 'Invalid username or password'
            raise ValidationError(msg, code='authentication')

        attrs['user'] = user

        return attrs
    


ArticleCategorySerializer = model_serializer_factory(models.ArticleCategory, fields=ALL_FIELDS)




NewsLetterSerializer = model_serializer_factory(models.NewsLetter, fields=ALL_FIELDS)




DownloadCategorySerializer = model_serializer_factory(models.DownloadCategory, fields=ALL_FIELDS)





DownloadSerializer = model_serializer_factory(models.Download, fields=ALL_FIELDS)




JournalCategorySerializer = model_serializer_factory(models.JournalCategory, fields=ALL_FIELDS)




JournalAuthorSerializer = model_serializer_factory(models.JournalAuthor, fields=ALL_FIELDS)




JournalPurchaseSerializer = model_serializer_factory(models.JournalPurchase, fields=ALL_FIELDS)






QuizSerializer = model_serializer_factory(models.Quiz, fields=ALL_FIELDS)





PicOfWeekImageSerializer = model_serializer_factory(models.PicOfWeekImage, fields=ALL_FIELDS)




class ArticleSerializer(ModelSerializer):
    class Meta:
        model = models.Article
        fields = ALL_FIELDS


    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['category'] = ArticleCategorySerializer(instance.category).data
        return data
    








class JournalSerializer(ModelSerializer):
    class Meta:
        model = models.Journal
        fields = ALL_FIELDS
        



    def to_representation(self, instance):
        map = super().to_representation(instance)
        map['categories'] = JournalCategorySerializer(instance.categories, many=True).data
        map['authors'] = JournalAuthorSerializer(instance.authors, many=True).data
        return map





class QuizPostSerializer(ModelSerializer):
    class Meta:
        model = models.QuizPost
        fields = ALL_FIELDS


    def to_representation(self, instance):
        map = super().to_representation(instance)
        map['quiz'] = QuizSerializer(instance.quiz).data
        return map
    










class PicOfWeekSerializer(ModelSerializer):
    class Meta:
        fields = ALL_FIELDS
        model = models.PicOfWeek


    def to_representation(self, instance):
        map = super().to_representation(instance)
        map['images'] = PicOfWeekImageSerializer(instance.images, many=True).data
        return map
    

