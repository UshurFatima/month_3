class Queries:
    CREATE_SURVEY_RESULTS_TABLE = '''
        CREATE TABLE IF NOT EXISTS book_survey (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT, 
            age INTEGER,
            gender TEXT,
            genre TEXT
        )
    '''

    DROP_GENRES_TABLE = '''
    DROP TABLE IF EXISTS genres
    '''

    CREATE_GENRES_TABLE = '''
    CREATE TABLE IF NOT EXISTS genres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
    )
    '''

    POPULATE_GENRES = '''
    INSERT INTO genres(name) VALUES 
    ('Детектив'),
    ('Фантастика'),
    ('Роман'),
    ('Хоррор')
    '''

    DROP_BOOKS_TABLE = '''
    DROP TABLE IF EXISTS books
    '''

    CREATE_BOOKS_TABLE = '''
    CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    author TEXT,
    price INTEGER,
    cover TEXT,
    genre_id INTEGER,
    FOREIGN KEY (genre_id) REFERENCES genre(id)
    )
    
    '''

    POPULATE_BOOKS = '''
    INSERT INTO books (name, author, price, cover, genre_id) VALUES 
    ('Оно', 'Стивен Кинг', 250, 'images/book1.jpg', 4),
    ('Записки о Шерлоке Холмсе', 'Артур Конан Дойл', 275, 'images/book2.jpg', 1),
    ('Великий Гэтсби', 'Фрэнсис Фицджеральд', 300, 'images/book3.jpg', 3),
    ('Джейн Эйр', 'Шарлотта Бронте', 340, 'images/book4.jpg', 3),
    ('Токийские легенды', 'Харуки Мураками', 400, 'images/book5.jpg', 2)
    '''