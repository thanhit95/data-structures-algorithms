#ifndef __BINARY_SEARCH_TREE_HPP__
#define __BINARY_SEARCH_TREE_HPP__


#include <tuple>
#include "binnode.hpp"
#include "bintree.hpp"
#include "public.hpp"


namespace mybt
{



template<typename T>
class BinarySearchTree : public BinTree<T>
{
////////////////////////////////////////////////////////
//                       FIELDS
////////////////////////////////////////////////////////
protected:
    int _count = 0;
    CandidateRemoval optionCanddRemoval = CandidateRemoval::RIGHT;



////////////////////////////////////////////////////////
//                       METHOHDS
////////////////////////////////////////////////////////
public:
    BinarySearchTree(CandidateRemoval canddRemoval = CandidateRemoval::RIGHT)
    {
        this->optionCanddRemoval = canddRemoval;
    }



public:
    const int count() const
    {
        return this->_count;
    }



public:
    BinNode<T> * get(T key) const
    {
        auto res = __search(this->root, key);
        return std::get<0>(res);
    }



public:
    void insert(T key)
    {
        this->root = __insert(this->root, key);
    }



protected:
    std::tuple< BinNode<T>*, BinNode<T>* > __search(BinNode<T> *node, T key) const
    {
        BinNode<T> *parent = nullptr;

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



    BinNode<T> * __insert(BinNode<T> *node, T key)
    {
        if (nullptr == node)
            return new BinNode<T>(key);

        if (key < node->key)
            node->left = __insert(node->left, key);
        else
            node->right = __insert(node->right, key);

        return node;
    }
};



} // mybt


#endif
