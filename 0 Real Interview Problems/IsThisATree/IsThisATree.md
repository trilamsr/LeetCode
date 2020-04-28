# 3. Is this a tree?

A binary tree is represented as a sequence of parent-child pairs, for example:(A,B) (A,C) (B,G) (C,H) (E,F) (B,D) (C,E)

The following is a recursive definition for the S-expression of a tree:

    S-exp(node) = ( node->val (S-exp(node->first_child))(S-exp(node->second_child))), if node != NULL = "", node == NULLwhere, first_child->val < second_child->val (first_child->val is lexicographically smaller than second_child-> val)
    
This tree can be represented in an S-expression in multiple ways.
The lexicographically smallest way of expressing it is as follows:

    (A(B(D)(G))(C(E(F))(H)))

Translate the node-pair representation into its lexicographically smallest S-expression or report any errors that do not conform to the definition of a binary tree.

The list of errors with their codes is as follows:
1. E1 More than 2 children
2. E2 Duplicate Edges
3. E3 Cycle present (node is direct descendant of more than one node)
4. E4 Multiple roots
5. E5 Any other error
    
**Function Description**
    Complete the function sExpression in the editor below. The function must return either the lexicographically lowest S-expression or the lexicographically lowest error code as a string.
    
    sExpression has the following parameter(s):
        nodes: a string of space-separated parenthetical elements, each of which contains the names of two connected nodes separated by a comma
    Constraints:
        All node names are single characters in the range ascii[A-Z]The maximum node count is 26.There is no specific order to the input (parent, child) pairs.