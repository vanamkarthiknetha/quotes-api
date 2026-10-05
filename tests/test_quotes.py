def test_featured_quote(get):
    assert get("/quote").json()["id"] == 1


def test_filter_by_tag(get):
    quotes = get("/quotes?tag=testing").json()
    assert quotes and all("testing" in q["tags"] for q in quotes)


def test_get_quote_404(get):
    assert get("/quotes/999").status_code == 404


def test_search(get):
    results = get("/quotes/search?q=bugs").json()
    assert results and all("bugs" in r["text"].lower() for r in results)


def test_search_requires_query(get):
    assert get("/quotes/search?q=a").status_code == 422


def test_random_quote(get):
    assert "text" in get("/quotes/random").json()
