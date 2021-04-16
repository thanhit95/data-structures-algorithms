#ifndef __AVL_TREE_HPP__
#define __AVL_TREE_HPP__


#include "avlnode.hpp"
#include "binsearchtree.hpp"
#include "candidateremoval.hpp"



namespace my
{
namespace bt
{



template < typename TKey, typename TNode=AvlNode<TKey> >
class AvlTree : public BinSearchTree<TKey, TNode>
{

//////////////////////////////////////////////////////////////
//                        FIELDS
//////////////////////////////////////////////////////////////



//////////////////////////////////////////////////////////////
//                        CONSTRUCTORS
//////////////////////////////////////////////////////////////



public:
    virtual ~AvlTree() { }



    AvlTree(CandidateRemoval canddRM = CandidateRemoval::RIGHT):
        BinSearchTree<TKey, TNode>(canddRM)
    {
    }



    AvlTree(const std::vector<TKey> &lst):
        BinSearchTree<TKey, TNode>(lst)
    {
    }



    AvlTree(const std::vector<TKey> &lst, CandidateRemoval canddRM):
        BinSearchTree<TKey, TNode>(lst, canddRM)
    {
    }



//////////////////////////////////////////////////////////////
//                        METHODS (PUBLIC)
//////////////////////////////////////////////////////////////



public:
    virtual int height() const override
    {
        return (nullptr == this->root) ? 0 : this->root->height();
    }



//////////////////////////////////////////////////////////////
//                        METHODS (PROTECTED)
//////////////////////////////////////////////////////////////



protected:
    virtual TNode* _insert(TNode *node, const TKey &key) override
    {
        if (nullptr == node)
        {
            this->successState = true;
            return new TNode(key); // return createNode(key);
        }

        if (key < node->key)
            node->left = _insert(node->left, key);
        else if (key > node->key)
            node->right = _insert(node->right, key);

        node = adjustBalance(node);
        return node;
    }



    virtual TNode* _remove(TNode *node, const TKey &key) override
    {
        if (nullptr == node)
            return nullptr;

        if (key < node->key)
            node->left = _remove(node->left, key);
        else if (key > node->key)
            node->right = _remove(node->right, key);
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
        // STEP 1. Update the height of the node
        node->updateHeight();

        // STEP 2. Get the balance factor
        int balance = node->balance();
        int balanceLe = node->balanceLeft();
        int balanceRi = node->balanceRight();

        // STEP 3. Process if the node is unbalanced ==> 4 cases

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



    // do not need to override method
    // virtual TNode* createNode(const TKey &key) const override



    virtual void buildTreeFromSortedListNodeFunc(TNode *node) override
    {
        node->updateHeight();
    }
};



} // bt
} // my



#endif // __AVL_TREE_HPP__
