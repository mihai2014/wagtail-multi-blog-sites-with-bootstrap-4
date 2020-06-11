#def traverse0(item):
#    print("-",item.title,item.url)
#    for item in item.get_children():      #.live().in_menu()
#        traverse2(item)

#html_menu = ''

#def traverse(item):
#
#    global html_menu
#
#    html_menu += "<li><a href="+item.url+">"+item.title+"</a></li>\n"
#
#    if (item.numchild != 0):
#        html_menu += "<ul>\n"
#        for item in item.get_children():
#            traverse(item)
#        html_menu += "</ul>\n"

#def get_tree(obj,is_live=True,is_in_menu=None):
#
#    global html_menu
#
#    #reset string
#    html_menu = ''
#
#    if(is_in_menu == None):
#        page = obj.objects.filter(live=is_live)[0]
#    else:
#        page = obj.objects.filter(live=is_live, show_in_menus=is_in_menu)[0]
#    traverse(page)
#
#    return html_menu



class PageTree:

    def __init__(self, page, live=True, menu=None):
        self.html_menu = ""
        self.menu = menu
        self.live = live
        self.traverse(page)

    def traverse(self,item):
        
        if(item.show_in_menus == self.menu) or (self.menu == None):
            if(item.live == self.live):
                self.html_menu += "<li><a href="+item.url+">"+item.title+"</a></li>\n"

        if (item.numchild != 0):
            self.html_menu += "<ul>\n"
            for i in item.get_children():
                self.traverse(i)
            self.html_menu += "</ul>\n"


def readFile(path):
    try:
        f = open(path, "r")
        str = f.read();
        f.close()
        return str
    except:
        return ""

def writeFile(path,string):
    f = open(path, "wb")
    f.write(string.encode('utf-8'))
    f.close()

