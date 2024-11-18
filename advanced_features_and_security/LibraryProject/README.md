
---

# **Library Management System Documentation**

## **Overview**
The Library Management System is a web-based application developed using Django. It allows users to manage books, libraries, and related entities while providing role-based functionalities such as librarian and member-specific views.

---

## **Project Structure**

### **Main Directory (`LibraryProject`)**
- **manage.py**: Command-line utility for Django management.
- **db.sqlite3**: SQLite database for development.
- **README.md**: Overview of the project and setup instructions.

### **Subdirectories**
1. **LibraryProject**:
   - Core project configuration.
   - URL routing, settings, and deployment files.
2. **bookshelf**:
   - Manages book CRUD operations.
   - Contains templates for book management.
3. **relationship_app**:
   - Manages user profiles, roles, and library relationships.
   - Includes signals, queries, and templates for user interactions.

---

## **Features**

### 1. **Authentication and Authorization**
- User registration, login, and logout.
- Role-based access control (e.g., members, librarians).
- Profile management for users.

### 2. **Book Management**
- CRUD operations for books:
  - **Create**: Add new books with specific attributes.
  - **Read**: View a list of books or details of individual books.
  - **Update**: Modify existing book details.
  - **Delete**: Remove books from the system.
- User-friendly templates for each operation.

### 3. **Library Relationships**
- Manage associations between users, books, and libraries.
- Dedicated views for:
  - Librarians: Manage books and oversee library operations.
  - Members: Access book lists and personal profiles.
- Library-specific detail pages.

---

## **Setup Instructions**

### **Prerequisites**
- Python 3.x
- Django (as per the `requirements.txt` file if available)
- SQLite (default database)

### **Steps**
1. Clone the repository.
   ```bash
   git clone <repository_url>
   cd LibraryProject
   ```
2. Install dependencies.
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations.
   ```bash
   python manage.py migrate
   ```
4. Run the development server.
   ```bash
   python manage.py runserver
   ```
5. Access the application at `http://127.0.0.1:8000/`.

---

## **Database Design**

### **Bookshelf Models**
- **Book**:
  - Fields: `title`, `author`, `published_date`, `isbn`, etc.
  - Relationships: Linked to libraries and authors.
- **Author**:
  - Fields: `name`, `biography`, etc.

### **Relationship Models**
- **Library**:
  - Fields: `name`, `location`, etc.
- **UserProfile**:
  - Extends default Django `User` model.
  - Additional fields: `role`, `library`, etc.

---

## **App Details**

### **Bookshelf**
- **Files**:
  - `models.py`: Book-related models.
  - `views.py`: Handles CRUD operations.
  - `forms.py`: Forms for creating and editing books.
  - `urls.py`: Routing for bookshelf operations.
- **Templates**:
  - `book_list.html`: Lists all books.
  - `create_book.html`: Form for adding books.
  - `edit_book.html`: Update book details.
  - `delete_book.html`: Delete confirmation.

### **Relationship App**
- **Files**:
  - `models.py`: Relationships between libraries, users, and books.
  - `views.py`: Handles role-based views and user interactions.
  - `forms.py`: Forms for user and library data.
  - `signals.py`: Implements event-based logic (e.g., post-save triggers).
  - `query_samples.py`: Examples of database queries.
- **Templates**:
  - `profile.html`, `profile_edit.html`: User profile pages.
  - `list_books.html`: Books list specific to libraries or roles.
  - `library_detail.html`: Detailed library view.

---

## **Documentation of CRUD Operations**

### **Create**
- Description: Allows adding a new entity (e.g., book, library).
- Relevant Files:
  - `forms.py`: Defines form structure.
  - `views.py`: Logic for creating entities.
  - Templates: `create_book.html`, `add_book.html`.

### **Read**
- Description: Lists or fetches details of entities.
- Relevant Files:
  - `views.py`: Handles data retrieval.
  - Templates: `book_list.html`, `list_books.html`.

### **Update**
- Description: Edits existing entity details.
- Relevant Files:
  - `forms.py`: Edit form structure.
  - `views.py`: Logic for updating entities.
  - Templates: `edit_book.html`, `profile_edit.html`.

### **Delete**
- Description: Removes entities from the system.
- Relevant Files:
  - `views.py`: Handles deletion logic.
  - Templates: `delete_book.html`.

---

## **Deployment**
For production deployment:
1. Set up a PostgreSQL database (or other production-grade DB).
2. Update `settings.py` with production configurations (e.g., `ALLOWED_HOSTS`, `DEBUG=False`).
3. Use a WSGI server (e.g., Gunicorn) and set up a web server (e.g., Nginx).
4. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

---

## **Future Enhancements**
1. Integration with external APIs for book metadata (e.g., Google Books API).
2. Advanced search and filtering options.
3. Notifications for due dates and new books.
4. Mobile-friendly design and responsiveness.

---

## **Acknowledgments**
- Django Documentation: [docs.djangoproject.com](https://docs.djangoproject.com)
- Community contributions and open-source libraries.

---
