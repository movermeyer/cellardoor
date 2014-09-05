import msgpack
from datetime import datetime
from . import Serializer


def default_handler(obj):
	try:
		iterable = iter(obj)
	except TypeError:
		pass
	else:
		return list(iterable)
	
	if isinstance(obj, datetime):
		return obj.isoformat()
	
	raise ValueError, "Can't pack object of type %s" % type(obj).__name__
	


class MsgPackSerializer(Serializer):
	
	mimetype = 'application/x-msgpack'
	
	def serialize(self, obj):
		return msgpack.packb(obj, default=default_handler)
		
		
	def unserialize(self, stream):
		return msgpack.unpack(stream)