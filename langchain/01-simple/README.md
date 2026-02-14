# 01-simple

LangChain + 通义千问 (Qwen) 简单链式调用示例。

- 使用 LCEL 构建 `Prompt -> LLM -> OutputParser` 链
- 需在项目根目录 `.env` 中配置 `DASHSCOPE_API_KEY`

## 运行

在项目根目录执行：

```bash
uv run python langchain/01-simple/main.py
```
