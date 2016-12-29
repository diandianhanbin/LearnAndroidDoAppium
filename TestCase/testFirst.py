# ecoding=utf-8
# Author: 翁彦彬 | Sven_Weng
# Email : sven_weng@wengyb.com
# Web   : http://wybblog.applinzi.com
# 本地测试对象的APK下载地址 http://pan.baidu.com/s/1gfKCJTp 中的testFirst.apk

import sys

sys.path.append("..")  # 保证上级config的引用
reload(sys)
sys.setdefaultencoding("utf-8")
import unittest

from Method.SimpleRead import SimpleRead
from BaseDriver.Driver import AppiumBaseTest


class MessageSimpleRead(AppiumBaseTest, SimpleRead):
	def test001_checkTextView(self):
		"""测试TextView内容是否正确"""
		textcontent = self.getTextView()
		self.assertEqual('This is a TextView!', textcontent)

	def test002_checkChangeTextView(self):
		"""测试修改TextView的内容"""
		self.clickMenu()
		self.clickMenusLabel(1)
		textcontent = self.getTextView()
		self.assertEqual('Change Text', textcontent)

	def test003_changeActivity(self):
		"""跳转Activity测试"""
		self.clickButtonStartActivity()
		self.assertEqual(self.checkSecondActivity(), True)
		self.assertEqual(self.getSecondActivityTextView(), u'This is Second Activity')

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(MessageSimpleRead)
	unittest.TextTestRunner(verbosity=2).run(suite)
