; Auto-generated. Do not edit!


(cl:in-package hw0-msg)


;//! \htmlinclude proximity.msg.html

(cl:defclass <proximity> (roslisp-msg-protocol:ros-message)
  ((up
    :reader up
    :initarg :up
    :type cl:integer
    :initform 0)
   (down
    :reader down
    :initarg :down
    :type cl:integer
    :initform 0)
   (left
    :reader left
    :initarg :left
    :type cl:integer
    :initform 0)
   (right
    :reader right
    :initarg :right
    :type cl:integer
    :initform 0))
)

(cl:defclass proximity (<proximity>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <proximity>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'proximity)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name hw0-msg:<proximity> is deprecated: use hw0-msg:proximity instead.")))

(cl:ensure-generic-function 'up-val :lambda-list '(m))
(cl:defmethod up-val ((m <proximity>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hw0-msg:up-val is deprecated.  Use hw0-msg:up instead.")
  (up m))

(cl:ensure-generic-function 'down-val :lambda-list '(m))
(cl:defmethod down-val ((m <proximity>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hw0-msg:down-val is deprecated.  Use hw0-msg:down instead.")
  (down m))

(cl:ensure-generic-function 'left-val :lambda-list '(m))
(cl:defmethod left-val ((m <proximity>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hw0-msg:left-val is deprecated.  Use hw0-msg:left instead.")
  (left m))

(cl:ensure-generic-function 'right-val :lambda-list '(m))
(cl:defmethod right-val ((m <proximity>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hw0-msg:right-val is deprecated.  Use hw0-msg:right instead.")
  (right m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <proximity>) ostream)
  "Serializes a message object of type '<proximity>"
  (cl:let* ((signed (cl:slot-value msg 'up)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'down)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'left)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'right)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <proximity>) istream)
  "Deserializes a message object of type '<proximity>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'up) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'down) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'left) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'right) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<proximity>)))
  "Returns string type for a message object of type '<proximity>"
  "hw0/proximity")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'proximity)))
  "Returns string type for a message object of type 'proximity"
  "hw0/proximity")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<proximity>)))
  "Returns md5sum for a message object of type '<proximity>"
  "7e422bbe29fec8ddaffc447bd5b0585b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'proximity)))
  "Returns md5sum for a message object of type 'proximity"
  "7e422bbe29fec8ddaffc447bd5b0585b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<proximity>)))
  "Returns full string definition for message of type '<proximity>"
  (cl:format cl:nil "int64 up~%int64 down~%int64 left~%int64 right~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'proximity)))
  "Returns full string definition for message of type 'proximity"
  (cl:format cl:nil "int64 up~%int64 down~%int64 left~%int64 right~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <proximity>))
  (cl:+ 0
     8
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <proximity>))
  "Converts a ROS message object to a list"
  (cl:list 'proximity
    (cl:cons ':up (up msg))
    (cl:cons ':down (down msg))
    (cl:cons ':left (left msg))
    (cl:cons ':right (right msg))
))
