from app.models import Author, Quote

AUTHORS = [
    Author(id=1, name="Edsger W. Dijkstra", born=1930),
    Author(id=2, name="Donald Knuth", born=1938),
    Author(id=3, name="Linus Torvalds", born=1969),
    Author(id=4, name="Grace Hopper", born=1906),
    Author(id=5, name="Alan Kay", born=1940),
]

QUOTES = [
    Quote(id=1, author_id=1, text="Simplicity is prerequisite for reliability.", tags=["design"]),
    Quote(id=2, author_id=2, text="Premature optimization is the root of all evil.", tags=["performance"]),
    Quote(id=3, author_id=3, text="Talk is cheap. Show me the code.", tags=["code"]),
    Quote(id=4, author_id=1, text="Testing shows the presence, not the absence of bugs.", tags=["testing"]),
    Quote(id=5, author_id=4, text="The most dangerous phrase is: we've always done it this way.", tags=["culture"]),
    Quote(id=6, author_id=5, text="The best way to predict the future is to invent it.", tags=["design", "culture"]),
    Quote(id=7, author_id=2, text="Beware of bugs in the above code; I have only proved it correct.", tags=["testing", "code"]),
]
