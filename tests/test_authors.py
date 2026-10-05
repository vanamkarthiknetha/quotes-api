def test_list_authors(get):
    assert len(get("/authors").json()) >= 3


def test_author_quotes(get):
    assert all(q["author_id"] == 1 for q in get("/authors/1/quotes").json())


def test_unknown_author(get):
    assert get("/authors/999/quotes").status_code == 404
