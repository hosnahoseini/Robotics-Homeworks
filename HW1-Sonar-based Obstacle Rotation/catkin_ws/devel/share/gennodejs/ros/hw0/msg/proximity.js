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

class proximity {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.up = null;
      this.down = null;
      this.left = null;
      this.right = null;
    }
    else {
      if (initObj.hasOwnProperty('up')) {
        this.up = initObj.up
      }
      else {
        this.up = 0;
      }
      if (initObj.hasOwnProperty('down')) {
        this.down = initObj.down
      }
      else {
        this.down = 0;
      }
      if (initObj.hasOwnProperty('left')) {
        this.left = initObj.left
      }
      else {
        this.left = 0;
      }
      if (initObj.hasOwnProperty('right')) {
        this.right = initObj.right
      }
      else {
        this.right = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type proximity
    // Serialize message field [up]
    bufferOffset = _serializer.int64(obj.up, buffer, bufferOffset);
    // Serialize message field [down]
    bufferOffset = _serializer.int64(obj.down, buffer, bufferOffset);
    // Serialize message field [left]
    bufferOffset = _serializer.int64(obj.left, buffer, bufferOffset);
    // Serialize message field [right]
    bufferOffset = _serializer.int64(obj.right, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type proximity
    let len;
    let data = new proximity(null);
    // Deserialize message field [up]
    data.up = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [down]
    data.down = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [left]
    data.left = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [right]
    data.right = _deserializer.int64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 32;
  }

  static datatype() {
    // Returns string type for a message object
    return 'hw0/proximity';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '7e422bbe29fec8ddaffc447bd5b0585b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 up
    int64 down
    int64 left
    int64 right
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new proximity(null);
    if (msg.up !== undefined) {
      resolved.up = msg.up;
    }
    else {
      resolved.up = 0
    }

    if (msg.down !== undefined) {
      resolved.down = msg.down;
    }
    else {
      resolved.down = 0
    }

    if (msg.left !== undefined) {
      resolved.left = msg.left;
    }
    else {
      resolved.left = 0
    }

    if (msg.right !== undefined) {
      resolved.right = msg.right;
    }
    else {
      resolved.right = 0
    }

    return resolved;
    }
};

module.exports = proximity;
