import consul
c = consul.Consul(host='127.0.0.1', port=8500)

# in another process
c.kv.put('foo', 'bar')

# poll a key for updates
index = None
while True:
    index, data = c.kv.get('foo', index=index)
    print(data['Value'])


