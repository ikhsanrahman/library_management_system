from django.shortcuts import render
from rest_framework import viewsets
from .models import Book, Student, Borrowing
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import BookSerializer, StudentSerializer, BorrowingSerializer
from django.core.exceptions import ValidationError
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['title']

    def get_queryset(self):
        return Book.objects.all()


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['firstname']


class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['book']

    def create(self, request, *args, **kwargs):
	    # Get the student who is borrowing the book.
	    student_id = request.data.get("student")[0]
	    book_id = request.data.get("book")[0]
	    student = Student.objects.filter(id=student_id)
	    # check if student doesnot exist
	    if not student:
	    	return Response({
	            'message': f'There is student id: {student_id} available.'
	        })
	    book = Book.objects.filter(id=book_id)
	    # check if book doesnot exist
	    if not book:
	    	return Response({
	            'message': f'There is book id: {book_id} available.'
	        })
	    # check if student has borrow the same book
	    has_borrowed = Borrowing.objects.filter(student=student_id, book=book_id)
	    if has_borrowed:
	    	return Response({
	            'message': f'There is book id: {book_id} has been borrowed by student id: {student_id}.'
	        })
	    # Get the number of books that the student is already borrowing.
	    borrowings_count = Borrowing.objects.filter(student=student_id).count()
	    # If the student is already borrowing 10 books, then raise an error.
	    if borrowings_count >= 10:
	        raise ValidationError({
	            'message': 'You can only borrow up to 10 books.'
	        })

	    return super().create(request, *args, **kwargs)
