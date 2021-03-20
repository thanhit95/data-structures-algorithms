#ifndef __PUBLIC_STUFF_HPP__
#define __PUBLIC_STUFF_HPP__


namespace mybt
{



#define max(a,b) ((a) > (b) ? (a) : (b))
#define min(a,b) ((a) < (b) ? (a) : (b))



enum class TraverseOrder
{
    PRE,
    IN,
    POST
};



enum class CandidateRemoval
{
    LEFT,
    RIGHT
};



} // mybt


#endif
