from rest_framework import serializers
from .models import Book

#tells django how to convert JSON data into python data for our model

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'