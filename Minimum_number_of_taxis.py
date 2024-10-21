# task: https://www.codewars.com/kata/5e1b37bcc5772a0028c50c5d
import heapq


def min_num_taxis(requests):
    heapq.heapify(requests)
    res = []
    while requests:
        first = requests[0][0]
        for request in requests:
            if request[0] == first:
                need_new = True
                for taxi in res:
                    if taxi[-1] < first:
                        taxi.extend(list(range(request[0], request[1] + 1)))
                        requests.remove(request)
                        need_new = False
                        break
                if need_new:
                    res.append(list(range(request[0], request[1] + 1)))
                    requests.remove(request)
            else:
                break
    return len(res)



'''var2()
def min_num_taxis(requests):
    res = []
    requests.sort(key=lambda x: (x[0], -len(x)))
    while requests:
        first = requests[0][0]
        for request in requests:
            if request[0] == first:
                need_new = True
                for taxi in res:
                    if taxi[-1] < first:
                        taxi.extend(list(range(request[0], request[1] + 1)))
                        requests.remove(request)
                        need_new = False
                        break
                if need_new:
                    res.append(list(range(request[0], request[1] + 1)))
                    requests.remove(request)
            else:
                break
    return len(res)
'''

'''var1
def min_num_taxis(requests):
    d = [[]]
    for r in requests:
        need_new = True
        for taxi in sorted(d, key=len, reverse=True):
            busy = False
            for h in range(r[0], r[1] + 1):
                if h in taxi:
                    busy = True
                    break
            if busy:
                continue
            else:
                taxi.extend(list(range(r[0], r[1] + 1)))
                need_new = False
                break
        if need_new:
            d.append(list(range(r[0], r[1] + 1)))
    return len(d)
'''

requests = [(1, 4), (2, 6)]
print(min_num_taxis(requests)) #2
requests = [(1, 4), (5, 9)]
print(min_num_taxis(requests)) #1
requests = [(1,4), (2, 9), (3, 6)]
print(min_num_taxis(requests)) #3
requests = [(1, 4), (2, 9), (2, 13), (14, 15)]
print(min_num_taxis(requests)) #3