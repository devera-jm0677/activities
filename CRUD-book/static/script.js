let table;
let isEditMode = false;
let currentISBN = null;

$(document).ready(function() {
    // Initialize DataTable
    table = $('#booksTable').DataTable({
        ajax: {
            url: '/api/books',
            dataSrc: ''
        },
        columns: [
            { data: 'isbn' },
            { data: 'title' },
            { data: 'publisher' },
            { 
                data: 'category',
                render: function(data) {
                    let badgeClass = '';
                    if (data === 'Fiction') badgeClass = 'bg-success';
                    else if (data === 'Art & Painting') badgeClass = 'bg-info';
                    else if (data === 'History') badgeClass = 'bg-warning';
                    return `<span class="badge ${badgeClass}">${data}</span>`;
                }
            },
            {
                data: null,
                className: 'text-center',
                render: function(data) {
                    return `
                        <button class="btn btn-sm btn-warning edit-btn" data-isbn="${data.isbn}" title="Edit">
                            <i class="fas fa-edit"></i>
                        </button>
                        <button class="btn btn-sm btn-danger delete-btn" data-isbn="${data.isbn}" title="Delete">
                            <i class="fas fa-trash"></i>
                        </button>
                    `;
                }
            }
        ],
        order: [[0, 'asc']],
        pageLength: 10,
        language: {
            search: "_INPUT_",
            searchPlaceholder: "Search books..."
        }
    });

    // Add Book Button
    $('#addBookBtn').click(function() {
        isEditMode = false;
        currentISBN = null;
        $('#modalTitle').text('Add New Book');
        $('#bookForm')[0].reset();
        $('#isbn').prop('disabled', false);
        $('#bookModal').modal('show');
    });

    // Edit Book Button
    $(document).on('click', '.edit-btn', function() {
        const isbn = $(this).data('isbn');
        
        // Find the book data from the table
        const rowData = table.row($(this).closest('tr')).data();
        
        isEditMode = true;
        currentISBN = isbn;
        $('#modalTitle').text('Edit Book');
        
        // Populate form
        $('#isbn').val(rowData.isbn).prop('disabled', true);
        $('#title').val(rowData.title);
        $('#publisher').val(rowData.publisher);
        $(`input[name="category"][value="${rowData.category}"]`).prop('checked', true);
        
        $('#bookModal').modal('show');
    });

    // Delete Book Button
    $(document).on('click', '.delete-btn', function() {
        const isbn = $(this).data('isbn');
        const rowData = table.row($(this).closest('tr')).data();
        
        Swal.fire({
            title: 'Are you sure?',
            text: `Do you want to delete "${rowData.title}"?`,
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#dc3545',
            cancelButtonColor: '#6c757d',
            confirmButtonText: 'Yes, delete it!',
            cancelButtonText: 'Cancel'
        }).then((result) => {
            if (result.isConfirmed) {
                deleteBook(isbn);
            }
        });
    });

    // Save Book Button
    $('#saveBookBtn').click(function() {
        if (!$('#bookForm')[0].checkValidity()) {
            $('#bookForm')[0].reportValidity();
            return;
        }

        const bookData = {
            isbn: parseInt($('#isbn').val()),
            title: $('#title').val(),
            publisher: $('#publisher').val(),
            category: $('input[name="category"]:checked').val()
        };

        if (isEditMode) {
            updateBook(currentISBN, bookData);
        } else {
            addBook(bookData);
        }
    });
});

// Add Book Function
function addBook(bookData) {
    $.ajax({
        url: '/api/books',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(bookData),
        success: function(response) {
            $('#bookModal').modal('hide');
            table.ajax.reload();
            
            Swal.fire({
                icon: 'success',
                title: 'Added!',
                text: 'Book has been added successfully.',
                showConfirmButton: false,
                timer: 1500
            });
        },
        error: function(xhr) {
            Swal.fire({
                icon: 'error',
                title: 'Error!',
                text: xhr.responseJSON.error || 'Failed to add book.'
            });
        }
    });
}

// Update Book Function
function updateBook(isbn, bookData) {
    $.ajax({
        url: `/api/books/${isbn}`,
        type: 'PUT',
        contentType: 'application/json',
        data: JSON.stringify(bookData),
        success: function(response) {
            $('#bookModal').modal('hide');
            table.ajax.reload();
            
            Swal.fire({
                icon: 'success',
                title: 'Updated!',
                text: 'Book has been updated successfully.',
                showConfirmButton: false,
                timer: 1500
            });
        },
        error: function(xhr) {
            Swal.fire({
                icon: 'error',
                title: 'Error!',
                text: 'Failed to update book.'
            });
        }
    });
}

// Delete Book Function
function deleteBook(isbn) {
    $.ajax({
        url: `/api/books/${isbn}`,
        type: 'DELETE',
        success: function(response) {
            table.ajax.reload();
            
            Swal.fire({
                icon: 'success',
                title: 'Deleted!',
                text: 'Book has been deleted successfully.',
                showConfirmButton: false,
                timer: 1500
            });
        },
        error: function(xhr) {
            Swal.fire({
                icon: 'error',
                title: 'Error!',
                text: 'Failed to delete book.'
            });
        }
    });
}