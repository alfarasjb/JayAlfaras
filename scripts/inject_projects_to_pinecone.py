from src.services.vector import Database


if __name__ == "__main__":
    db = Database()
    # db.store_to_pinecone()
    print(db.store.similarity_search("Projects using Python"))