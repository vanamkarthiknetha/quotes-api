def test_tags_have_counts(get):
    tags = {t["name"]: t["count"] for t in get("/tags").json()}
    assert tags["design"] == 2
