"""
Agent Demo 配置：模型名等。
从环境变量读取，与项目其他 demo 一致。
"""
import os

# 通义千问模型名
MODEL_NAME = os.getenv("AGENT_MODEL_NAME", "qwen-max")
