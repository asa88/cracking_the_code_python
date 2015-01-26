''' Given a Binary Search tree, convert it to max heap'''

'''Sol: use reverse inOrder travrsal to get the tree element in descending order,
	the array is a max-heap story in array data structure.

	max_heap: if a node is stored at index k , its left child is at index 2k+1
		  and right child at index 2k+2.
''' 
