FILE_PATH = 'example1.log.txt'

total_requests = 0
total_data = 0
requested_resource_details = {}
remote_host_details = {}
request_status_details = {'1xx': 0, '2xx': 0, '3xx': 0, '4xx': 0, '5xx': 0}

file = open(FILE_PATH, 'r')
for line in file:
    line = line.strip()
    fields = line.split(' ')
    
    total_requests = total_requests + 1
    total_data = total_data + int(fields[-1])
    
    if fields[0] in remote_host_details:
        remote_host_details[fields[0]] = remote_host_details[fields[0]] + 1
    else:
        remote_host_details[fields[0]] = 1
    
    if fields[6] in requested_resource_details:
        requested_resource_details[fields[6]] = requested_resource_details[fields[6]] + 1
    else:
        requested_resource_details[fields[6]] = 1
    
    if fields[8][0] == '1':
        request_status_details['1xx'] = request_status_details['1xx'] + 1
    elif fields[8][0] == '2':
        request_status_details['2xx'] = request_status_details['2xx'] + 1
    elif fields[8][0] == '3':
        request_status_details['3xx'] = request_status_details['3xx'] + 1
    elif fields[8][0] == '4':
        request_status_details['4xx'] = request_status_details['4xx'] + 1
    elif fields[8][0] == '5':
        request_status_details['5xx'] = request_status_details['5xx'] + 1

file.close()

sorted_remote_host_details = sorted(remote_host_details.items(), key=lambda x: x[1])
sorted_requested_resource_details = sorted(requested_resource_details.items(), key=lambda x: x[1])

print(f'Total Requests: {total_requests}')
print(f'Total Data transmitted: {total_data / (1024 * 1024 * 1024):.1f}GiB')
print(f'Most requested resource: {sorted_requested_resource_details[-1][0]}')
print(f'Total requests for {sorted_requested_resource_details[-1][0]}: {sorted_requested_resource_details[-1][1]}')
print(f'Percentage of requests for {sorted_requested_resource_details[-1][0]}: {(sorted_requested_resource_details[-1][1] / total_requests) * 100:.10f}')
print(f'Remote host with the most requests: {sorted_remote_host_details[-1][0]}')
print(f'Total requests from  {sorted_remote_host_details[-1][0]}: {sorted_remote_host_details[-1][1]}')
print(f'Percentage of requests from {sorted_remote_host_details[-1][0]}: {(sorted_remote_host_details[-1][1]/ total_requests) * 100:.10f}')
print(f'Percentage of 1xx requests: {(request_status_details["1xx"] / total_requests) * 100:.10f}')
print(f'Percentage of 2xx requests: {(request_status_details["2xx"] / total_requests) * 100:.10f}')
print(f'Percentage of 3xx requests: {(request_status_details["3xx"] / total_requests) * 100:.10f}')
print(f'Percentage of 4xx requests: {(request_status_details["4xx"] / total_requests) * 100:.10f}')
print(f'Percentage of 5xx requests: {(request_status_details["5xx"] / total_requests) * 100:.10f}')
