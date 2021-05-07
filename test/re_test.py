#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/8 14:33
# @Author  : Beam
# @File    : re_test.py


dic = {'aof_rewrite_in_progress': '0', 'total_connections_received': '18249074', 'IP': '10.51.29.61', 'used_cpu_sys_children': '766.73', 'run_id': 'e2191df08ba291196a16e6a9f803f118a73a7a65', 'rejected_connections': '0', 'redis_build_id': 'ad0305d3dd5b541a', 'used_memory_peak_human': '11.27M', 'pubsub_patterns': '0', 'redis_mode': 'standalone', 'connected_slaves': '0', 'uptime_in_days': '205', 'multiplexing_api': 'epoll', 'lru_clock': '10292188', 'redis_version': '3.0.2', 'redis_git_sha1': '00000000', 'sync_partial_ok': '0', 'migrate_cached_sockets': '0', 'gcc_version': '4.8.2', 'connected_clients': '27', 'keyspace_misses': '27747211', 'used_memory': '9953392', 'tcp_port': '6390', 'master_repl_offset': '0', 'used_cpu_user_children': '3621.81', 'repl_backlog_first_byte_offset': '0', 'rdb_current_bgsave_time_sec': '-1', 'pubsub_channels': '0', 'used_cpu_user': '18957.74', 'used_memory_lua': '36864', 'instantaneous_ops_per_sec': '1', 'rdb_last_save_time': '1486686903', 'total_commands_processed': '88830553', 'aof_last_write_status': 'ok', 'role': 'master', 'cluster_enabled': '0', 'aof_rewrite_scheduled': '0', 'sync_partial_err': '0', 'used_memory_rss': '13176832', 'hz': '10', 'sync_full': '0', 'aof_enabled': '0', 'config_file': '/usr/local/webserver/redis/etc/cache.conf', 'Hostname': 'iZ23se6hqjcZ', 'used_cpu_sys': '8544.82', 'rdb_last_bgsave_status': 'ok', 'instantaneous_output_kbps': '1.29', 'latest_fork_usec': '613', 'aof_last_bgrewrite_status': 'ok', 'aof_last_rewrite_time_sec': '-1', 'used_memory_human': '9.49M', 'loading': '0', 'blocked_clients': '0', 'process_id': '18814', 'repl_backlog_histlen': '0', 'client_biggest_input_buf': '0', 'aof_current_rewrite_time_sec': '-1', 'arch_bits': '64', 'repl_backlog_active': '0', 'mem_fragmentation_ratio': '1.32', 'rdb_last_bgsave_time_sec': '0', 'expired_keys': '5957903', 'db9': 'keys=20,expires=0,avg_ttl=0', 'total_net_input_bytes': '7076848834', 'evicted_keys': '0', 'db11': 'keys=2,expires=0,avg_ttl=0', 'db10': 'keys=44122,expires=158,avg_ttl=73199502', 'rdb_bgsave_in_progress': '0', 'repl_backlog_size': '1048576', 'instantaneous_input_kbps': '0.04', 'client_longest_output_list': '0', 'mem_allocator': 'jemalloc-3.6.0', 'total_net_output_bytes': '6819484492', 'used_memory_peak': '11812488', 'uptime_in_seconds': '17739045', 'rdb_changes_since_last_save': '36', 'redis_git_dirty': '0', 'os': 'Linux', 'keyspace_hits': '13043324'}

# ls = []
# tempdic = {}
# for key in dic:
#     if 'db' in key:
#         ls.append(key+':'+dic[key])
# for i in ls:
#     if i.startswith('db'):
#         tempdic[i.split(':')[0]] = i.split(':')[1]
# dbdict = {}
# dbdict['Keyspace'] = tempdic
#
# print(dbdict['Keyspace']['db9'])


import re
dbdict = {}
for key in dic:
    if re.search('^db*',key):
        dbdict[key] = dic[key]
dic['Keyspace'] = dbdict
print(dic['Keyspace']['db9'])
