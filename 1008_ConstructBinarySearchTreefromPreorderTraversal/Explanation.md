
![Figure 1-1](https://www.cdn.geeksforgeeks.org/wp-content/uploads/Preorder-from-Inorder-and-Postorder-traversals.jpg "Figure 1-1")

```
the preorder traversal for this tree is:
[25, 15, 10, 4, 12, 22, 18, 24, 50, 35, 31, 44, 70, 66, 90]

consider grouping all left-spines with respect to their leader (root of that subtree)

[[25,15,10,4],[12],[22,18],[24],[50,35,31],[44],[70,66],[90]]
  ^             ^    ^       ^    ^          ^    ^       ^

now imagine that the we get a stream of nodes coming in  1 at a time

Assume we already processed [25,15,10,4]:
Now we get 12 && remaining : [22, 18, 24, 50, 35, 31, 44, 70, 66, 90]]

because [12] isnt part of the left-spine-group of [25,15,10,4],
we must keep climbing up the tree from [4] until we can construct a new-group or left-spine with [12] as the leader

-last thing we pop from the stack is [10] and start a new left-spine from [10]
1. [10].right = [12]
2. push onto the stack

instead of imagining the stack as a 'stack'
think of it as the group of left-spines
[[25,15], [12]]

now given: 22 as our data:
and since 22 > 12: we must construct a group for it
so we keep popping and our group of left spine looks like this:

[[25], [22]]

now we have [18] from our stream of data
since 18 is part of the current left-spine, namely [22],
we join [18] to part of our left-spine so our 
group of left-spines look like this:

[[25],[22,18]]

we now process [24]
[24] is its own left-spine
so our group of left-spines look like this

[[25], [24]]

```

### REMINDER ###
```
this is what the picture looks like
```

![Figure 1-1](https://www.cdn.geeksforgeeks.org/wp-content/uploads/Preorder-from-Inorder-and-Postorder-traversals.jpg "Figure 1-1")



```
This is our data
[25, 15, 10, 4, 12, 22, 18, 24, 50, 35, 31, 44, 70, 66, 90]

[[25,15,10,4],[12],[22,18],[24],[50,35,31],[44],[70,66],[90]]
||||||||||||||||||||||||||||||
^----------------------------^
all the things we've processed so far
```
```
our groups of left-spine look like this:
[[25], [24]]

now we get [50] as an incoming data
according the the picture:
[50] is its own leader so we must construct a new leftspine for it

however, its greater than the root of the tree
so after climbing up from [24] -> [25]

our group of left-spines look like this:
Popped: [24] -> [25] (via climbing back up the tree)
[[50]]

These are remaining items we must process: [35, 31, 44, 70, 66, 90]

I will make this short now.
[35, 31] are part of the group of left spine of 50
so we concatenate taht and our group of left-spines will look like this:

[[50,35, 31]]

however, 44 its its own left-spine and greater than 35 so we must construct
a new left-spine for that

as a result, it will look like this:

[[50],[44]], remaining: [70, 66, 90]

[70] requires its own left-spine

so we need to keep climbing up the tree until we can do so
as a result:

group of left-spines:
[[70]]

66 is part of left-spine of 70:

[[70, 66]]

[90] is its own new leader:
so keep climbing back up and add to group of left-spines

[[90]]

we are done now


```