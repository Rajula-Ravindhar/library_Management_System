import mysql.connector


def mydf():
    return mysql.connector.connect(    #database connecting.
        host='localhost',
        username='root',
        password='Root',
        database='library'
    )
db=mydf()
curs=db.cursor()          #cursor intializing...

#Tables creation.              #create tables books,members and borrow_record for storing info.
# curs.execute('''
# CREATE TABLE books(
#     book_id INT AUTO_INCREMENT PRIMARY KEY,
#     Title VARCHAR(100),
#     Author VARCHAR(100),
#     Status VARCHAR(50));
# '''
# )
# curs.execute('''
# CREATE TABLE members(
#     member_id INT AUTO_INCREMENT PRIMARY KEY,
#     Name VARCHAR(100),
#     Eemail VARCHAR(100)
# );
# ''')
# curs.execute('''
# CREATE TABLE borrow_record(
#     record_id INT AUTO_INCREMENT PRIMARY KEY,
#     book_id INT,
#     member_id INT,
#     borrow_date date,
#     return_date date);
# ''')

def add_book():          #we can add new books into library.
    Title=input("enter title :\n")
    Author=input("enter author:\n")
    Status=input("enter status:\n")
    curs.execute('INSERT INTO books(Title,Author,Status) VALUES(%s,%s,%s);',(Title,Author,Status))
    db.commit()
    print(f'Successfully Added {Title} Book')


def register_member():     #here members can register into library.
    Name=input("enter name\n")
    Eemail=input("enter email\n")
    curs.execute('INSERT INTO members(Name,Eemail) VALUES(%s,%s);',(Name,Eemail))
    db.commit()
    print(f'Successfully Registered {Name} Record')


def issue_book():
    curs.execute('SELECT book_id,Title FROM books WHERE Status is "avail";')
    book_id=int(input('enter book_id:\n'))
    member_id=int(input('enter member_id:\n'))
    borrow_date=input('enter borrow_date:\n')
    return_date=input('enter return_date:')
    curs.execute('INSERT INTO borrow_record(book_id,member_id,barrow_date,return_date) VALUES(%s,%s,%s,%s);',(book_id,member_id,borrow_date,return_date))
    print('book issues success\n')
    curs.execute('''
    UPDATE books 
    SET Status='not avail'
    WHERE book_id=%s;
    ''',(book_id,))
    db.commit()


def return_book():
    book_id=int(input('enter book_id you returning\n'))
    curs.execute('''
    UPDATE books
    SET Status='avail'
    WHERE book_id=%s;''',(book_id,))
    db.commit()
    print("book submmitted successfully\n")


def view_all_books():
    curs.execute("SELECT * FROM books;")
    for row in curs.fetchall():
        print(row)

def view_all_members():
    curs.execute("SELECT * FROM members;")
     for row in curs.fetchall():
        print(row)


def view_borrow_records():
    curs.execute('SELECT * FROM borrow_record;')
     for row in curs.fetchall():
        print(row)


if __name__=='__main__':
 while True:
    print(" 1.Add_book\n  2.Register_member\n   3.Issue_book\n   4.Return_book\n  5.View_all_books\n  6.View_all_members\n  7.View_all_borrow_records\n")
    choice=int(input('>\n'))
    if choice==1:
        add_book()
    elif choice==2:
        register_member()
    elif choice==3:
        issue_book()
    elif choice==4:
        return_book()
    elif choice==5:
        view_all_books()
    elif choice==6:
        view_all_members()
    else:
        view_borrow_records()
    trigger=input("do you want do any operations (yes/no)\n")
    if trigger!= 'yes':
        break
