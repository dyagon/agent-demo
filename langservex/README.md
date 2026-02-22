# LangServe + DeepSeek-R1 思维链 Demo

使用 **deepseek-reasoner**（DeepSeek-R1）的 LangServe 示例：LCEL 链暴露为 REST API，可选 Chainlit 对话界面。

## 环境

- 环境变量 **DEEPSEEK_API_KEY**（[DeepSeek API Key](https://platform.deepseek.com/api_keys)）由 uv 或运行环境注入。

## 1. 启动 LangServe API

在**项目根目录**执行：

```bash
uv run uvicorn langservex.server:app --reload --port 8080
```

- 文档与探索：<http://localhost:8080/docs>
- 链路径：`/reasoner`（支持 `invoke`、`stream`、`batch`）
- 请求体示例：`{"input": "用三步解释什么是 LangChain"}`

## 2. 启动 Chainlit 对话（可选）

在**项目根目录**另开终端：

```bash
uv run chainlit run langservex/chainlit_app.py -w --port 8050
```

浏览器打开 <http://localhost:8050>，对话会直接调用本地思维链（不依赖已启动的 8080 服务）。

## 结构说明

| 文件 | 说明 |
|------|------|
| `thinking_chain.py` | LCEL 链：`ChatDeepSeek(model="deepseek-reasoner")` + Prompt → StrOutputParser |
| `server.py` | FastAPI + `add_routes(app, chain, path="/reasoner")` |
| `chainlit_app.py` | Chainlit 前端，对用户输入调用链并流式输出 |
