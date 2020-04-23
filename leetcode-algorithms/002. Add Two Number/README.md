# 001 add_two_number  
## 思路

1. 建立一个任意链表节点 result指向此节点 curr当前指针也指向此节点 result作为变量 保存头指针
```
    result
        |
    LinkNode(0)->None
        |
        curr
```
2. p q 为两个加法运算数字 头指针  inc进位初始=0
```
    p->l1
    q->l2
```
3. 当p or q未指向None时（p q之一有值 未遍历完）
```
    x=p.val if p else 0
    x=y.val if q else 0
   inc,re= divmod(x+y+inc,10)
```
   余数 re 应当插入链表的尾部,然后当前指针指向插入的余数
```
   curr.next=ListNode(re)
   curr=curr.next
   if(p)
        p=p.next
   if(q)
        q=q.next
   
   result
        |
        ListNode(0)->ListNode(re)->None
                            |
                            curr
```
4. 循环3步骤 不断插入加法后的余数，进位参与下一位的加法运算 直到p q遍历到None 退出3步骤
5. 最后检查进位inc 如果inc！=0, 链表尾部再插入ListNode(inc)
```
   result
        |
        ListNode(0)->ListNode(re)->...ListNode(re)->ListNode(inc)->None
                                           |
                                           curr
```
6. 返回的应当是result->next 节点
    return result.next 
    由此指针遍历最终结果

   
    