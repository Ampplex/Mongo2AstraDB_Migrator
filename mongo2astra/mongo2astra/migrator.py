from pymongo import MongoClient
from langchain_astradb import AstraDBVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
import argparse

def flatten_oid(val):
    """Convert ObjectId or Mongo extended JSON to plain string."""
    if isinstance(val, dict) and "$oid" in val:
        return val["$oid"]
    return str(val)

def migrate(
    mongo_uri,
    db_name,
    collection_name,
    astra_collection_name,
    embedding_fields,
    metadata_fields,
    astra_token,
    astradb_endpoint,
):
    # Connect MongoDB
    mongo_client = MongoClient(mongo_uri)
    mongo_db = mongo_client.get_database(db_name)
    mongo_collection = mongo_db.get_collection(collection_name)

    print(f"✅ Connected to MongoDB collection '{collection_name}")

    # Setup Astra Vector Store
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vstore = AstraDBVectorStore(
        collection_name=astra_collection_name,
        embedding=embedding,
        token=astra_token,
        api_endpoint=astradb_endpoint,
    )

    print(f"✅ Connected to Astra Vector Store '{astra_collection_name}")

    # Fetch Mongo documents
    docs = []
    for item in mongo_collection.find():
        # Embedding text
        text = " ".join(str(item.get(f, "")) for f in embedding_fields)
        # Metadata
        metadata = {}
        for key in metadata_fields:
            val = item.get(key)
            if isinstance(val, list):
                metadata[key] = [flatten_oid(v) for v in val]
            elif isinstance(val, dict) and "$oid" in val:
                metadata[key] = flatten_oid(val)
            else:
                metadata[key] = val

        metadata["mongo_id"] = flatten_oid(item["_id"])
        docs.append(Document(page_content=text, metadata=metadata))

    # Insert into Astra
    inserted = vstore.add_documents(docs)
    print(f"✅ Migrated {len(inserted)} documents to collection '{astra_collection_name}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MongoDB Atlas to AstraDB VectorDB Migration Tool")
    parser.add_argument("--mongo_uri", type=str, required=True, help="MongoDB Atlas URI")
    parser.add_argument("--db", type=str, required=True, help="MongoDB database name")
    parser.add_argument("--collection", type=str, required=True, help="MongoDB collection name")
    parser.add_argument("--astra_collection", type=str, required=True, help="Astra VectorDB collection name")
    parser.add_argument("--embed", nargs="+", required=True, help="Fields to embed (text fields)")
    parser.add_argument("--meta", nargs="+", required=True, help="Fields to store in metadata")
    parser.add_argument("--token", type=str, help="AstraDB token")
    parser.add_argument("--astradb_endpoint", type=str, help="AstraDB API endpoint")

    args = parser.parse_args()

    migrate(
        mongo_uri=args.mongo_uri,
        db_name=args.db,
        collection_name=args.collection,
        astra_collection_name=args.astra_collection,
        embedding_fields=args.embed,
        metadata_fields=args.meta,
        astra_token=args.token,
        astradb_endpoint=args.astradb_endpoint
    )