# Merkel_tree
实现merkel树


    Merkle trees是区块链的基本组成部分。虽说从理论上来讲，没有Merkel tree区块链当然也是可能的，只需创建直接包含每一笔交易的巨大区块头（block header）就可以实现，但这样做无疑会带来可扩展性方面的挑战，从长远发展来看，可能最后将只有那些具有强大算力的计算机，才可以运行这些无需受信的区块链。 正是因为有了Merkel tree，以太坊节点才可以建立运行在所有的计算机、笔记本、智能手机，甚至是那些由Slock.it生产的物联网设备之上。
    Merkle trees的主要作用是快速归纳和校验区块数据的存在性和完整性。一般意义上来讲，它是哈希大量聚集数据“块”的一种方式，它依赖于将这些数据“块”分裂成较小单位的数据块，每一个bucket块仅包含几个数据“块”，然后取每个bucket单位数据块再次进行哈希，重复同样的过程，直至剩余的哈希总数仅变为1。
    
    
    Merkle树看起来非常像二叉树，其叶子节点上的值通常为数据块的哈希值，而非叶子节点上的值，所以有时候Merkle tree也表示为Hash tree，如下图所示：



![image](https://user-images.githubusercontent.com/75195549/180139360-4bda80e1-2a58-4fe3-9689-79cd79f59e0e.png)


# 基本思路
构造Merkle tree时：



（1）对data blocks分别计算哈希值（sha256等算法）；


（2）每层两两计算获得hash值


（3）直至计算至最上一层，得到proof。

proof可以用来检验数据的完整性和正确性，即一个data block的改动或缺失，就会导致proof的改变。




在此实现了C++版本
C++版本中，使用一维数组代表merkle树，数组元素为我们的自写结构体，其中包含左右子树以及父节点的引用标号、Hash值、节点深度等变量。我们依次按照此种顺序将Hash值写入对应数组元素，并设置其高度（根据每次轮回不同，节点高度应对应增加）、子树节点以及父节点等。倘若该层节点不足以两两分完，则将最后一个节点记录下来，并以它为头节点对应的树上的所有节点高度均加一，作为下一层节点进行，此处是为了符合RFC6962要求。


初始化一个二维列表用于存放我们的Merkel tree，计算树的深度和叶子节点的个数，接着计算数据哈希值并写入叶子节点；每两个子节点计算相加后的哈希值并写入父节点列表。 而对于同一层的节点可以重复调用这个function（过程），生成下一层（父节点层）Merkle树的节点；每层向上生成父节点的时候，需要讨论对于节点数为奇数的层的最后一个节点，直接写入下一层（父节点层）；节点数为偶数则正好配对完全，进行递归，完成Merkle树的生成过程；进行实验测试：输入测试数据，将整个Merkle树printf出来，相同深度的node位于同一个列表中待所有节点均被设置，Merkle树创建完毕。


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


![image](https://user-images.githubusercontent.com/75195549/181455652-b5e1a373-a57a-49d6-a25e-eee395390abd.png)



更改message信息即可创建具有10w节点的merkletree。


然后对其进行存在性测试：


结果如下：


![image](https://user-images.githubusercontent.com/75195549/181044860-7dccd6dd-dd27-4e90-a377-4e9e40060437.png)

