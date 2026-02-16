# 05-retriever：LangChain Retriever + PGVector 示例

基于 **PGVector** 的若干 **LangChain Retriever** 用法示例，数据与表结构参考 [04-vector](../04-vector/)（或 03-embedding）。

## 数据准备

- **01、02、03**：使用与 04-vector 相同的表 `rag_hybrid`。请先执行：
  ```bash
  uv run python langchain/04-vector/init_db.py
  uv run python langchain/04-vector/build_db.py <文档目录>
  ```

- **01_pgvector_native**：使用 `langchain_postgres.PGVector` 自带集合时，需执行其目录下 `build_db.py`。

## 示例一览

| 示例 | 说明 |
|------|------|
| [01_pgvector_native](01_pgvector_native/) | `langchain_postgres.PGVector.as_retriever()`：相似检索、MMR |
| [02_pgvector_hybrid](02_pgvector_hybrid/) | **EnsembleRetriever**：向量 + 全文（tsvector）两路，RRF 融合 |
| [03_bm25_ensemble](03_bm25_ensemble/) | **EnsembleRetriever**：向量 + **BM25** 两路，RRF 融合 |

## 运行

```bash
# 01：PGVector 原生
uv run python langchain/05-retriever/01_pgvector_native/app.py "你的问题"

# 02：向量 + 全文 RRF
uv run python langchain/05-retriever/02_pgvector_hybrid/app.py "你的问题"
uv run python langchain/05-retriever/02_pgvector_hybrid/app.py "你的问题" --weights 0.7 0.3

# 03：向量 + BM25 RRF（需安装 rank_bm25）
uv run python langchain/05-retriever/03_bm25_ensemble/app.py "你的问题"
uv run python langchain/05-retriever/03_bm25_ensemble/app.py "你的问题" --weights 0.7 0.3
```

## 环境

- `DASHSCOPE_API_KEY`：embedding（01、02、03 需要）
- `PG_CONNECTION`：与 04-vector / dev docker-compose 一致
- 03_bm25_ensemble 需安装 `rank_bm25`（已加入项目依赖，`uv sync` 即可）
