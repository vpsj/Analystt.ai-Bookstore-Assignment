import React, { Component } from 'react';
import BookService from './services/BookService';

class BookList extends Component {

    state = {
        books: [],
        searchTerm: ''
    };

    componentDidMount() {
        this.getBooks();
    }

    getBooks() {
        BookService.getBooks().then(books => {
            this.setState({ books });
        });
    }

    handleChange = (event) => {
        this.setState({ searchTerm: event.target.value });
    }

    handleSearch = (event) => {
        event.preventDefault();
        this.setState({
            books: this.state.books.filter(book => book.title.toLowerCase().includes(this.state.searchTerm.toLowerCase()))
        });
    }

    render() {
        return (
            <div>
                <h1>Book List</h1>
                <input
                    type="text"
                    placeholder="Search for books"
                    value={this.state.searchTerm}
                    onChange={this.handleChange}
                />
                <button onClick={this.handleSearch}>Search</button>
                <ul>
                    {this.state.books.map(book => (
                        <li key={book.id}>{book.title}</li>
                    ))}
                </ul>
            </div>
        );
    }
}

export default BookList;
