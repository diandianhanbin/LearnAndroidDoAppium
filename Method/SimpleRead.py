# ecoding=utf-8
# Author: 翁彦彬 | Sven_Weng
# Email : sven_weng@wengyb.com
# Web   : http://wybblog.applinzi.com

import methodConfig

from BaseDriver.BaseCommon import AppUI


class SimpleRead(AppUI):

	# ----------------------新闻简读所有数据--------------------------
	TextView = methodConfig.SIMPLEREAD['TextView']
	MainMenu = methodConfig.SIMPLEREAD['MainMenu']
	ChangeTextView = methodConfig.SIMPLEREAD['ChangeTextView']
	ButtonStartActivity = methodConfig.SIMPLEREAD['ButtonStartActivity']
	SecondActivity = methodConfig.SIMPLEREAD['SecondActivity']
	SecondActivityTextView = methodConfig.SIMPLEREAD['SecondActivity_TextView']

	# --------------------------------------------------------------

	# -------------------------执行方法------------------------------
	def getTextView(self):
		"""
		获取TextView
		:return:str, 标题文本
		"""
		return self.getTextOfElement(*self.TextView)

	def clickMenu(self):
		"""
		点击Menu菜单
		:return:
		"""
		self.clickElement(*self.MainMenu)

	def clickChangeTextView(self):
		"""
		点击Menu菜单中的改变标签文本
		:return:
		"""
		self.clickElement(*self.ChangeTextView)

	def clickMenusLabel(self, num):
		"""
		点击Menu菜单中的标签
		:param num: 标签从上到下的顺序
		:return:
		"""
		self.find_elements(*self.ChangeTextView)[num].click()

	def clickButtonStartActivity(self):
		"""
		点击按钮启动Activity
		:return:
		"""
		self.clickElement(*self.ButtonStartActivity)

	def checkSecondActivity(self):
		"""
		检查是否启动第二个Activity
		:return: True or False
		"""
		return self.waitActivity(self.SecondActivity)

	def getSecondActivityTextView(self):
		"""
		获取第二个Activity的文本内容
		:return:
		"""
		return self.getTextOfElement(*self.SecondActivityTextView)
