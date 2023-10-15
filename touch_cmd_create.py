from agent_use import GptAgent
from mlocate import Mlocate
from file_keywards_get import get_file_keywards
from env_var_get import get_related_env_vars


task = "crate a file named `config.json` in the directory where my tool `windterm` is located"
# task = "crate a file named `config.json` in my CUDA installation directory"

touch_cmd_creator = GptAgent()
related_env_vars = get_related_env_vars(task)
related_fearch_keywards_list = get_file_keywards(task)
fsearcher = Mlocate()
related_path_list = fsearcher.get_related_files_by_keywords(related_fearch_keywards_list)


prompt = f"information about env vars:\n\n{related_env_vars}\n\nknown path or file of current ubuntu system:\n{related_fearch_keywards_list}\n\nPlease generate a touch command {task},"
touch_cmd_creator.prompt_add(prompt)
output = touch_cmd_creator.prompt_post()
print(output)
