from agent_use import GptAgent
from config_parser import llm_name,local_roles
import text_regular_check
from syslogger import logger


file_keywards_generator = GptAgent(llm_name)
file_keywards_generator.init_messages_by_json(local_roles["file_keywards_generator"])




def get_file_keywards(task_text) -> list:
    """
    获取用户指令相关的关键文件
    :task_text: 用户的输入的任务
    :return: 返回与关键字相关的文件或目录名列表
    """
    prompt = f"{task_text}，指令相关文件有:"
    file_keywards_generator.prompt_add(prompt)
    output = file_keywards_generator.prompt_post(remember_flag=False,T=0.01)
    if not text_regular_check.is_str_list_text(output):
        logger.error(f"file_keywards_generator output is not str list: ---{output}---")
        output = []
        return
    logger.info(f"Determine the relevant file or path: {output}")
    output = eval(output)
    return output

