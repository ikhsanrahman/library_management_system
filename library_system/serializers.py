from rest_framework import serializers
from .models import Book, Student, Borrowing


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class BorrowingSerializer(serializers.ModelSerializer):
    # Add a new field to the serializer to get the number of times the book has been renewed.
    renewed_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Borrowing
        fields = "__all__"
