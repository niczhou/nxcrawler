#coding = utf-8

import tkinter as tk
from NxUI import NxUI
from EdCrawler import EdCrawler

# ui = NxUI()
# ui.create_view()

ecrawler = EdCrawler()
ecrawler.search_ed2k("keyword")