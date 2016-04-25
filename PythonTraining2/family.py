from bottle import template

lastname = 'hettingers'
first_names = 'raymond<Father> rachel matthew'

### put '!' in front of the variable which you want the template to escape '<' and '>' if output is not HTML.
t_text = '''\
The {{lastname.title()}} Family
---------------------
%for first_name in first_names:
* {{!first_name.title()}}               
%end
'''
print template(t_text,
               first_names = first_names.split(),
               lastname = lastname)

t_html ='''
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="utf-8">
   <title> {{lastname.title()}} Family </title>
</head>
<body>
  <h1> The <em> {{lastname.title()}} </em> Family </h1>
  <hr>
  <ol>
% for first_name in first_names:  
     <li> {{first_name.title()}} </li>
% end
  </ol>
</body>
</html>
'''

lastname = 'simpsons'
first_names = 'homer<Father> marge bart lisa maggie'

print template(t_html,
               first_names = first_names.split(),
               lastname = lastname)
