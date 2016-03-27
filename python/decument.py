#!/usr/bin/env python
#coding:utf-8
try:
  import xml.etree.cElementTree as ET 
except ImportError: 
  import xml.etree.ElementTree as ET 
import sys 
  
try: 
  tree = ET.parse("config.xml")     #打开xml文档 
  root = tree.getroot()         #获得root节点  
except Exception, e: 
  print "Error:cannot parse file:country.xml."
  sys.exit(1) 
print root.tag, "---", root.attrib  
for child in root: 
  print child.tag, "---", child.attrib 
  
print "*"*10
print root[0][1].text   #通过下标访问 
print root[0].tag, root[0].text 
print "*"*10
