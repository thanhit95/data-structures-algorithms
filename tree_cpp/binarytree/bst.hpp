#ifndef __BINARY_SEARCH_TREE_HPP__
#define __BINARY_SEARCH_TREE_HPP__


#include <tuple>
#include "binnode.hpp"
#include "bintree.hpp"
#include "global.hpp"

// #define NDEBUG // disable assertion
#include <cassert>


namespace mybt
{



template <typename T>
class BinarySearchTree : public BinTree<T>
{
////////////////////////////////////////////////////////
//                       FIELDS
////////////////////////////////////////////////////////
protected:
    int _count = 0;
    CandidateRemoval _optionCanddRemoval = CandidateRemoval::RIGHT;



////////////////////////////////////////////////////////
//                       METHOHDS
////////////////////////////////////////////////////////
public:
    BinarySearchTree(CandidateRemoval canddRemoval = CandidateRemoval::RIGHT)
    {
        this->_optionCanddRemoval = canddRemoval;
    }


    virtual ~BinarySearchTree() { }



public:
    const int count() const
    {
        return this->_count;
    }



public:
    BinNode<T> * get(T key) const
    {
        auto res = search(this->root, key);
        return std::get<0>(res);
    }



public:
    void insert(T key)
    {
        this->root = __insert(this->root, key);
    }



public:
    bool remove(T key)
    {
        if (nullptr == this->get(key))
            return false;

        this->root = this->__remove(this->root, key);

        this->_count -= 1;
        return true;
    }



public:
    T * getMin() const
    {
        auto temp = searchMin(this->root, nullptr);

        BinNode<T> *res = std::get<0>(temp);

        if (nullptr == res)
            return nullptr;

        return &res->key;
    }



    T * getMax() const
    {
        auto temp = searchMax(this->root, nullptr);

        BinNode<T> *res = std::get<0>(temp);

        if (nullptr == res)
            return nullptr;

        return &res->key;
    }



protected:
    std::tuple< BinNode<T>*, BinNode<T>* > search(BinNode<T> *node, T key) const
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



    virtual BinNode<T> * __insert(BinNode<T> *node, T key)
    {
        if (nullptr == node)
        {
            this->_count += 1;
            return new BinNode<T>(key);
        }

        if (key < node->key)
            node->left = __insert(node->left, key);
        else
            node->right = __insert(node->right, key);

        return node;
    }



    virtual BinNode<T> * __remove(BinNode<T> *node, T key)
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

            removeCandidate(node);
        }

        return node;
    }



    void removeCandidate(BinNode<T> *node)
    {
        assert(nullptr != node);

        BinNode<T> *candidate = nullptr;

        switch (this->_optionCanddRemoval)
        {
        case CandidateRemoval::RIGHT :
            candidate = std::get<0>( searchMin(node->right, node) );
            node->key = candidate->key;
            node->right = this->__remove(node->right, candidate->key);
            break;

        case CandidateRemoval::LEFT :
            candidate = std::get<0>( searchMax(node->left, node) );
            node->key = candidate->key;
            node->left = this->__remove(node->left, candidate->key);
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



    std::tuple< BinNode<T>*, BinNode<T>* >
    searchMin(BinNode<T> *node, BinNode<T> *parent) const
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



    std::tuple< BinNode<T>*, BinNode<T>* >
    searchMax(BinNode<T> *node, BinNode<T> *parent) const
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
};



} // mybt


#endif
