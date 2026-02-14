# agent-demo

用于学习 Agent / LLM 应用的示例项目。**每个子目录一个独立 demo，用单独命令即可运行。**

## 环境准备

- Python 3.12+（推荐用 [uv](https://github.com/astral-sh/uv) 管理）
- 环境变量（如 `DASHSCOPE_API_KEY`）由 uv 或运行环境注入，无需 .env

```bash
# 安装依赖（在项目根目录）
uv sync
```

## 项目结构

```
agent-demo/
├── README.md           # 本说明
├── main.py             # 列出所有 demo 及运行命令
├── pyproject.toml      # 项目与依赖
├── langchain/          # LangChain 示例
│   ├── 01-simple/
│   │   ├── README.md
│   │   └── main.py
│   └── 02-article-gen/
│       ├── README.md
│       └── app.py
└── langgraph/          # LangGraph 示例
    ├── 01-simple/      # StateGraph 多节点流程（问题→回答→总结）
    │   ├── README.md
    │   └── main.py
    └── 02-qa/          # 文档 QA：PGVector + 对话式问答
        ├── README.md
        ├── config.py
        ├── build_db.py
        ├── test_retrieval.py
        ├── graph.py
        ├── app.py
        └── docs/       # 默认 Markdown 文档目录
```

## 运行各 Demo

在**项目根目录**执行（保证能读到根目录的 `.env`）：

| Demo | 说明 | 命令 |
|------|------|------|
| langchain/01-simple | LangChain + Qwen 简单链 | `uv run python langchain/01-simple/main.py` |
| langchain/02-article-gen | Streamlit 文章生成（topic→标题→正文） | `uv run streamlit run langchain/02-article-gen/app.py` |
| langgraph/01-simple | LangGraph StateGraph 多节点（问题→回答→总结） | `uv run python langgraph/01-simple/main.py` |
| langgraph/02-qa | 文档 QA：先 `build_db.py <文档目录>` 建库，再 `test_retrieval.py` 测试，`streamlit run app.py` 对话 | 见 `langgraph/02-qa/README.md` |

新增 demo 时，在对应主题目录下新建子目录，放入 `main.py` 或 `app.py` 及可选 `README.md`，并在上表中补充一行运行命令即可。
