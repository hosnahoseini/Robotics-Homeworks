; Auto-generated. Do not edit!


(cl:in-package hw0-msg)


;//! \htmlinclude twist.msg.html

(cl:defclass <twist> (roslisp-msg-protocol:ros-message)
  ((degree
    :reader degree
    :initarg :degree
    :type cl:integer
    :initform 0)
   (clockwise
    :reader clockwise
    :initarg :clockwise
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass twist (<twist>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <twist>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'twist)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name hw0-msg:<twist> is deprecated: use hw0-msg:twist instead.")))

(cl:ensure-generic-function 'degree-val :lambda-list '(m))
(cl:defmethod degree-val ((m <twist>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hw0-msg:degree-val is deprecated.  Use hw0-msg:degree instead.")
  (degree m))

(cl:ensure-generic-function 'clockwise-val :lambda-list '(m))
(cl:defmethod clockwise-val ((m <twist>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hw0-msg:clockwise-val is deprecated.  Use hw0-msg:clockwise instead.")
  (clockwise m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <twist>) ostream)
  "Serializes a message object of type '<twist>"
  (cl:let* ((signed (cl:slot-value msg 'degree)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'clockwise) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <twist>) istream)
  "Deserializes a message object of type '<twist>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'degree) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
    (cl:setf (cl:slot-value msg 'clockwise) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<twist>)))
  "Returns string type for a message object of type '<twist>"
  "hw0/twist")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'twist)))
  "Returns string type for a message object of type 'twist"
  "hw0/twist")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<twist>)))
  "Returns md5sum for a message object of type '<twist>"
  "128437c3d8b8934f35d831c72604701b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'twist)))
  "Returns md5sum for a message object of type 'twist"
  "128437c3d8b8934f35d831c72604701b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<twist>)))
  "Returns full string definition for message of type '<twist>"
  (cl:format cl:nil "int64 degree~%bool clockwise~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'twist)))
  "Returns full string definition for message of type 'twist"
  (cl:format cl:nil "int64 degree~%bool clockwise~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <twist>))
  (cl:+ 0
     8
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <twist>))
  "Converts a ROS message object to a list"
  (cl:list 'twist
    (cl:cons ':degree (degree msg))
    (cl:cons ':clockwise (clockwise msg))
))
