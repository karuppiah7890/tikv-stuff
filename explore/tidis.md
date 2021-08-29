https://github.com/yongman/tidis

https://xiking.win/tidis/

```bash
tidis-docker-compose $ git clone https://github.com/yongman/tidis-docker-compose.git

tidis-docker-compose $ cd tidis-docker-compose/

tidis-docker-compose $ docker-compose up -d
[+] Running 11/11
 ⠿ pd Pulled                                                                                                   18.4ss
   ⠿ 9812b53cc158 Pull complete                                                                                 4.2ss
   ⠿ e8355eb28dda Pull complete                                                                                 4.4ss
   ⠿ 1197d937b561 Pull complete                                                                                13.8s
   ⠿ 145e91b0363f Pull complete                                                                                14.3s
 ⠿ tidis Pulled                                                                                                17.7s
   ⠿ ffa04466427c Pull complete                                                                                13.5s
 ⠿ tikv Pulled                                                                                                 51.5s
   ⠿ 9d48c3bd43c5 Pull complete                                                                                 2.1s
   ⠿ a5bfcc748ffc Pull complete                                                                                45.6s
   ⠿ 6ac6ee01b237 Pull complete                                                                                47.3s
[+] Running 4/4
 ⠿ Network tidis-docker-compose_default    Created                                                              0.0s
 ⠿ Container tidis-docker-compose_pd_1     Started                                                              1.0s
 ⠿ Container tidis-docker-compose_tikv_1   Started                                                              1.4s
 ⠿ Container tidis-docker-compose_tidis_1  Started                                                              2.2s
tidis-docker-compose $ docker-compose ps
NAME                           COMMAND                  SERVICE             STATUS              PORTS
tidis-docker-compose_pd_1      "/pd-server --name=p…"   pd                  running             0.0.0.0:50689->2379/tcp, 2380/tcp
tidis-docker-compose_tidis_1   "/tidis-server -conf…"   tidis               running             0.0.0.0:5379->5379/tcp, :::5379->5379/tcp
tidis-docker-compose_tikv_1    "/tikv-server --addr…"   tikv                running             20160/tcp
tidis-docker-compose $ redis-cli -p 5379
127.0.0.1:5379> dbsize
(error) ERR command error
127.0.0.1:5379> DBSIZE
(error) ERR command error
127.0.0.1:5379> info
# Server
redis_mode:standalone
127.0.0.1:5379> info status
# Cluster
cluster_enabled:0
127.0.0.1:5379> info status
# Cluster
cluster_enabled:0
127.0.0.1:5379> info server
# Cluster
cluster_enabled:0
127.0.0.1:5379> info 
# Server
redis_mode:standalone
127.0.0.1:5379> info something
# Cluster
cluster_enabled:0
127.0.0.1:5379> info 
# Server
redis_mode:standalone
127.0.0.1:5379> get blah
(nil)
127.0.0.1:5379> set blah bloo
OK
127.0.0.1:5379> get blah
"bloo"
127.0.0.1:5379> 
```

This is pretty interesting!! :)

It doesn't have support for all features in Redis, because it's not Redis :P But it's good enough

For example there's no `DBSIZE` or `KEYS *` or `WATCH`, but anyways, it's still a big list of commands that's been implemented, from what I see in the repo readme


