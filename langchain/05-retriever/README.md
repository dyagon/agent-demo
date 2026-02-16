# 05-retriever：LangChain Retriever + PGVector 示例

基于 **PGVector** 的若干 **LangChain Retriever** 用法示例，数据与表结构参考 [03-vector](../03-vector/)。

## 数据准备

- **示例 01、03**：使用与 [03-vector](../03-vector/) 相同的表 `rag_hybrid`。请先执行：
  ```bash
  uv run python langchain/03-vector/init_db.py
  uv run python langchain/03-vector/build_db.py <文档目录>
  ```
  例如：`uv run python langchain/03-vector/build_db.py langgraph/02-qa/docs`

- **示例 02**：使用 `langchain_postgres.PGVector` 自带集合，需单独灌数：
  ```bash
  uv run python langchain/05-retriever/build_db.py <文档目录>
  ```

## 示例一览

| 示例 | 说明 |
|------|------|
| [01_custom_rag_hybrid](01_custom_rag_hybrid/) | 自定义 `BaseRetriever`，直接查 03-vector 的 `rag_hybrid` 表，返回 `Document` 列表 |
| [02_pgvector_native](02_pgvector_native/) | 使用 `langchain_postgres.PGVector.as_retriever()`：相似检索、MMR 检索 |
| [03_rag_chain](03_rag_chain/) | 用 Retriever 组 RAG 链：retriever → 格式化文档 → LLM 生成回答 |

## 运行

```bash
# 01：自定义 Retriever（依赖 03-vector 的 rag_hybrid 已建表并灌数）
uv run python langchain/05-retriever/01_custom_rag_hybrid/app.py "你的问题"

# 02：PGVector 原生 as_retriever（需先执行本目录 build_db.py）
uv run python langchain/05-retriever/02_pgvector_native/app.py "你的问题"

# 03：RAG 链（默认用 01 的 retriever，即 rag_hybrid）
uv run python langchain/05-retriever/03_rag_chain/app.py "你的问题"
```

## 环境

- `DASHSCOPE_API_KEY`：embedding 与 LLM（03 需要）
- `PG_CONNECTION`：与 03-vector / dev docker-compose 一致，02 需为 `postgresql+psycopg://...` 格式
