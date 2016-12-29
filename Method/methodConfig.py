# ecoding=utf-8
# Author: 翁彦彬 | Sven_Weng
# Email : sven_weng@wengyb.com
# Web   : http://wybblog.applinzi.com
from selenium.webdriver.common.by import By

SIMPLEREAD = {
	"TextView": (By.ID, u"com.example.svenweng.uiwidgettest:id/text_view"),
	"MainMenu": (By.XPATH, u"//android.widget.ImageView[@content-desc='更多选项']"),
	"ChangeTextView": (By.ID, u"com.example.svenweng.uiwidgettest:id/title"),
	"ButtonStartActivity": (By.ID, u'com.example.svenweng.uiwidgettest:id/button'),
	"SecondActivity": ".SecondActivity",
	"SecondActivity_TextView": (By.ID, u'com.example.svenweng.uiwidgettest:id/textView2')
}