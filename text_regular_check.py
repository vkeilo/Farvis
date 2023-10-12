# 构建一个函数，对一个字符串进行正则检查，确保字符串可以在被eval解析后，能够解析为一个字符串数组，只能使用单引号
import re




# 匹配单引号的字符串列表文本   类似： ['hello', 'world', 'python']
def is_str_list_text(str) -> bool:
    pattern = re.compile(r"\['[^']+(?:','[^']+)+'\]")
    result = re.match(pattern, str)
    matched_flag = result is not None
    return matched_flag
