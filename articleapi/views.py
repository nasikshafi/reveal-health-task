from rest_framework.response import Response
from rest_framework import status, generics
from articleapi.models import Article
from articleapi.serializers import ArticleSerializer
import math
from datetime import datetime


class Articles(generics.GenericAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    def get_article(self, title):
        try:
            return Article.objects.get(title=title)
        except:
            return None

    def get(self, request):
        search_param = request.GET.get("search")
        articles = Article.objects.all()
        if search_param:
            articles = articles.filter(title__icontains=search_param)
        serializer = self.serializer_class(articles, many=True)
        return Response({
            "status": "success",
            "articles": serializer.data
        })

    def post(self, request):
        print (request.data)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "article": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, title):
        article = self.get_article(title)
        if article == None:
            return Response({"status": "fail", "message": f"article with title: {title} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            article, data=request.data, partial=True)
        if serializer.is_valid():   
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "article": serializer.data})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, title):
        article = self.get_article(title)
        if article == None:
            return Response({"status": "fail", "message": f"Article with title: {title} not found"}, status=status.HTTP_404_NOT_FOUND)

        article.delete()
        return Response({"status":"success","message":"record deleted successfully"},status=status.HTTP_204_NO_CONTENT)

