import csv
import sys

from app.db.seed import QUOTES

writer = csv.writer(sys.stdout)
writer.writerow(["id", "author_id", "text", "tags"])
for q in QUOTES:
    writer.writerow([q.id, q.author_id, q.text, ";".join(q.tags)])
