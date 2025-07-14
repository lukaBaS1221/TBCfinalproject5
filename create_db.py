from ext import app, db
from models import Book

Books = [
    {
        "name": "the count of monte cristo",
        "price": 27.99,
        "author": "alexandre Dumas",
        "image": "count of monte cristo.jpg",
        "description": "A betrayed man escapes prison and sets out to get revenge on those who wronged him."
    },

{
    "name": "East of eden",
    "price": 24.99,
    "author": "John Steinbeck",
    "image": "eastofeden.jpg",
    "description": "Two families struggle with love, jealousy, and destiny across generations in California's Salinas Valley."
},
{
    "name": "Demons",
    "price": 26.49,
    "author": "Fyodor Dostoevsky",
    "image": "demons.jpg",
    "description": "A political group spirals into chaos as radical ideas collide with personal ambition and moral collapse."
},
{
    "name": "1984",
    "price": 19.99,
    "author": "George Orwell",
    "image": "1984.jpg",
    "description": "A totalitarian government controls every aspect of life, rewriting truth and erasing freedom."
},
{
    "name": "The iliad",
    "price": 16.99,
    "author": "Homer",
    "image": "iliad.jpg",
    "description": "Greek heroes clash during the Trojan War, where honor, wrath, and fate shape every battle."
},
{
    "name": "The master and margarita",
    "price": 20.99,
    "author": "Mikhail Bulgakov",
    "image": "master and margarita.jpg",
    "description": "the devil visits Soviet Moscow, unleashing chaos while a writer questions truth and freedom."
},
{
    "name": "The Great gatsby",
    "price": 18.99,
    "author": "F. Scott Fitzgerald",
    "image": "great gatsby.jpg",
    "description": "A mysterious millionaire throws lavish parties in pursuit of a lost love during the Jazz Age."
},
{
    "name": "The picture of dorian gray",
    "price": 17.49,
    "author": "Oscar Wilde",
    "image": "doriangray.jpg",
    "description": "A young man stays forever young while his portrait absorbs the marks of his sins."
},
{
    "name": "Emma",
    "price": 16.00,
    "author": "Jane austen",
    "image": "emma.jpg",
    "description": "A clever young woman plays matchmaker, unaware of the romantic missteps she’s causing."
},
{
    "name": "Moby-dick",
    "price": 23.49,
    "author": "Herman Melville",
    "image": "moby-dick.jpg",
    "description": "A sea captain’s obsession with a white whale leads his crew on a doomed journey."
},
{
    "name": "451 Fahrenheit",
    "price": 14.50,
    "author": "Ray Bradbury",
    "image": "451.jpg",
    "description": "In a future where books are illegal, a fireman begins to question the system he enforces."
},
{
    "name": "Homo faber",
    "price": 17.99,
    "author": "Max Frisch",
    "image": "homo faber.jpg",
    "description": "An engineer’s rigid worldview unravels after a chance encounter with someone from his past."
},
{
    "name": "A clockwork orange",
    "price": 23.00,
    "author": "Anthony Burgess",
    "image": "clockwork orange.jpg",
    "description": "A teenage delinquent faces state control and moral reprogramming in a violent dystopian future."
},
{
    "name": "The stranger",
    "price": 15.00,
    "author": "Albert Camus",
    "image": "stranger.jpg",
    "description": "A detached man commits murder and faces trial in a world that feels meaningless to him."
},
{
    "name": "Stoner",
    "price": 18.99,
    "author": "John Williams",
    "image": "stoner.jpg",
    "description": "A quiet literature professor lives an unremarkable life filled with quiet struggles and inner strength."
}
]

with app.app_context():
    db.drop_all()
    db.create_all()

    for book_data in Books:
        book = Book(
            name=book_data["name"],
            price=book_data["price"],
            author=book_data["author"],
            img=book_data["image"],
            description=book_data["description"]
        )
        db.session.add(book)

    db.session.commit()
