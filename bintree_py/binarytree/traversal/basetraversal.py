'''

BINARY TREE BASE TRAVERSAL

Description:    Base class which help traverse through binary trees.

Author:         Thanh Trung Nguyen
                thanh.it1995 (at) gmail.com

License:        3-Clause BSD License

'''


#
#
class BaseTraversal:
    def traverse(self, root, order: str) -> list:
        '''
        Traverses a tree entirely.
        Args:
            order: Type of traversal order.
                - 'pre': pre-order
                - 'in': in-order
                - 'post': post-order
        Returns:
            A list of keys.
        '''
        raise NotImplementedError()
