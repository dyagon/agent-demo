# 01-simple

LangGraph 简单示例：用 `StateGraph` 实现多节点流程。

- **流程**：问题 → 生成回答 → 润色总结 → 输出
- **状态**：`State` 在节点间传递（question / answer / summary）
- 需在项目根目录 `.env` 中配置 `DASHSCOPE_API_KEY`

## 运行

在项目根目录执行：

```bash
uv run python langgraph/01-simple/main.py
```
