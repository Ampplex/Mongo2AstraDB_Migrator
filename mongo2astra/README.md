Sure! Here's the complete `README.md` content in plain text so you can copy and paste it directly:

---

```markdown
# 🛠️ Mongo2Astra

**Mongo2Astra** is a Python CLI tool that migrates documents from a MongoDB collection (such as MongoDB Atlas) to an [AstraDB Vector Store](https://www.datastax.com/astra) using powerful HuggingFace embeddings and LangChain's vector store integration.

> Ideal for building search, retrieval-augmented generation (RAG), and AI-powered applications on AstraDB with existing MongoDB data.

---

## 🚀 Features

- 📦 Migrate any MongoDB collection to AstraDB vector DB
- 🔍 Choose specific fields to embed using HuggingFace
- 🧠 Store associated metadata alongside vectorized content
- 🔗 Automatically converts MongoDB ObjectIDs to plain strings
- 🖥️ Command-line interface (CLI) for quick usage

---

## 📦 Installation

Install directly from source (with pip):

```bash
pip install .
```

Or use as a script after cloning:

```bash
git clone https://github.com/your-username/mongo2astra.git
cd mongo2astra
pip install -r requirements.txt
```

---

## 🧪 Requirements

- Python 3.8+
- `pymongo`
- `langchain-core`
- `langchain-huggingface`
- `langchain-astradb`
- `python-dotenv` (if using `.env` files for secrets)

---

## ⚙️ Usage

### CLI

```bash
python -m mongo2astra.migrator \
  --mongo_uri "your-mongodb-uri" \
  --db "your-db-name" \
  --collection "your-collection-name" \
  --astra_collection "your-astra-vector-collection" \
  --embed "field1" "field2" \
  --meta "field3" "field4" \
  --token "your-astra-token" \
  --astradb_endpoint "https://your-db-id-us-east1.apps.astra.datastax.com"
```

### Arguments

| Argument             | Type     | Description                                      |
|----------------------|----------|--------------------------------------------------|
| `--mongo_uri`        | `str`    | MongoDB connection URI                           |
| `--db`               | `str`    | MongoDB database name                            |
| `--collection`       | `str`    | MongoDB collection name                          |
| `--astra_collection` | `str`    | AstraDB vector collection name                   |
| `--embed`            | `list`   | Fields to use for creating text embeddings       |
| `--meta`             | `list`   | Fields to include as metadata in the vector store|
| `--token`            | `str`    | AstraDB token                                    |
| `--astradb_endpoint` | `str`    | AstraDB API endpoint                             |

---

## 🧠 Example

```bash
python -m mongo2astra.migrator \
  --mongo_uri "mongodb+srv://user:pass@cluster.mongodb.net" \
  --db "blog" \
  --collection "posts" \
  --astra_collection "blog_vectors" \
  --embed "title" "content" \
  --meta "author" "tags" \
  --token "<your-astra-token>" \
  --astradb_endpoint "https://vector-db-id-us-east1.apps.astra.datastax.com"
```

---

## 🛡️ Security Note

Avoid hardcoding sensitive credentials like your AstraDB token or MongoDB URI. Instead, use environment variables or a `.env` file and load them with [`python-dotenv`](https://github.com/theskumar/python-dotenv).

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Developed with ❤️ by **Ankesh Kumar**  
📧 [ankesh3905222@gmail.com](mailto:ankesh3905222@gmail.com)

---

## 🌟 Star this repo if it helped you!
```

---

Let me know if you'd like help generating the `LICENSE` file or setting up `setup.cfg`/`.gitignore`.