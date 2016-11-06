import socket, time, json, os, psutil, datetime


def get_process_list():
    ps_list = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name'])
        except psutil.NoSuchProcess:
            pass
        else:
            ps_list.append(pinfo)

    return ps_list

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ""
port = 9999
serversocket.bind((host, port))

serversocket.listen(5)

print("Socket for Monitoring Server started")

while True:

    clientsocket,addr = serversocket.accept()

    print("Got a connection from %s" % str(addr))
    currentTime = time.ctime(time.time())
    data = {'status': 'ok',
            'request_host': str(addr),
            'server_time': currentTime,
            'cpu count': psutil.cpu_count(logical=False),
            'cpu_load': psutil.cpu_percent(interval=None, percpu=True),
            'boot_time': datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"),
            'process_list': get_process_list()}
    jdata = json.dumps(data)
    clientsocket.send(jdata.encode('utf-8'))
    clientsocket.close()