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


class Images():
    def __init__(self, ip):
        self.c = docker.Client(base_url='tcp://%s:2376' % ip, version='1.19', timeout=5)

    def list(self, name):
        return self.c.images(name=name)

    def search(self, term):
        self.c.search(term=term)

    def pull(self, repository):
        self.c.pull(repository=repository)

    def inspect(self, image):
        return self.c.inspect_image(image=image)

    def remove(self, image):
        return self.c.remove_image(image=image)


class Containers():
    def __init__(self, ip):
        self.c = docker.Client(base_url='tcp://%s:2376' % ip, version='1.19', timeout=5)

    def list(self):
        return self.c.containers(all=True)

    def start(self, container):
        return self.c.start(container=container)

    def stop(self, container):
        return self.c.stop(container=container)

    def delete(self, container):
        return self.c.remove_container(container=container, force=True)

if __name__ == '__main__':
    # print Images('192.168.128.128').list('*/mon*')
    # print Images('192.168.128.128').remove('ubuntu')
    # print Images('192.168.128.128').inspect('b2cdf227209f9f8d119974698e0912b93c15736249e64415d02aed2576ae3994')
    print Containers('192.168.128.128').list()

    # print Containers('192.168.128.128').start('03c0301cdeb2c884e817e9ed2c39e30e753c02ddee7c12dbe93bc7033e432786')
    # print Containers('192.168.128.128').stop('03c0301cdeb2c884e817e9ed2c39e30e753c02ddee7c12dbe93bc7033e432786')
    print Containers('192.168.128.128').delete('03c0301cdeb2c884e817e9ed2c39e30e753c02ddee7c12dbe93bc7033e432786')

