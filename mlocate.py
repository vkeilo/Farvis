import subprocess
from syslogger import logger

class Mlocate():
    def __init__(self):
        # 检查ubuntu中是否安装有mlocate，没有就退出
        self.check_mlocate()

    def count_related_files(self, keyword):
        """
        统计与关键字相关的文件数量
        :param keyword: 关键字
        :return: 返回与关键字相关的文件数量
        """
        query = "locate -c" + keyword
        output = self.get_mlocate_output(query)
        logger.info(f"keyword[{keyword}] \trelated files: {output}")
        return int(output)

    def get_related_files(self, keyword):
        """
        获取与关键字相关的文件列表
        :keyword: 单个关键字
        :return: 返回与关键字相关的文件列表
        """
        query = "locate " + keyword
        output = self.get_mlocate_output(query)
        return output.split("\n")

    def check_mlocate(self):
        """
        检查ubuntu中是否安装有mlocate，没有就抛出异常
        :return: None
        """
        command = "mlocate"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicatat()
        if len(stderr) > 0:
            logger.error("mlocate is not installed")
            exit(1)
        
    def update_mlocate_database(self):
        """
        更新mlocate数据库
        :return: None
        """
        # 注意权限
        command = "sudo updatedb"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicatat()
        if len(stderr) > 0:
            logger.error("updatedb error")
            exit(1)

    def get_mlocate_output(self,query):
        """
        获取mlocate的输出
        :param query: 要搜索的内容
        :return: 返回一个包含mlocate输出的列表
        """
        logger.info(f"running query: {query}")
        command = query
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            return stdout
        

# 运行mlocate命令
command = "mlocate your_search_query"  # 将your_search_query替换为您要搜索的内容
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

# 检查是否有错误
if process.returncode == 0:
    # 如果没有错误，stdout包含mlocate的输出
    mlocate_output = stdout.decode('utf-8')
    print("mlocate输出:\n", mlocate_output)
else:
    # 如果有错误，stderr包含错误信息
    error_message = stderr.decode('utf-8')
    print("mlocate命令执行错误:\n", error_message)
