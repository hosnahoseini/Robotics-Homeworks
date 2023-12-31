// Generated by gencpp from file hw0/twist.msg
// DO NOT EDIT!


#ifndef HW0_MESSAGE_TWIST_H
#define HW0_MESSAGE_TWIST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace hw0
{
template <class ContainerAllocator>
struct twist_
{
  typedef twist_<ContainerAllocator> Type;

  twist_()
    : degree(0)
    , clockwise(false)  {
    }
  twist_(const ContainerAllocator& _alloc)
    : degree(0)
    , clockwise(false)  {
  (void)_alloc;
    }



   typedef int64_t _degree_type;
  _degree_type degree;

   typedef uint8_t _clockwise_type;
  _clockwise_type clockwise;





  typedef boost::shared_ptr< ::hw0::twist_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::hw0::twist_<ContainerAllocator> const> ConstPtr;

}; // struct twist_

typedef ::hw0::twist_<std::allocator<void> > twist;

typedef boost::shared_ptr< ::hw0::twist > twistPtr;
typedef boost::shared_ptr< ::hw0::twist const> twistConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::hw0::twist_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::hw0::twist_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::hw0::twist_<ContainerAllocator1> & lhs, const ::hw0::twist_<ContainerAllocator2> & rhs)
{
  return lhs.degree == rhs.degree &&
    lhs.clockwise == rhs.clockwise;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::hw0::twist_<ContainerAllocator1> & lhs, const ::hw0::twist_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace hw0

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::hw0::twist_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::hw0::twist_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::hw0::twist_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::hw0::twist_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::hw0::twist_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::hw0::twist_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::hw0::twist_<ContainerAllocator> >
{
  static const char* value()
  {
    return "128437c3d8b8934f35d831c72604701b";
  }

  static const char* value(const ::hw0::twist_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x128437c3d8b8934fULL;
  static const uint64_t static_value2 = 0x35d831c72604701bULL;
};

template<class ContainerAllocator>
struct DataType< ::hw0::twist_<ContainerAllocator> >
{
  static const char* value()
  {
    return "hw0/twist";
  }

  static const char* value(const ::hw0::twist_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::hw0::twist_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int64 degree\n"
"bool clockwise\n"
;
  }

  static const char* value(const ::hw0::twist_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::hw0::twist_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.degree);
      stream.next(m.clockwise);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct twist_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::hw0::twist_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::hw0::twist_<ContainerAllocator>& v)
  {
    s << indent << "degree: ";
    Printer<int64_t>::stream(s, indent + "  ", v.degree);
    s << indent << "clockwise: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.clockwise);
  }
};

} // namespace message_operations
} // namespace ros

#endif // HW0_MESSAGE_TWIST_H
