from django.shortcuts import render
# Create your views here.

from .models.book import Book
from .models.author import Author
from .models.book_instance import BookInstance
from .models.genre import Genre


def index(request):
    """View function for home page of site."""
    search_word = request.GET.get('search_word', '').lower()
   
   
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_genres = Genre.objects.all().count() 

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_genres = Genre.objects.filter(name__icontains=search_word).count()
    num_books = Book.objects.filter(title__icontains=search_word).count()
    
    
    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_genres': num_genres,
        'num_instances_available': num_instances_available,
        #'num_genres_available': num_genres_available,
        #'num_books_available' : num_books_available,
        'num_authors': num_authors,
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
