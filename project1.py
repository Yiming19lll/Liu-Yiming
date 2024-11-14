import os
from llama_index.llms.dashscope import DashScope, DashScopeGenerationModels

# 设置 API 密钥
os.environ["DASHSCOPE_API_KEY"] = "sk-c977de3aa4db4b5a8733b3e377fa9355"  # 请将YOUR_DASHSCOPE_API_KEY替换为您的实际API密钥

# 初始化 DashScope 模型
dashscope_llm = DashScope(
    model_name=DashScopeGenerationModels.QWEN_MAX,
    api_key=os.environ["DASHSCOPE_API_KEY"]
)

# 用于存储多轮对话的历史记录
conversation_history = []

def get_response(input_text):
    # 将用户输入和历史对话组合成提示语
    prompt = "\n".join(conversation_history) + f"\n用户: {input_text}\nAI:"
    response = dashscope_llm.complete(prompt).text
    conversation_history.append(f"用户: {input_text}")
    conversation_history.append(f"AI: {response}")
    return response

def check_end_of_conversation(input_text):
    # 检测结束对话的关键词
    end_phrases = ["谢谢", "再见", "感谢"]
    return any(phrase in input_text for phrase in end_phrases)

# 开始对话循环
while True:
    user_input = input("用户: ")
    if check_end_of_conversation(user_input):
        print("AI: 感谢您的咨询，再见")
        break
    response = get_response(user_input)
    print("AI:", response)

