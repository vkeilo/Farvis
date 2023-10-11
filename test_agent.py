from agent_use import gpt_agent

target_tester = "path_analyser.json"
test_agent = gpt_agent("chatglm2-6b")
test_agent.init_messages_by_json(target_tester)






test_prompt = "在用户 Ana 的桌面建立新文件夹"
test_agent.prompt_add(test_prompt)
output = test_agent.prompt_post(remember_flag=False,T=0.001)
print(output)