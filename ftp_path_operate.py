#!/usr/bin/python
# -*- coding:utf-8 -*-
# @File     : ftp_path_operate.py
# @Author   : lihui
# @Time     : 2019/11/4 11:03
# @Software : PyCharm
# 说明      : 删除和上传目录
import ftplib
import os


class FTPPath(object):
    lines = []

    def __init__(self, path, user, password):
        self.ftp = ftplib.FTP(path, user, password)

    def __del__(self):
        self.ftp.close()

    def __clear_lines(self):
        self.lines = []

    def __save_line(self, line):
        self.lines.append(line)

    def delete_path(self, path):
        """
        删除一个目录及其中全部的文件
        由于FTP只能删除空目录，要递归删除
        :param path:
        :return:
        """
        self.__clear_lines()
        self.ftp.cwd(path)
        self.ftp.retrlines("LIST", callback=self.__save_line)
        self.ftp.cwd('/')
        for line in self.lines:
            name = path + "/" + line.split(" ")[-1]
            if line[0] == "d":
                self.delete_path(name)
            else:
                self.ftp.delete(name)
        self.ftp.rmd(path)

    def __upload_file(self, file_name):
        """
        上传文件
        :param file_name:
        :return:
        """

        upload_path = "/" + os.path.split(file_name)[0].replace("\\", '/')
        with open(file_name, 'rb') as fd:
            self.ftp.cwd(upload_path)
            self.ftp.storbinary("STOR %s" % os.path.split(file_name)[-1], fd)

    def upload_path(self, path):
        """
        将路径下的文件全部上传
        :param path:
        :return:
        """
        files = os.listdir(path)
        pathname = os.path.split(path)[-1]

        upload_path = "/" + os.path.split(path)[0].replace("\\", '/')

        self.ftp.cwd(upload_path)
        self.ftp.mkd(pathname)

        for fi in files:
            fi_d = os.path.join(path, fi)
            if os.path.isdir(fi_d):
                self.upload_path(fi_d)
            else:
                self.__upload_file(fi_d)
