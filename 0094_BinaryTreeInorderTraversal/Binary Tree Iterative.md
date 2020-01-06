def populate_leftspine(spine, node):
    while node:
        spine.append(node)
        node = node.left
        
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ret = []
        spine, node = [], root
        while spine or node:
            # populate the left spine of the tree  with respect to current 'root'
            populate_leftspine(spine, node)
      
            # we are now at the bottom of the leftspine
            # we are now ready to climb back up
            node = spine.pop()
            ret.append(node.val)
            
            # if there is a right-subtree,
            # we take a detour and solve that
            # then we resume to climb back up our current spine
            # after that subproblem is solved
            node = node.right
                        
        return ret


    
# Corollary:
# since you are processing leftspines in the binary search tree...
# starting from the bottom (of the left spine), 
# whenever youre popping elements, you will always get the sorted form

# so everytime you're working on new set of leftspines:
# you're getting that chunk and adding top of whatever you already have:
'''
[left-spine of the system]:

        / <- [root]
       /
      /
     / 
    / [top-of-stack + popped] <-- 
      has a right subtree with a left-spine:
      (see: ->)
                         /
                        /
                       /



> append entire [left-spine] to what we have:                 
        /
       / 
      /       +     /
     /             /
                  /  [left-spine-of-right-subtree]
                   
= 
  [concatenated version of left-spine]

         / <- [root]
        / 
       /   
      /
     +  <- [this is missing since we popped]
    /
   /
  / <-[top of stack,
      min elt of left-spine(right subtree),
      bottom of spine] 


[left-spine of the system (updated)]

        / <- [root]
       / 
      /   
     /
    /
   /
  / <-[top of stack] / [min elt of left-spine(right subtree)] 


imagine you cleared all of this leftspine,
    root has a right subtree ->
    rebuild the leftspine with respect to that
        right subtree of the root
    - climb back up that original left spine

[left-spine of the system]

       / <- [right of original root]
      /   
     /
    /
   / <- [top of stack, bottom of spine]
                             

###############################################################