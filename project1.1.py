import os
from llama_index.llms.dashscope import DashScope, DashScopeGenerationModels
from llama_index.core.base.llms.types import MessageRole, ChatMessage

# 设置 API 密钥
os.environ["DASHSCOPE_API_KEY"] = "sk-c977de3aa4db4b5a8733b3e377fa9355"  # 请替换为您的实际 API 密钥

# 初始化 DashScope 模型
dashscope_llm = DashScope(
    model_name=DashScopeGenerationModels.QWEN_MAX,
    api_key=os.environ["DASHSCOPE_API_KEY"]
)

# 定义初始对话内容
messages = [
    ChatMessage(role=MessageRole.SYSTEM, content="You are a helpful assistant.")
]

def get_response_stream(user_input):
    # 将用户输入添加到消息列表
    messages.append(ChatMessage(role=MessageRole.USER, content=user_input))

    # 使用 stream_chat 进行流式输出
    responses = dashscope_llm.stream_chat(messages)
    response_text = ""

    # 实时输出响应内容
    for response in responses:
        print(response.delta, end="", flush=True)
        response_text += response.delta  # 累积完整回复

    # 将 AI 回复添加到消息列表中
    messages.append(ChatMessage(role=MessageRole.ASSISTANT, content=response_text))

    return response_text

def check_end_of_conversation(input_text):
    # 检测用户输入是否包含结束对话的关键词
    end_phrases = ["谢谢", "再见", "感谢"]
    return any(phrase in input_text for phrase in end_phrases)

# 开始多轮对话循环
while True:
    user_input = input("用户: ")
    if check_end_of_conversation(user_input):
        print("AI: 感谢您的咨询，再见")
        break
    print("AI:", end=" ", flush=True)
    get_response_stream(user_input)  # 调用流式输出的响应函数
    print()  # 输出换行以保持对话格式整洁

