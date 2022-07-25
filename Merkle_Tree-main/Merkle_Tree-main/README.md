# 实验名称
Impl Merkle Tree following RFC6962

# 实验完成人
权周雨 

学号：202000460021 

git账户名称：baekhunee

# 代码部分说明
new_node为用于创建新节点的宏函数；

void print_tree(merkletree* tree, int height)用于打印出生成的Merkletree；

uint hash(char* s1, char* s2)用于计算单个节点的哈希值；

uint hash_nodes(uint n1, uint n2)用于计算由两个旧节点生成的新节点的哈希值；

merkletree* last_node(merkletree* tree)用于寻找当前merkletree中最后一个节点；

merkletree* find_new_node(merkletree* tree)用于寻找可插入的新节点；

merkletree* initial(merkletree* tree, char** s, int n)生成merkletree，倘若该层节点不足以两两分完，则将最后一个节点记录下来，并以它为头节点对应的树上的所有节点高度均加一作为下一层节点进行，以符合RFC6962要求。

void delete_tree(merkletree* tree)删除merkletree；

char** divide_string(char* str, int* number)merkletree支持字符串的存储，且以标点符号为分割；

void delete_string(char** s, int n)删除字符串；

# 运行测试
  给定message="Hello!This is Baekhunee.I'm writing a merkle tree!"
  
![image](https://user-images.githubusercontent.com/105578152/180704750-71d4623f-0b29-454f-87a2-13eafeda8517.png)
  发现可以成功生成merkletree，与之类似更改message信息即可创建具有10w节点的merkletree。

