// Auto-generated. Do not edit!

// (in-package hw0.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class twist {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.degree = null;
      this.clockwise = null;
    }
    else {
      if (initObj.hasOwnProperty('degree')) {
        this.degree = initObj.degree
      }
      else {
        this.degree = 0;
      }
      if (initObj.hasOwnProperty('clockwise')) {
        this.clockwise = initObj.clockwise
      }
      else {
        this.clockwise = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type twist
    // Serialize message field [degree]
    bufferOffset = _serializer.int64(obj.degree, buffer, bufferOffset);
    // Serialize message field [clockwise]
    bufferOffset = _serializer.bool(obj.clockwise, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type twist
    let len;
    let data = new twist(null);
    // Deserialize message field [degree]
    data.degree = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [clockwise]
    data.clockwise = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 9;
  }

  static datatype() {
    // Returns string type for a message object
    return 'hw0/twist';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '128437c3d8b8934f35d831c72604701b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 degree
    bool clockwise
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new twist(null);
    if (msg.degree !== undefined) {
      resolved.degree = msg.degree;
    }
    else {
      resolved.degree = 0
    }

    if (msg.clockwise !== undefined) {
      resolved.clockwise = msg.clockwise;
    }
    else {
      resolved.clockwise = false
    }

    return resolved;
    }
};

module.exports = twist;
