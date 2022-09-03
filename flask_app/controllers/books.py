from flask import render_template, request , redirect
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book




#routes to books page which is a form used to add a book to an author
@app.route('/books')
def display_books():
    return render_template("books.html", all_books = Book.get_all())

# route to create a book and pass that info to our database and redirects to the same page displaying the new information added by the user
@app.route('/create/book', methods=['POST'])
def create_book():
    data={
        "title":request.form['title'],
        "num_of_pages":request.form['num_of_pages']
    }
    book_id = Book.save(data)
    return redirect('/books')

@app.route('/book/<int:id>')
def show_book(id):
    data = {
        "id":id
    }
    return render_template('show_book.html', book=Book.get_by_id(data),unfavorited_authors=Author.unfavorited_authors(data))


@app.route('/join/author', methods=['POST'])
def join_book_on_author():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/book/{request.form['book_id']}")
