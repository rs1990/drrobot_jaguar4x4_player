"""autogenerated by genmsg_py from Range.msg. Do not edit."""
import roslib.message
import struct

import roslib.msg

class Range(roslib.message.Message):
  _md5sum = "c005c34273dc426c67a020a87bc24148"
  _type = "drrobot_player/Range"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# Single range reading from an active ranger that emits energy and reports
# one range reading that is valid along an arc at the distance measured. 
# This message is not appropriate for fixed-range obstacle detectors, 
# such as the Sharp GP2D15. This message is also not appropriate for laser 
# scanners. See the LaserScan message if you are working with a laser scanner.

Header header    	# timestamp in the header is the time the ranger
		 	# returned the distance reading

# Radiation type enums
# If you want a value added to this list, send an email to the ros-users list
uint8 ULTRASOUND=0
uint8 INFRARED=1

uint8 radiation_type    # the type of radiation used by the sensor
		 	# (sound, IR, etc) [enum]

float32 field_of_view   # the size of the arc that the distance reading is
		 	# valid for [rad]
		 	# the object causing the range reading may have
		 	# been anywhere within -field_of_view/2 and
		 	# field_of_view/2 at the measured range. 
                        # 0 angle corresponds to the x-axis of the sensor.

float32 min_range       # minimum range value [m]
float32 max_range       # maximum range value [m]

float32 range           # range data [m]
		 	# (Note: values < range_min or > range_max
		 	# should be discarded)

================================================================================
MSG: roslib/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

"""
  # Pseudo-constants
  ULTRASOUND = 0
  INFRARED = 1

  __slots__ = ['header','radiation_type','field_of_view','min_range','max_range','range']
  _slot_types = ['Header','uint8','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       header,radiation_type,field_of_view,min_range,max_range,range
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(Range, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = roslib.msg._Header.Header()
      if self.radiation_type is None:
        self.radiation_type = 0
      if self.field_of_view is None:
        self.field_of_view = 0.
      if self.min_range is None:
        self.min_range = 0.
      if self.max_range is None:
        self.max_range = 0.
      if self.range is None:
        self.range = 0.
    else:
      self.header = roslib.msg._Header.Header()
      self.radiation_type = 0
      self.field_of_view = 0.
      self.min_range = 0.
      self.max_range = 0.
      self.range = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_B4f.pack(_x.radiation_type, _x.field_of_view, _x.min_range, _x.max_range, _x.range))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      if self.header is None:
        self.header = roslib.msg._Header.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 17
      (_x.radiation_type, _x.field_of_view, _x.min_range, _x.max_range, _x.range,) = _struct_B4f.unpack(str[start:end])
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_B4f.pack(_x.radiation_type, _x.field_of_view, _x.min_range, _x.max_range, _x.range))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      if self.header is None:
        self.header = roslib.msg._Header.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 17
      (_x.radiation_type, _x.field_of_view, _x.min_range, _x.max_range, _x.range,) = _struct_B4f.unpack(str[start:end])
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_3I = struct.Struct("<3I")
_struct_B4f = struct.Struct("<B4f")
