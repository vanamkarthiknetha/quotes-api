from app.utils.hashing import generate_api_key, hash_api_key

key = generate_api_key()
print(f"key:  {key}")
print(f"hash: {hash_api_key(key)}")
