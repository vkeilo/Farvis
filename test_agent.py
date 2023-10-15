from agent_use import GptAgent
from mlocate import Mlocate
from file_keywards_get import get_file_keywards
from env_var_get import get_related_env_vars
# target_tester = "roles_play/task_judge.json"
# test_agent = GptAgent("chatglm_pro")
# test_agent.init_messages_by_json(target_tester)
# test_prompt = "在miniconda3的默认环境存储文件夹中建立新文件夹tmpdir"
# test_agent.prompt_add(test_prompt)
# output = test_agent.prompt_post(remember_flag=False,T=0.01)
# print(output)

get_file_keywards("creat a file named tmp.txt in tool `clash` installation directory")

# get_related_env_vars("creat a file named tmp.txt in MINICONDA3 installation directory")

# print(file_keywards_generator.messages)




# locate_test = Mlocate()
# output = locate_test.get_related_files_by_keywords(["passwd","config.json"])
# output = locate_test.get_mlocate_output("locate  passwd")
# print(output)