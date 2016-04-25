from bottle import template

family_plain_text = '''
The {{lastname.title()}} Family
--------------------
% for name in first_names:
* {{name.title()}}
% end
'''

family_html = '''
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
  % for name in first_names:
     <li> {{name.title()}} </li>
  % end
  </ol>
</body>
</html>
'''

print template(family_html,
               lastname = 'simpsons',
               first_names = 'homer<father> marge bart lisa maggie'.split())


