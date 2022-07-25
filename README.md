# Merkel_tree
实现merkel树
Merkle树看起来非常像二叉树，其叶子节点上的值通常为数据块的哈希值，而非叶子节点上的值，所以有时候Merkle tree也表示为Hash tree，如下图所示：



![image](https://user-images.githubusercontent.com/75195549/180139360-4bda80e1-2a58-4fe3-9689-79cd79f59e0e.png)


# 基本思路
构造Merkle tree时：



（1）对data blocks分别计算哈希值（sha256等算法）；


（2）每层两两计算获得hash值


（3）直至计算至最上一层，得到proof。

proof可以用来检验数据的完整性和正确性，即一个data block的改动或缺失，就会导致proof的改变。




在此实现了python版本和C++版本
C++版本中，使用一维数组代表merkle树，数组元素为我们的自写结构体，其中包含左右子树以及父节点的引用标号、Hash值、节点深度等变量。我们依次按照此种顺序将Hash值写入对应数组元素，并设置其高度（根据每次轮回不同，节点高度应对应增加）、子树节点以及父节点等。倘若该层节点不足以两两分完，则将最后一个节点记录下来，并以它为头节点对应的树上的所有节点高度均加一，作为下一层节点进行，此处是为了符合RFC6962要求。
待所有节点均被设置，Merkle树创建完毕。

# 函数解释

new_node为用于创建新节点的宏函数；


uint hash_nodes(uint n1, uint n2)用于计算由两个旧节点生成的新节点的哈希值；


void print_tree(merkletree* tree, int height)用于打印出生成的Merkletree；

uint hash(char* s1, char* s2)用于计算单个节点的哈希值；

merkletree* last_node(merkletree* tree)用于寻找当前merkletree中最后一个节点；

merkletree* find_new_node(merkletree* tree)用于寻找可插入的新节点；

merkletree* initial(merkletree* tree, char** s, int n)生成merkletree，倘若该层节点不足以两两分完，则将最后一个节点记录下来，并以它为头节点对应的树上的所有节点高度均加一作为下一层节点进行，以符合RFC6962要求。

void delete_tree(merkletree* tree)删除merkletree；

char** divide_string(char* str, int* number)merkletree支持字符串的存储，且以标点符号为分割；

void delete_string(char** s, int n)删除字符串；

# 运行测试
给定message="Liujinyuan，202000460082，male"

得到下图所示的运行结果：



![image](https://user-images.githubusercontent.com/75195549/180789550-8bd7cd42-e0c9-4f91-946f-7ec90fc7e6cd.png)






更改message信息即可创建具有10w节点的merkletree。

