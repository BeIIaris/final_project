#dijkstra算法，单源最短路
#时间复杂度O（m*logn），适用于稀疏图
#无法处理负环问题
import heap
class dijkstra:
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
        self._ans=['None' for i in range(n)]#结果列表
        renewed=[0 for i in range(n)]#是否更新过
        
        #设置堆
        class node:
            def __init__(self,num,val) -> None:
                self.num=num
                self.val=val
        def cmp_hp(x1:node,x2:node):
            return x1.val<x2.val
        hp=heap.heap(cmp_hp)
    
       #放入起点，启动算法
        self._ans[start]=0
        st=node(start,0)
        hp.push(st)
        #循环，堆内有值就不结束
        while not(hp.empty()):
            #弹出
            u=hp.top();
            hp.pop();
            u=u.num;
            #如果更新过就弹下一个
            if(renewed[u]):
                continue;
            renewed[u]=1

            #更新结果值
            for i in range(len(self._side[u])):
                v=self._side[u][i]
                w=self._value[u][i]
                #松弛操作
                if self._cmp(w+self._ans[u],self._ans[v]):
                    self._ans[v]=w+self._ans[u]

                    #更新后节点放入堆中，堆中可能有多个该节点，但是value不一样
                    nod=node(v,self._ans[v])
                    hp.push(nod)#此句话时间复杂度O（logn）
            
    def clear(self):
        n=self._n
        self._side=[[] for i in range(n)]
        self._value=[[] for i in range(n)]
        self._ans=[]

    def get_ans(self,end:int):
        end-=1
        return self._ans[end]