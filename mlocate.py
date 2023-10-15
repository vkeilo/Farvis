import subprocess
from syslogger import logger

class Mlocate():
    def __init__(self,threshold = 100):
        # 检查ubuntu中是否安装有mlocate，没有就退出
        self.check_mlocate()
        # 最大的可统计的文件计数阈值，超过了就不计入了
        self.count_threshold = threshold

    def count_related_files(self, keyword):
        """
        统计与关键字相关的文件数量
        :param keyword: 关键字
        :return: 返回与关键字相关的文件数量
        """
        query = "locate -c " + keyword
        output = self.get_mlocate_output(query)
        logger.info(f"keyword[{keyword}] \trelated files num: {output}")
        return int(output)

    def get_related_files_by_keyword(self, keyword):
        """
        获取与关键字相关的文件列表
        :keyword: 单个关键字
        :return: 返回与关键字相关的文件绝对路径列表
        """
        query = "locate " + keyword
        output = self.get_mlocate_output(query)
        return output.split("\n")

    def get_related_files_by_keywords(self, keyword_list) -> list:
        """
        获取与关键字列表相关的文件的绝对路径列表
        :keyword_list: 关键字列表
        :return: 返回与关键字相关的文件绝对路径列表
        """
        related_file_count_dic = {keyword: self.count_related_files(keyword) for keyword in keyword_list}
        # 删除字典中值大于count_threshold的键值对
        related_file_count_dic = {keyword: count for keyword, count in related_file_count_dic.items() if
                                   count <= self.count_threshold}
        related_file_path_dic = {keyword: self.get_related_files_by_keyword(keyword) for keyword in related_file_count_dic}
        union_file_path_list = []
        for keyword, file_path_list in related_file_path_dic.items():
            logger.info(f"get keyword[{keyword}] \trelated files path: {file_path_list}")
            union_file_path_list.extend(file_path_list)
        return union_file_path_list

    def check_mlocate(self):
        """
        检查ubuntu中是否安装有mlocate，没有就抛出异常
        :return: None
        """
        command = "locate -h"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        _, stderr = process.communicate()
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
        :return: locate 命令语句输出，执行失败就是空字符串
        """
        logger.info(f"running query: {query}")
        command = query
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            return stdout.decode("utf-8")
        else:
            logger.error(f"mlocate query error:{query}")
            return ""


        

