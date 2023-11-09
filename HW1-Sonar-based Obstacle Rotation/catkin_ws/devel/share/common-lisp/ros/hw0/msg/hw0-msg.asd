
(cl:in-package :asdf)

(defsystem "hw0-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "proximity" :depends-on ("_package_proximity"))
    (:file "_package_proximity" :depends-on ("_package"))
    (:file "twist" :depends-on ("_package_twist"))
    (:file "_package_twist" :depends-on ("_package"))
  ))