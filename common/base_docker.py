import docker

base_url = 'tcp://10.5.1.235:2345'
version = '1.19'
timeout = 10

'''
def containers_list():
    c = docker.Client(base_url='tcp://10.5.1.36:2345', version='1.19', timeout=10)
    return c.containers(all=True)


def containers_pause(containers_id):
    return make_response(json.dumps(connect.pause(container=containers_id)), 200)

@api.route('/api/containers_unpause/<containers_id>')
def containers_unpause(containers_id):
    return make_response(json.dumps(connect.unpause(container=containers_id)), 200)

@api.route('/api/containers_start/<containers_id>')
def containers_start(containers_id):
    return make_response(json.dumps(connect.start(container=containers_id)), 200)

@api.route('/api/containers_stop/<containers_id>')
def containers_stop(containers_id):
    return make_response(json.dumps(connect.stop(container=containers_id)), 200)

@api.route('/api/containers_restart/<containers_id>')
def containers_restart(containers_id):
    return make_response(json.dumps(connect.restart(container=containers_id)), 200)

@api.route('/api/containers_destroy/<containers_id>')
def containers_destroy(containers_id):
    return make_response(json.dumps(connect.destroy(container=containers_id)), 200)

@api.route('/api/containers_stats/<containers_id>')
def containers_stats(containers_id):
    return make_response(connect.stats(container=containers_id).next().strip(), 200)

# #images
@api.route('/api/images_list')
def images_list():
    return make_response(json.dumps(connect.images()), 200)

# #nodes
@api.route('/api/nodes_list')
def nodes_list():
    list = ['10.5.1.235:2345']
    result = []
    for host in list:
        connect = docker.Client(base_url='tcp://%s' % host, version='1.19', timeout=10)
        info = connect.info()
        info['Host'] = host
        result.append(info)

    return make_response(json.dumps(result), 200)


# #nodes
@api.route('/api/events_list')
def events_list():
    result = []
    events = connect.events(since=int(time.mktime(time.strptime('2015-12-29 17:00:00', "%Y-%m-%d %H:%M:%S"))))
    for e in events:
        print e
    print 'done'
    return make_response('111', 200)'''


class Docker():
    def __init__(self, ip):
        self.c = docker.Client(base_url='tcp://%s:2376' % ip, version='1.19', timeout=10)

    def images(self):
        return self.c.images()

    def containers(self):
        return self.c.containers()

if __name__ == '__main__':
    print Docker('192.168.128.128').containers()
