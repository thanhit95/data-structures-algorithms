#ifndef __BIN_SEARCH_TREE_HPP__
#define __BIN_SEARCH_TREE_HPP__


#include <algorithm>
#include <tuple>
#include <cassert>
#include "binnode.hpp"
#include "bintree.hpp"
#include "candidateremoval.hpp"



#ifdef min
#undef min
#endif

#ifdef max
#undef max
#endif



namespace my
{
namespace bt
{



template < typename TKey, typename TNode=BinNode<TKey> >
class BinSearchTree : public BinTree<TKey, TNode>
{

//////////////////////////////////////////////////////////////
//                        FIELDS
//////////////////////////////////////////////////////////////



protected:
    int _count = 0;
    CandidateRemoval optionCanddRM = CandidateRemoval::RIGHT;
    bool successState = false;



//////////////////////////////////////////////////////////////
//                        CONSTRUCTORS
//////////////////////////////////////////////////////////////



public:
    virtual ~BinSearchTree() { }



    BinSearchTree(CandidateRemoval canddRM = CandidateRemoval::RIGHT):
        BinTree<TKey, TNode>()
    {
        this->optionCanddRM = canddRM;
    }



    BinSearchTree(const std::vector<TKey> &lst): BinTree<TKey, TNode>()
    {
        constructFromList(lst);
    }



    BinSearchTree(const std::vector<TKey> &lst, CandidateRemoval canddRM):
        BinTree<TKey, TNode>()
    {
        constructFromList(lst);
        this->optionCanddRM = canddRM;
    }



//////////////////////////////////////////////////////////////
//                        METHODS (PUBLIC)
//////////////////////////////////////////////////////////////



public:
    int count() const
    {
        return this->_count;
    }



    bool contain(const TKey &key) const
    {
        auto temp = search(this->root, key);
        TNode *node = std::get<0>(temp);
        return (nullptr != node);
    }



    bool insert(const TKey &key)
    {
        this->successState = false;

        this->root = _insert(this->root, key);

        if (false == this->successState) {
            return false;
        }

        this->_count += 1;
        return true;
    }



    bool remove(const TKey &key)
    {
        if (nullptr == this->root)
            return false;

        if (false == contain(key))
            return false;

        this->root = _remove(this->root, key);

        this->_count -= 1;
        return true;
    }



    TKey min() const
    {
        if (this->empty())
            throw std::logic_error("Tree is empty");

        auto temp = searchMin(this->root, nullptr);
        TNode *res = std::get<0>(temp);

        return res->key;
    }



    TKey max() const
    {
        if (this->empty())
            throw std::logic_error("Tree is empty");

        auto temp = searchMax(this->root, nullptr);
        TNode *res = std::get<0>(temp);

        return res->key;
    }



//////////////////////////////////////////////////////////////
//                        METHODS (PROTECTED)
//////////////////////////////////////////////////////////////



protected:
    virtual TNode* _insert(TNode *node, const TKey &key)
    {
        if (nullptr == node)
        {
            this->_count += 1;
            return this->createNode(key);
        }

        if (key < node->key)
        {
            node->left = _insert(node->left, key);
        }
        else if (key > node->key)
        {
            node->right = _insert(node->right, key);
        }

        return node;
    }



    virtual TNode* _remove(TNode *node, const TKey &key)
    {
        if (nullptr == node)
            return nullptr;

        if (key < node->key)
        {
            node->left = _remove(node->left, key);
        }
        else if (key > node->key)
        {
            node->right = _remove(node->right, key);
        }
        else
        {
            if (nullptr == node->left)
                return node->right;

            if (nullptr == node->right)
                return node->left;

            removeCandidate(node);
        }

        return node;
    }



    void removeCandidate(TNode *node)
    {
        assert(nullptr != node);

        TNode *candidate = nullptr;

        switch (this->optionCanddRM)
        {
        case CandidateRemoval::RIGHT :
            candidate = std::get<0>( searchMin(node->right, node) );
            node->key = candidate->key;
            node->right = this->_remove(node->right, candidate->key);
            break;

        case CandidateRemoval::LEFT :
            candidate = std::get<0>( searchMax(node->left, node) );
            node->key = candidate->key;
            node->left = this->_remove(node->left, candidate->key);
            break;

        default:
            break;
        }

        if (nullptr != candidate)
        {
            delete candidate;
            candidate = nullptr; // avoid dangling pointer
        }
    }



    std::tuple< TNode*, TNode* >
    search(TNode *node, TKey key) const
    {
        TNode *parent = nullptr;

        while (1)
        {
            if (nullptr == node)
                return std::make_tuple(nullptr, nullptr);

            if (key == node->key)
                return std::make_tuple(node, parent);

            parent = node;

            if (key < node->key)
                node = node->left;
            else
                node = node->right;
        }

        return std::make_tuple(nullptr, nullptr);  // ensures a value to return, unreachable statement...
    }



    std::tuple< TNode*, TNode* >
    searchMin(TNode *node, TNode *parent) const
    {
        if (nullptr == node)
            return std::make_tuple(nullptr, nullptr);

        while (nullptr != node->left)
        {
            parent = node;
            node = node->left;
        }

        return std::make_tuple(node, parent);
    }



    std::tuple< TNode*, TNode* >
    searchMax(TNode *node, TNode *parent) const
    {
        if (nullptr == node)
            return std::make_tuple(nullptr, nullptr);

        while (nullptr != node->right)
        {
            parent = node;
            node = node->right;
        }

        return std::make_tuple(node, parent);
    }



    void constructFromList(std::vector<TKey> lst)
    {
        this->disposeRoot(this->root);

        std::sort(lst.begin(), lst.end());
        lst.erase(std::unique(lst.begin(), lst.end()), lst.end());

        int lenLst = lst.size();

        this->root = buildTreeFromSortedList(lst, 0, lenLst - 1);
        this->_count = lenLst;
    }



    TNode* buildTreeFromSortedList(const std::vector<TKey> &lst, int indexStart, int indexEnd)
    {
        if (indexStart > indexEnd)
            return nullptr;

        int indexMid = (indexStart + indexEnd) / 2;
        TNode *node = this->createNode(lst[indexMid]);

        node->left = buildTreeFromSortedList(lst, indexStart, indexMid - 1);
        node->right = buildTreeFromSortedList(lst, indexMid + 1, indexEnd);

        buildTreeFromSortedListNodeFunc(node);

        return node;
    }



    virtual void buildTreeFromSortedListNodeFunc(TNode *node)
    {
    }
};



} // bt
} // my



#endif // __BIN_SEARCH_TREE_HPP__
