from bs4 import BeautifulSoup as bs

def test_bs4():
	xml_string = "<open></open>"
	print(bs(xml_string, "xml"))