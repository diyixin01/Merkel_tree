import hashlib
from typing import List,Tuple
from RBytes import RBytes

PADDING_HASH = b'0'*20

def find_closest_power_of_2(number:int):
    power = 0
    x = 1
    while x <= number:
        power += 1
        x = x << 1

    return power

class MerkleTree:
    def __init__(self):
        self.list_representation = []
        self.objects:dict = {}
        self.depth = 0

    def __get_node_by_index(self,index:int):
        return self.list_representation[index]

    def __calculate_parents_hash(self,index:int):
        left_child = (index*2)+1
        if left_child >= len(self.list_representation):
            return None
        right_child = (index*2)+2
        if right_child >= len(self.list_representation):
            return None
        hash_input = bytes(RBytes(self.__get_node_by_index(left_child))&\
                            RBytes(self.__get_node_by_index(right_child)))
        return hashlib.sha256(hash_input).digest()

    def __populate_tree(self,right_node:int,right_branch=True):
        
        if right_node <= 0 or\
            self.list_representation[0] != None:
            return

        parent_index = (right_node-2)//2

        self.list_representation[parent_index] =\
            self.__calculate_parents_hash(parent_index)
        self.__populate_tree(right_node-2,not right_branch)
        
        if right_branch:
            self.__populate_tree(parent_index) 
      
    def __str__(self):
        return str(self.list_representation)

    def add_objects(self,input:List[bytes]) -> bool:
        if len(self.objects) > 0:
            # check if tree was already innited if yes, return False,
            # because that tree is immutable
            return False
      
        
        input_copy = input.copy()
        
        self.depth = find_closest_power_of_2(len(input_copy))
        if len(input_copy)%2 != 0:        
            for i in range(len(input),2**self.depth):
                input_copy.append(PADDING_HASH)
            self.depth = find_closest_power_of_2(len(input_copy))


        amount_of_nodes = (2**self.depth) - 1
        self.list_representation = [None]*(amount_of_nodes-len(input_copy))
        for inp in input_copy:
            to_append = None
            if isinstance(inp,bytes):
                to_append = hashlib.sha256(inp).digest()
            else:
                to_append = hashlib.sha256(bytes(inp,'ascii')).digest()
                try:
                    self.objects[to_append]
                    raise Exception('Object: '+str(to_append)+\
                                        'already exists')
                except KeyError:
                    self.objects[to_append] = len(self.list_representation)
            self.list_representation.append(to_append)

        self.__populate_tree(len(self.list_representation)-1)
        
        return True
    
    def __check_node(self, index:int) -> bool:
        return self.__get_node_by_index(index) == \
            self.__calculate_parents_hash(index)


    def get_proof(self,data:bytes) -> List[bytes]:
        starting_node = self.objects[data]

        to_return = []
        while starting_node != 0:
            if starting_node%2 == 0:
                to_return.append(self.list_representation[starting_node-1])
                starting_node = (starting_node-2)//2
            else:
                to_return.append(self.list_representation[starting_node+1])
                starting_node = (starting_node-1)//2
        return to_return

    def get_root(self) -> bytes:
        return self.list_representation[0]

    
def verify_proof(data:bytes,root:bytes,proof:List[bytes]) -> bool:
    calculated_root = hashlib.sha256(bytes(RBytes(data)&RBytes(proof[0]))).digest()

    for pr in proof[1:]:
        calculated_root = hashlib.sha256(bytes(RBytes(pr)&RBytes(calculated_root))).digest()

    return calculated_root == root



if __name__ == '__main__':
    tree = MerkleTree()
    tree.add_objects(['562','445','4895','asdf','s5cs'])
    print(tree)
    proof = tree.get_proof(hashlib.sha256(b'123').digest())
    verify_proof(hashlib.sha256(b'123').digest(),
                 tree.get_root(),
                 proof)
    input('Ended')
