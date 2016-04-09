
# See bottle tutorial at:  http://bottlepy.org/docs/dev/tutorial.html

from bottle import run, route, request, response
import time, subprocess, algebra, monkey_patching

@route('/')
def welcome():
    return '<h1> Howdy! </h1>'

@route('/now')
def show_time():
    response.content_type = 'text/plain'
    response.set_header('Cache-Control', 'max-age=1')                        
    return time.ctime()

@route('/interfaces')
def show_netstat():
    response.content_type = 'text/plain'
    return subprocess.check_output(['netstat', '-i'])

@route('/area/circle')
def circle_area_service():
    radius = float(request.query.get('radius', '0'))
    area = algebra.area(radius)
    return dict(radius=radius, area=area, service=request.path)

if __name__ == '__main__':
    run(host='', port=8081, server='gunicorn', workers=4)
    # run(host='localhost', port=8081, debug=True)
