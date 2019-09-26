#coding=utf-8
#import switch as switch

#from src.seleniumMain_master.package_selenium.reconstitution_package.Driver import dr
import dr as dr


def element(element, name):
    try:

        if element.__eq__("id"):
            a = dr.find_element_by_id(name)
        elif element.__eq__("name"):
            a = dr.find_element_by_name(name)
        elif element.__eq__("classname"):
            a = dr.find_element_by_class_name(name)
        elif element.__eq__("tagname"):
            a = dr.find_element_by_tag_name(name)
        elif element.__eq__("css"):
            a = dr.find_element_by_css_selector(name)
        elif element.__eq__("xpath"):
            a = dr.find_element_by_xpath(name)
        elif element.__eq__("linktext"):
            a = dr.find_element_by_link_text(name)
        elif element.__eq__(""):
            a = dr.f(name)
        elif element.__eq__(""):
            a = dr.find_element_by_name(name)
        else:
            print("输入格式错误。有以下格式"
                  "id,name,classname,tagname,css,xpath,linktext"
                  "如：element(\"name\",\"login\")")
        return a
    except Exception as e:
        return "格式错误或者查找不到"

"""
def element(element,name)

def element(a,b,c)

"""
