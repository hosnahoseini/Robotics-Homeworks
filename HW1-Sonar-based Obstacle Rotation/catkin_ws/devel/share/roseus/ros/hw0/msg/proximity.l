;; Auto-generated. Do not edit!


(when (boundp 'hw0::proximity)
  (if (not (find-package "HW0"))
    (make-package "HW0"))
  (shadow 'proximity (find-package "HW0")))
(unless (find-package "HW0::PROXIMITY")
  (make-package "HW0::PROXIMITY"))

(in-package "ROS")
;;//! \htmlinclude proximity.msg.html


(defclass hw0::proximity
  :super ros::object
  :slots (_up _down _left _right ))

(defmethod hw0::proximity
  (:init
   (&key
    ((:up __up) 0)
    ((:down __down) 0)
    ((:left __left) 0)
    ((:right __right) 0)
    )
   (send-super :init)
   (setq _up (round __up))
   (setq _down (round __down))
   (setq _left (round __left))
   (setq _right (round __right))
   self)
  (:up
   (&optional __up)
   (if __up (setq _up __up)) _up)
  (:down
   (&optional __down)
   (if __down (setq _down __down)) _down)
  (:left
   (&optional __left)
   (if __left (setq _left __left)) _left)
  (:right
   (&optional __right)
   (if __right (setq _right __right)) _right)
  (:serialization-length
   ()
   (+
    ;; int64 _up
    8
    ;; int64 _down
    8
    ;; int64 _left
    8
    ;; int64 _right
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _up
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _up (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _up) (= (length (_up . bv)) 2)) ;; bignum
              (write-long (ash (elt (_up . bv) 0) 0) s)
              (write-long (ash (elt (_up . bv) 1) -1) s))
             ((and (class _up) (= (length (_up . bv)) 1)) ;; big1
              (write-long (elt (_up . bv) 0) s)
              (write-long (if (>= _up 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _up s)(write-long (if (>= _up 0) 0 #xffffffff) s)))
     ;; int64 _down
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _down (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _down) (= (length (_down . bv)) 2)) ;; bignum
              (write-long (ash (elt (_down . bv) 0) 0) s)
              (write-long (ash (elt (_down . bv) 1) -1) s))
             ((and (class _down) (= (length (_down . bv)) 1)) ;; big1
              (write-long (elt (_down . bv) 0) s)
              (write-long (if (>= _down 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _down s)(write-long (if (>= _down 0) 0 #xffffffff) s)))
     ;; int64 _left
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _left (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _left) (= (length (_left . bv)) 2)) ;; bignum
              (write-long (ash (elt (_left . bv) 0) 0) s)
              (write-long (ash (elt (_left . bv) 1) -1) s))
             ((and (class _left) (= (length (_left . bv)) 1)) ;; big1
              (write-long (elt (_left . bv) 0) s)
              (write-long (if (>= _left 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _left s)(write-long (if (>= _left 0) 0 #xffffffff) s)))
     ;; int64 _right
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _right (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _right) (= (length (_right . bv)) 2)) ;; bignum
              (write-long (ash (elt (_right . bv) 0) 0) s)
              (write-long (ash (elt (_right . bv) 1) -1) s))
             ((and (class _right) (= (length (_right . bv)) 1)) ;; big1
              (write-long (elt (_right . bv) 0) s)
              (write-long (if (>= _right 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _right s)(write-long (if (>= _right 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _up
#+(or :alpha :irix6 :x86_64)
      (setf _up (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _up (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _down
#+(or :alpha :irix6 :x86_64)
      (setf _down (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _down (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _left
#+(or :alpha :irix6 :x86_64)
      (setf _left (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _left (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _right
#+(or :alpha :irix6 :x86_64)
      (setf _right (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _right (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(setf (get hw0::proximity :md5sum-) "7e422bbe29fec8ddaffc447bd5b0585b")
(setf (get hw0::proximity :datatype-) "hw0/proximity")
(setf (get hw0::proximity :definition-)
      "int64 up
int64 down
int64 left
int64 right
")



(provide :hw0/proximity "7e422bbe29fec8ddaffc447bd5b0585b")


