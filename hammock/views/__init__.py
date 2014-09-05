class View(object):
	
	serializers = None
	
	def get_collection_response(self, req, objs):
		raise NotImplementedError
		
		
	def get_individual_response(self, req, obj):
		raise NotImplementedError
		
		
	def serialize(self, req, obj):
		content_type, serializer = self.get_serializer(req)
		return content_type, serializer.serialize(obj)
		
		
	def get_serializer(self, req):
		raw_accept = req.get_header('Accept')
		if raw_accept:
			accept = raw_accept.split(';')[0].split(',')
			for a in accept:
				for k,v in self.serializers:
					if a == k:
						return k, v
		return self.serializers[0]
		
		
		
from minimal import MinimalView