## two sum linkedlist
### 模拟正常相加，
. 首先设立一个返回node result(0)
```
当前node curr=result
p,q 指向l1,l2
初始 进位 inc=0
p q有1个非空 进行循环
循环 (p not none or q not none)：
    if p存在,x 取p.val else x取0
    if q存在,y 取q.val else y取0
    和sum=x+y+inc
    得到的当前位余数 re 新建linkNode(re)
    将curr-next 设为 reNode
    curr指向curr-next 即余数节点
    即 将余数节点加入result链，
    if p p=p-next
    if q q=q-next
    当p q均为none 退出循环
. 此时检查进位 将进位插入到result链末尾
    curr-next=LinkNode(inc)
    得到 result链条
    因为result 链条头节点为0，
返回 result-next
```

