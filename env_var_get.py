from agent_use import GptAgent
from config_parser import llm_name,local_roles
import text_regular_check
from syslogger import logger
import os

# 获取所有环境变量的字典
env_vars = os.environ


env_var_selector = GptAgent(llm_name)


def get_related_env_vars(task_text) -> str:
    """
    获取用户指令相关的关键文件
    :task_text: 用户的输入的任务
    :return: 返回与任务相关的环境变量字典
    """
    env_var_selector.history_add_one('user',f'{env_vars}')
    env_var_selector.history_add_one('assistant',f'This is env var of a Ubuntu system, what information you want to know')
    # env_var_selector.history_add_one('user',f'我现在需要编写能够完成文件创建任务\n{task_text}\n的touch指令，在这些环境变量中，有哪几个关键信息，用少于300字符的文本回答')
    # prompt = f"当前正在处理的任务是：\n`{task_text}`\n\n当前已知的ubuntu环境变量有：\n`{env_vars}`\n\n 请你从中筛选出几个与任务最相关的完整信息，不多于300字符，不要废话`\n"
    # prompt = f'我现在需要编写能够完成文件创建任务\n{task_text}\n的touch指令，在这些环境变量中，有哪几个关键信息'
    prompt = f'Here is a task\n{task_text}\nWhich information above can help me write the correct `touch` command '
    env_var_selector.prompt_add(prompt)
    output = env_var_selector.prompt_post(remember_flag=False,T=0.01)
    logger.info(f"Determine the relevant information from environment vars: {output}")
    return output




# 打印所有环境变量
# for key, value in env_vars.items():
#     print(f"{key}: {value}")