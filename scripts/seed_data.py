from app.db.seed import AUTHORS, QUOTES

for author in AUTHORS:
    print(f"{author.id:>2}  {author.name}")
    for quote in (q for q in QUOTES if q.author_id == author.id):
        print(f"      #{quote.id} {quote.text}")
