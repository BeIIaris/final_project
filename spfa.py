#SPFA，Bellman-Ford优化算法，单源最短路
#时间复杂度O（nm）
#可以处理负权边、负环，容易被卡
import queue
class spfa:
    def __init__(self,n:int) -> None:
        self._side=[[] for i in range(n)]#邻接表存边
        self._value=[[] for i in range(n)]#邻接表存权值
        self._n=n#节点数

        #比较函数
        def cmp(x1,x2):
            if x1=='None':
                return False
            if x2=='None':
                return True
            return x1<x2
        self._cmp=cmp

    def push_oneway_side(self,u:int,v:int,w):#放入单向边
        u-=1
        v-=1
        self._side[u].append(v)
        self._value[u].append(w)

    def push_side(self,u:int,v:int,w):#放入双向边
        self.push_oneway_side(u,v,w)
        self.push_oneway_side(v,u,w)

    def calculate(self,start:int):#计算
        #计算初始化
        start-=1
        n=self._n
        dots_queue=queue.Queue()#队列
        in_queue=[False for i in range(n)]#入队记录
        self._ans=['None' for i in range(n)]#结果列表
        self._cnt=[0 for i in range(n)]#更新次数，用于处理负环
        self._Negative_circle=False#负环标记
        
        #起始点入队，启动算法
        self._ans[start]=0
        self._cnt[start]+=1
        dots_queue.put(start)
        in_queue[start]=True

        while not(dots_queue.empty()):
            #出队
            u=dots_queue.get()
            in_queue[u]=False

            for i in range(len(self._side[u])):
                v=self._side[u][i]
                w=self._value[u][i]

                #松弛操作
                if self._cmp(w+self._ans[u],self._ans[v]):
                    self._ans[v]=w+self._ans[u]
                    self._cnt[v]+=1

                    if(self._cnt[v]>=n):#如果存在负环就结束
                        self._Negative_circle=True
                        break

                    if not(in_queue[v]):#如果在队列就不入队
                        in_queue[v]==True
                        dots_queue.put(v)
      
    def clear(self):
        n=self._n
        self._side=[[] for i in range(n)]
        self._value=[[] for i in range(n)]
        self._ans=[]
        self._cnt=[0 for i in range(n)]
        self._Negative_circle=False

    def get_ans(self,end:int):
        end-=1
        if self._Negative_circle:
            return 'Negative circle exists'
        return self._ans[end]


# 实现步骤：        
# 1.spfa求最短路（没有负环） 
# （1）初始化dist数组（求最短路一定要初始化）
# （2）把所有点都入队，入队的点都用一个bool数组标记为true，表示在队列中（需要更新）
# （3）取出队首的点，将该点标记为false，遍历它的出边，更新其他点
# （4）其他点被更新后，如果不在队列中，就入队，并标记为true
# （5）重复上述步骤，直到队列为空

# 2.spfa判断是否存在负环（需要多设置一个cnt数组）
# （1）初始化dist数组（虽然不初始化也可以）
# （2）把所有点都入队，入队的点都用一个bool数组标记为true，表示在队列中（需要更新）
# （3）取出队首的点，将该点标记为false，遍历它的出边，更新其他点
# （4）更新cnt数组，如果某个点的cnt>=n，那么就i说明有负环
# （5）其他点被更新后，如果不在队列中，就入队，并标记为true
# （6）重复上述步骤，直到队列为空