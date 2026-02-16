"""
自定义 BaseRetriever：查询 03-vector 的 rag_hybrid 表。
供 01_custom_rag_hybrid 与 03_rag_chain 共用。
"""
import psycopg
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
from langchain_community.embeddings import DashScopeEmbeddings


class HybridRetriever(BaseRetriever):
    """基于 03-vector 的 rag_hybrid 表的向量检索 Retriever。"""

    connection_str: str
    table_name: str
    k: int = 5
    embeddings: DashScopeEmbeddings = None

    def _get_relevant_documents(self, query: str) -> list[Document]:
        vec = self.embeddings.embed_query(query)
        vec_str = "[" + ",".join(str(x) for x in vec) + "]"
        docs = []
        with psycopg.connect(self.connection_str) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    f"""
                    SELECT id::text, content, metadata
                    FROM {self.table_name}
                    ORDER BY embedding <=> %s::vector
                    LIMIT %s
                    """,
                    (vec_str, self.k),
                )
                for row in cur.fetchall():
                    doc_id, content, metadata = row[0], row[1], row[2] or {}
                    if not isinstance(metadata, dict):
                        metadata = {}
                    metadata["id"] = doc_id
                    docs.append(Document(page_content=content, metadata=metadata))
        return docs
