from agent_use import GptAgent

target_tester = "path_locate.json"
test_agent = GptAgent("chatglm2-6b")
test_agent.init_messages_by_json(target_tester)






test_prompt = "查看当前显示器名字"
test_agent.prompt_add(test_prompt)
output = test_agent.prompt_post(remember_flag=False,T=0.001)
print(output)