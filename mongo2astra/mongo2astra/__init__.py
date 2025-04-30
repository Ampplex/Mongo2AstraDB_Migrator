from .migrator import migrate
import argparse

__version__ = "0.1.1"

def main():

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

if __name__ == "__main__":
    main()