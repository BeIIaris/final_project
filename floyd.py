#floyd算法，多源最短路
#时间复杂度O（n^3）
#无法处理负环问题
import copy
class floyd:
    #初始化
    def __init__(self,n:int) -> None:
        self._side=[['None' for i in range(n)] for j in range(n)]#邻接矩阵，适合稠密图，floyd只能用这个
        self._n=n#节点数

        def cmp(x1,x2):#比较函数
            if x1=='None':
                return False
            if x2=='None':
                return True
            return x1<x2
        self._cmp=cmp

    def push_oneway_side(self,u:int,v:int,w):#放入单向边
        u-=1
        v-=1
        if self._cmp(w,self._side[u][v]):
            self._side[u][v]=w

    def push_side(self,u:int,v:int,w):#放入双向边
        self.push_oneway_side(u,v,w)
        self.push_oneway_side(v,u,w)

    def calculate(self):#计算结果
        self._ans=copy.deepcopy(self._side)
        n=self._n

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    #有边不存在就退出
                    if self._ans[i][k]=='None' or self._ans[k][j]=='None':
                        continue
                    #松弛操作，操作数n^3
                    w=self._ans[i][k]+self._ans[k][j]
                    if self._cmp(w,self._ans[i][j]):
                        self._ans[i][j]=w

    def get_ans(self,u:int,v:int):
        u-=1
        v-=1
        return self._ans[u][v]
    
    def clear(self):
        n=self._n
        self._side=[['None' for i in range(n)] for j in range(n)]
        self._ans=[]
