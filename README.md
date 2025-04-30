```markdown
# 🚀 MongoDB Atlas to AstraDB VectorDB Migration Tool

A seamless CLI-based migration tool to bridge your MongoDB Atlas data with AstraDB Vector Store — built for modern AI-native and LLM-powered applications.

---

## 🔧 Key Features

- Connects to MongoDB Atlas using `pymongo`
- Embeds selected fields using HuggingFace’s `sentence-transformers` (`all-MiniLM-L6-v2`)
- Stores vectorized documents in AstraDB VectorDB using `LangChain` integration
- CLI support for:
  - Embedding fields
  - Metadata fields
  - Collection names
  - Astra token & API endpoint
- Automatically flattens `ObjectId` and extended JSON
- Ideal for building semantic search, RAG, and recommendation engines

---

## 📦 Installation

```bash
pip install pymongo langchain langchain-astra langchain-huggingface sentence-transformers
```

---

## 🚀 Usage

```bash
python migrate.py \
  --mongo_uri "<MONGO_ATLAS_URI>" \
  --db "<DATABASE_NAME>" \
  --collection "<MONGO_COLLECTION>" \
  --astra_collection "<ASTRA_COLLECTION>" \
  --embed "title" "content" \
  --meta "author" "tags" \
  --token "<ASTRA_DB_TOKEN>" \
  --astradb_endpoint "<ASTRA_DB_ENDPOINT>"
```

---

## 🧠 Example Use Case

If you have a MongoDB collection of blog posts:

```bash
--embed "title" "body"
--meta "author" "category"
```

This transforms your posts into vectors for similarity search or LLM retrieval.

---

## 🛠 How It Works

1. Connects to your MongoDB Atlas collection
2. Fetches documents and selects `embedding` + `metadata` fields
3. Converts ObjectId to string format
4. Embeds text using HuggingFace model
5. Pushes as `Document` objects into AstraDB Vector Store via LangChain

---

## 📁 Project Structure

```
migrate.py      # Main script
README.md       # Documentation
```

---

## ✨ Why Use This?

Most NoSQL databases aren’t vector-native. This script:

- Makes your unstructured MongoDB data LLM-ready
- Enables vector-based search and reasoning
- Saves hours of manual ETL work
- Supports scalable RAG pipelines

---

## 🙋‍♂️ Author Note

I built this tool to simplify my own vector migration pipeline. If you’re working in GenAI, ML, or search — feel free to use, fork, or improve!

> Contributions & feedback welcome!
