from dogbreed import db
from sqlalchemy.ext.declarative import DeclarativeMeta


class ModelDictMixin(object):
    def as_dict(self, fields_to_expand=[]):
	# return {c.name: getattr(self, c.name) for c in self.__table__.columns}

	# go through each field in this SQLalchemy class
	fields = {}
	for field in [x for x in dir(self) if not x.startswith('_') and x not in ['metadata', 'query', 'query_class', 'as_dict']]:
	    val = self.__getattribute__(field)

	    # is this field another SQLalchemy object, or a list of SQLalchemy objects?
	    if isinstance(val.__class__, DeclarativeMeta) or (isinstance(val, list) and len(val) > 0 and isinstance(val[0].__class__, DeclarativeMeta)):
		# unless we're expanding this field, stop here
		if field not in fields_to_expand:
		    # not expanding this field: set it to None and continue
		    fields[field] = None
		    continue
		fields[field] = val.as_dict()
		continue
	    fields[field] = val
	# a json-encodable dict
	return fields

class BaseModel(db.Model, ModelDictMixin):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
