mysubjects = [ "Math201","CoE202","CoE203","CoE241","EE202","EE212","ICS102"]
mynewlist = mysubjects.copy()
mynewlist.append("ICS201")
print(mynewlist)
print(len(mynewlist))
mysubjects.remove("ICS102")
print(mysubjects)
mysubjects.clear()
print(mysubjects)
