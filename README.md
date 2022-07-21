# Merkel_tree
实现merkel树
Merkle树看起来非常像二叉树，其叶子节点上的值通常为数据块的哈希值，而非叶子节点上的值，所以有时候Merkle tree也表示为Hash tree，如下图所示：



![image](https://user-images.githubusercontent.com/75195549/180139360-4bda80e1-2a58-4fe3-9689-79cd79f59e0e.png)



构造Merkle tree时：



（1）对data blocks分别计算哈希值（sha256等算法）；


（2）每层两两计算获得hash值


（3）直至计算至最上一层，得到proof。

proof可以用来检验数据的完整性和正确性，即一个data block的改动或缺失，就会导致proof的改变。
