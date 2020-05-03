Traceback (most recent call last):
  File "aa.py", line 51, in <module>
    import urllib.request,os; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); open(os.path.join(ipp, pf), 'wb').write(urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ','%20')).read())
NameError: name 'sublime' is not defined

***Repl Closed***




x=input("what?")
print('hello,x')