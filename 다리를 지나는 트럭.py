import queue

def solution(bridge_length, weight, truck_weights):
    q = queue.Queue()

    for i in range(0, bridge_length):
        q.put(0)

    q.get() ; q.put(truck_weights[0])
    time = 1 ; q_weight = truck_weights[0] ;
    del truck_weights[0]
    value = len(truck_weights)+1

    while (len(truck_weights) > 0):
        out_truck = q.get()

        if out_truck is not 0:
            value = value-1
            q_weight = q_weight - out_truck

        time = time + 1

        if q.qsize() > bridge_length:
            continue

        if q_weight + truck_weights[0] <= weight:
            q.put(truck_weights[0])
            q_weight = q_weight + truck_weights[0]
            del truck_weights[0]

        else:
            q.put(0)

    while q.qsize() > 0 and value is not 0:
        t = q.get_nowait()
        time = time + 1

        if t is not 0:
            value=value-1

    return time

bridge_length_list = [2, 100, 100]
weight_list = [10, 100, 100]
truck_weights_list = [[7,4,5,6], [10], [10,10,10,10,10,10,10,10,10,10]]

for i in range(0, 3):
    answer = solution(bridge_length_list[i], weight_list[i], truck_weights_list[i])
    print("{}. answer = {}".format(i, answer))