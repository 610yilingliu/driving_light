import random

# 0近光,1远光,2远近
sols = {
'夜间在没有路灯，照明不良条件下行驶': 1,
'夜间同方向近距离跟车行驶':0,
'夜间与机动车会车':0,
'夜间在照明良好的道路上行驶':0,
'夜间直行通过路口':0,
'夜间超越前方车辆':2,
'夜间通过坡路拱桥':2,
'夜间通过急弯拱桥':2,
'夜间通过急弯坡路':2,
'夜间通过拱桥人行横道':2,
'夜间通过没有交通信号灯控制的路口':2,
'雾天行驶':{"fog","warn"},
'夜间在道路上发生故障，阻碍交通但难以移动':{'warn','size'},
'路边临时停车':{'warn','size'},
'夜间通过没有交通信号灯的路口':2
}


class status():
    def __init__(self,val):
        self.current_status = val
    def set_status(self, now_status):
        self.current_status = now_status
    def status_add(self):
        self.current_status +=1
    def status_minus(self):
        self.current_status -=1
    def get_status(self):
        return self.current_status

def light(current_status):
    if current_status == 0:
        print("近光灯打开")
    if current_status == 1:
        print("远光灯打开")
    if current_status == 2:
        print("双闪")


def key_presses(current):
    in_string = input()
    sta = status(current)

    if in_string == 'w':
        try: 
            sta.status_add()
            print("Current Status", sta.get_status())
            if type(sta.get_status()) == int and sta.get_status() > 2:
                print('Reach to Max')
            else:
                light(sta.get_status())
            return(key_presses(sta.get_status()))
        except:
            sta.set_status(0)
            light(sta.get_status())
            return(key_presses(sta.get_status()))

    if in_string == 's':
        try:
            sta.status_minus()
            print("Current Status", sta.get_status())
            if type(sta.get_status()) == int and sta.get_status() < 0:
                print('Light off')
            else:
                light(sta.get_status())
            return(key_presses(sta.get_status()))
        except:
            return "err"

    if in_string == 'f':
        try:
            sta.current_status.add('fog')
            print('fog light on')
            return(key_presses(sta.get_status()))
        except:
            sta.set_status(set())
            sta.current_status.add('fog')
            print('fog light on')
            return(key_presses(sta.get_status()))

    if in_string == 'warn':
        try:
            sta.current_status.add('warn')
            print('Warning light on')
            return(key_presses(sta.get_status()))           
        except:
            sta.current_status = set()
            sta.current_status.add('warn')
            print('Warning light on')
            return(key_presses(sta.get_status())) 

    if in_string == 'size':
        try:
            sta.current_status.add('size')
            print('Size light on')
            return(key_presses(sta.get_status())) 
        except:
            sta.current_status = set()
            sta.current_status.add('size')
            print('Size light on')
            return(key_presses(sta.get_status())) 

    if in_string == 'done':
        print('submitted')
        return sta.get_status()


# def start(init):
#     print("Started")
#     for i in range(0,5):
#         pos = random.randint(0,len(sols)-1)
#         key = list(sols.keys())[pos]
#         print("Question",i+1)
#         print(key)
#         ans = list(sols.values())[pos]
#         state = key_presses(init)
#         if state == ans:
#             print("T")
#         else:
#             print("F")

# if __name__ == "__main__":
#     start(-1)


if __name__ == "__main__":
    container = -1
    print("Started")
    for i in range(0,5):
        pos = random.randint(0,len(sols)-1)
        key = list(sols.keys())[pos]
        ans = list(sols.values())[pos]
        print("Question",i+1)
        print(key)
        stat = key_presses(container)
        if stat == ans:
            print("T")
        else:
            print("F")
           
        container = stat
