"""
ReAct Agent Demo：LangGraph StateGraph 方式（agent ↔ tools 条件边）。
支持单次命令行提问或交互式多轮，环境变量 DASHSCOPE_API_KEY。
"""
import os
import sys
from langchain_core.messages import HumanMessage

from graph import build_agent_graph


def main():
    if not os.environ.get("DASHSCOPE_API_KEY"):
        print("请设置环境变量 DASHSCOPE_API_KEY（通义千问 API Key）")
        sys.exit(1)

    graph = build_agent_graph()

    # 单次提问
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
        result = graph.invoke({"messages": [HumanMessage(content=question)]})
        last = result["messages"][-1]
        print(last.content if hasattr(last, "content") else str(last))
        return

    # 交互式
    print("LangGraph ReAct Agent（计算器 / 当前时间）")
    print("输入问题后回车，空行退出。")
    messages = []
    while True:
        try:
            line = input("\n你: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not line:
            break
        messages.append(HumanMessage(content=line))
        result = graph.invoke({"messages": messages})
        messages = result["messages"]
        last = messages[-1]
        text = last.content if hasattr(last, "content") else str(last)
        print("Agent:", text)


if __name__ == "__main__":
    main()
