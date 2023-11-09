;; Auto-generated. Do not edit!


(when (boundp 'hw0::twist)
  (if (not (find-package "HW0"))
    (make-package "HW0"))
  (shadow 'twist (find-package "HW0")))
(unless (find-package "HW0::TWIST")
  (make-package "HW0::TWIST"))

(in-package "ROS")
;;//! \htmlinclude twist.msg.html


(defclass hw0::twist
  :super ros::object
  :slots (_degree _clockwise ))

(defmethod hw0::twist
  (:init
   (&key
    ((:degree __degree) 0)
    ((:clockwise __clockwise) nil)
    )
   (send-super :init)
   (setq _degree (round __degree))
   (setq _clockwise __clockwise)
   self)
  (:degree
   (&optional __degree)
   (if __degree (setq _degree __degree)) _degree)
  (:clockwise
   (&optional (__clockwise :null))
   (if (not (eq __clockwise :null)) (setq _clockwise __clockwise)) _clockwise)
  (:serialization-length
   ()
   (+
    ;; int64 _degree
    8
    ;; bool _clockwise
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _degree
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _degree (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _degree) (= (length (_degree . bv)) 2)) ;; bignum
              (write-long (ash (elt (_degree . bv) 0) 0) s)
              (write-long (ash (elt (_degree . bv) 1) -1) s))
             ((and (class _degree) (= (length (_degree . bv)) 1)) ;; big1
              (write-long (elt (_degree . bv) 0) s)
              (write-long (if (>= _degree 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _degree s)(write-long (if (>= _degree 0) 0 #xffffffff) s)))
     ;; bool _clockwise
       (if _clockwise (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _degree
#+(or :alpha :irix6 :x86_64)
      (setf _degree (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _degree (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; bool _clockwise
     (setq _clockwise (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get hw0::twist :md5sum-) "128437c3d8b8934f35d831c72604701b")
(setf (get hw0::twist :datatype-) "hw0/twist")
(setf (get hw0::twist :definition-)
      "int64 degree
bool clockwise
")



(provide :hw0/twist "128437c3d8b8934f35d831c72604701b")


