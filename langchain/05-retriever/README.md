# 04-retriever：LangChain Retriever + PGVector 示例

基于 **PGVector** 的若干 **LangChain Retriever** 用法示例，数据与表结构参考 [03-embedding](../03-embedding/)（或 03-vector）。

## 数据准备

- **01、02_pgvector_hybrid、02_pgvector_ensemble**：使用与 03-embedding 相同的表 `rag_hybrid`。请先执行：
  ```bash
  uv run python langchain/03-embedding/init_db.py
  uv run python langchain/03-embedding/build_db.py <文档目录>
  ```

- **01_pgvector_native**：使用 `langchain_postgres.PGVector` 自带集合，需执行其目录下 `build_db.py`。

## 示例一览

| 示例 | 说明 |
|------|------|
| [01_pgvector_native](01_pgvector_native/) | `langchain_postgres.PGVector.as_retriever()`：相似检索、MMR |
| [02_pgvector_hybrid](02_pgvector_hybrid/) | 自定义 Retriever 查 `rag_hybrid` 向量 |
| [02_pgvector_ensemble](02_pgvector_ensemble/) | **EnsembleRetriever**：向量 + 全文两路检索，RRF 融合 |

## 运行

```bash
# 01：PGVector 原生
uv run python langchain/04-retriever/01_pgvector_native/app.py "你的问题"

# 02 hybrid：向量检索
uv run python langchain/04-retriever/02_pgvector_hybrid/app.py "你的问题"

```

## 环境

- `DASHSCOPE_API_KEY`：embedding（01、02 需要）
- `PG_CONNECTION`：与 03-embedding / dev docker-compose 一致
