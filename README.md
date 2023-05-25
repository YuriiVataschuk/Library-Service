# Library site

API service for the library site

## Installing using GitHub

```shell
git clone git@github.com:YuriiVataschuk/Library-Service.git
cd Library-Service
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
set SECRET_KEY=<your secret key>
python manage.py migrate
python manage.py runserver
```
  
## Getting access

```shell
create user via /api/users/
get access token via /api/users/token/
```

## Features

1. JWT authenticated
2. Admin panel /admin/
3. Documentation is located at /api/doc/swagger/
4. Book Catalog: The system maintains a complete catalog of all the books available in the library. It includes information such as book titles, authors, and daily fees.
5. Book Search: Users can easily search for books using different criteria, such as title, author, or daily fee.
6. Book Borrowing: Users can request to borrow books through the online system. They can browse the catalog and select the desired book(s) they wish to borrow. During the borrowing process, users can specify the borrowing period.
7. Availability Check: The system checks the availability of the selected book(s) before processing the borrowing request. It ensures that the requested books are currently available for borrowing.
8. Borrowing Management: The system manages the entire borrowing process. It keeps track of borrowed books, borrowing dates, and return dates.
