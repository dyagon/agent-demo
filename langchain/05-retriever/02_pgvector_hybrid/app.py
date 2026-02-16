"""
自定义 BaseRetriever：查询 03-vector 的 rag_hybrid 表，返回 LangChain Document 列表。

依赖：先执行 langchain/03-vector/init_db.py 与 build_db.py <文档目录>。

用法：uv run python langchain/05-retriever/01_custom_rag_hybrid/app.py "你的问题"
"""
import sys
from pathlib import Path

_root = Path(__file__).resolve().parent.parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))
from config import PG_CONNECTION_PSYCOPG, TABLE_NAME, RETRIEVE_K
from hybrid_retriever import HybridRetriever
from langchain_community.embeddings import DashScopeEmbeddings


def main():
    query = sys.argv[1] if len(sys.argv) > 1 else "项目有哪些 demo"
    embeddings = DashScopeEmbeddings(model="text-embedding-v3")
    retriever = HybridRetriever(
        connection_str=PG_CONNECTION_PSYCOPG,
        table_name=TABLE_NAME,
        k=RETRIEVE_K,
        embeddings=embeddings,
    )
    docs = retriever.invoke(query)
    print(f"--- 自定义 Retriever（rag_hybrid 向量检索） query: {query} ---\n")
    for i, d in enumerate(docs, 1):
        print(f"[{i}] {d.page_content[:200].replace(chr(10), ' ')}...")
        print()


if __name__ == "__main__":
    main()
