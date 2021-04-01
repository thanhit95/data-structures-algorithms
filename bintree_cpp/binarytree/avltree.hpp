#ifndef __AVL_TREE_HPP__
#define __AVL_TREE_HPP__


#include "avlnode.hpp"
#include "bst.hpp"
#include "global.hpp"



namespace my
{
namespace bt
{



template < typename TKey, typename TNode=AvlNode<TKey> >
class AvlTree : public BinarySearchTree<TKey, TNode>
{
////////////////////////////////////////////////////////
//                       FIELDS
////////////////////////////////////////////////////////



////////////////////////////////////////////////////////
//                       METHOHDS
////////////////////////////////////////////////////////
public:
    AvlTree(CandidateRemoval canddRemoval = CandidateRemoval::RIGHT)
        : BinarySearchTree<TKey, TNode>(canddRemoval)
    {

    }



    virtual ~AvlTree() {  }



protected:
    virtual TNode* __insert(TNode *node, const TKey &key) override
    {
        if (nullptr == node)
        {
            this->_count += 1;
            return new TNode(key);
        }

        if (key < node->key)
            node->left = __insert(node->left, key);
        else if (key > node->key)
            node->right = __insert(node->right, key);

        node = adjustBalance(node);
        return node;
    }



    virtual TNode* __remove(TNode *node, const TKey &key) override
    {
        if (nullptr == node)
            return nullptr;

        if (key < node->key)
            node->left = __remove(node->left, key);
        else if (key > node->key)
            node->right = __remove(node->right, key);
        else
        {
            if (nullptr == node->left)
                return node->right;

            if (nullptr == node->right)
                return node->left;

            this->removeCandidate(node);
        }

        node = adjustBalance(node);
        return node;
    }



    virtual TNode* adjustBalance(TNode *node)
    {
        // STEP 1. Updates the height of the node
        node->updateHeight();

        // STEP 2. Gets the balance factor
        int balance = node->balance();
        int balanceLe = node->balanceLeft();
        int balanceRi = node->balanceRight();

        // STEP 3. Processes if the node is unbalanced ==> 4 cases

        // Case 1: left-left
        if (  balance > 1 && balanceLe >= 0  )
            return rotateRight(node);

        // Case 2: right-right
        if (  balance < -1 && balanceRi <= 0  )
            return rotateLeft(node);

        // Case 3: left-right
        if (  balance > 1 && balanceLe < 0  )
        {
            node->left = rotateLeft(node->left);
            return rotateRight(node);
        }

        // Case 4: right-left
        if (  balance < -1 && balanceRi > 0  )
        {
            node->right = rotateRight(node->right);
            return rotateLeft(node);
        }

        return node;
    }



protected:
    TNode* rotateLeft(TNode *node)
    {
        /*
            node
            /  \
           ..   V
               / \
              a   b
        */

        TNode *V = node->right;
        TNode *a = V->left;

        V->left = node;
        node->right = a;

        node->updateHeight();
        V->updateHeight();

        return V;
    }



    TNode* rotateRight(TNode *node)
    {
        /*
            node
            /  \
           V   ..
          / \
         a   b
        */

        TNode *V = node->left;
        TNode *b = V->right;

        V->right = node;
        node->left = b;

        node->updateHeight();
        V->updateHeight();

        return V;
    }
};



} // bt
} // my



#endif // __AVL_TREE_HPP__
