from bottle import route, request, response
import time , subprocess
import algebra, monkey_patching

@route('/')
def welcome():
    return '<h1> Howdy! </h1>'

@route('/area/circle')
def circle_area_service():
    radius = float(request.query.get('radius','0'))   # request.query is a dict
    print 'radius is',radius
    area = algebra.area(radius)
    return dict(radius=radius, area=area, service=request.path)
    
@route('/now')
def show_time():
    response.content_type = 'text/plain'
    response.set_header('Cache-Control','max-age=10')
    return time.ctime()

@route('/interfaces')
def show_interfaces():
    response.content_type = 'text/plain'
    return subprocess.check_output(['netstat','-i'])

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)   #make debug False during actual production
    
    
