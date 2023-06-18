#heap最大最小堆数据结构
#每次操作实际复杂度O（logn）
#用于dijkstra算法
#基于完全二叉树，存储在列表中
class heap:
    def __init__(self,cmp) -> None:#初始化
        self._array=[0]
        self._size=0
        self._cmp=cmp
    def pop(self):#弹出堆顶
        #将最后一个节点放到第一个
        self._array[1]=self._array[self._size]
        self._array=self._array[:self._size]
        self._size-=1
        #将最后一个节点向下更新
        i=1
        while i<=self._size:
            l=i*2#左孩子节点编号
            r=i*2+1#右孩子节点编号
            if l>self._size:#左孩子不在堆中
                break
            elif r>self._size:#只有右孩子不在堆中
                if self._cmp(self._array[l],self._array[i]):
                    self._array[l],self._array[i]=self._array[i],self._array[l]
                    i=l
                else:
                    break#更新完成，退出
            else:#都在堆中
                if self._cmp(self._array[l],self._array[r]):
                    if self._cmp(self._array[l],self._array[i]):#比较自己和左孩子
                        self._array[l],self._array[i]=self._array[i],self._array[l]
                        i=l
                    else:
                        break#更新完成，退出
                else:
                    if self._cmp(self._array[r],self._array[i]):#比较自己和右孩子
                        self._array[r],self._array[i]=self._array[i],self._array[r]
                        i=l
                    else:
                        break#更新完成，退出
    def top(self):#输出堆顶
        return self._array[1]
    def push(self,new):#输入
        #放在最后一个节点
        self._array.append(new)
        self._size+=1
        #向上更新
        i=self._size
        while i>1:#到头节点就结束
            next=i//2#父亲节点
            if self._cmp(self._array[i],self._array[next]):#向上与父亲节点交换
                self._array[next],self._array[i]=self._array[i],self._array[next]
            i=next
    def size(self):
        return self._size
    def empty(self):
        return self._size==0
    # def prt(self):
    #     print(self._size)
    #     print(self._array)