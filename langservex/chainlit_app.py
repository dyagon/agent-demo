"""
Chainlit 前端：调用 langservex 思维链（deepseek-reasoner），流式输出。
运行: 先启动 LangServe（见 README），再运行
  uv run chainlit run langservex/chainlit_app.py -w --port 8050
或直接本地链（不依赖已启动的 API）：
  uv run chainlit run langservex/chainlit_app.py -w --port 8050
环境变量: DEEPSEEK_API_KEY
"""
import chainlit as cl

from thinking_chain import chain


@cl.on_message
async def on_message(msg: cl.Message):
    out = cl.Message(content="")
    async for chunk in chain.astream({"input": msg.content}):
        out.content += chunk
        await out.update()
    await out.send()
