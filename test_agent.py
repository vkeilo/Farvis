from agent_use import GptAgent
from mlocate import Mlocate
from file_keywards_get import get_file_keywards
# target_tester = "file_keywards_generator.json"
# test_agent = GptAgent("chatglm_lite")
# test_agent.init_messages_by_json(target_tester)






# test_prompt = "查看当前显示器名字"
# test_agent.prompt_add(test_prompt)
# output = test_agent.prompt_post(remember_flag=False,T=0.01)
# print(output)

get_file_keywards("查看主机hostname")
# print(file_keywards_generator.messages)




# locate_test = Mlocate()
# output = locate_test.get_related_files_by_keywords(["passwd","config.json"])
# output = locate_test.get_mlocate_output("locate  passwd")
# print(output)