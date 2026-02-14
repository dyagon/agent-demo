# agent-demo

用于学习 Agent / LLM 应用的示例项目。**每个子目录一个独立 demo，用单独命令即可运行。**

## 环境准备

- Python 3.14+（推荐用 [uv](https://github.com/astral-sh/uv) 管理）
- 在项目根目录创建 `.env`，按各 demo 需要配置 API Key（如 `DASHSCOPE_API_KEY`）

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
├── .env                # 环境变量（不提交）
└── langchain/          # 按框架/主题分子目录
    ├── 01-simple/      # LangChain + 通义千问 简单链
    │   ├── README.md
    │   └── main.py
    └── 02-article-gen/ # Streamlit + LangChain 文章生成（topic→标题→正文）
        ├── README.md
        └── app.py
```

## 运行各 Demo

在**项目根目录**执行（保证能读到根目录的 `.env`）：

| Demo | 说明 | 命令 |
|------|------|------|
| langchain/01-simple | LangChain + Qwen 简单链 | `uv run python langchain/01-simple/main.py` |
| langchain/02-article-gen | Streamlit 文章生成（topic→标题→正文） | `uv run streamlit run langchain/02-article-gen/app.py` |

新增 demo 时，在对应主题目录下新建子目录（如 `langchain/02-xxx`），放入 `main.py` 和可选 `README.md`，并在上表中补充一行运行命令即可。
