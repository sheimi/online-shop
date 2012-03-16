'''
This file is to create the index of commodities 
'''
from models import *
from whoosh.index import create_in
from whoosh.fields import *
from shop import app

def travel_commodity(writer):
    commodities = Commodity.select()
    for com in commodities:
        writer.add_document(type=u"commodity",
                            id=unicode(com.id),
                            name=unicode(com.name),
                            des=unicode(com.des))



if __name__ == '__main__':
    schema = Schema(type=TEXT(stored=True),
                    id = ID(stored=True),
                    name = TEXT(stored=True),
                    des= TEXT)
    ix = create_in(app.config.get("INDEX_DIR"), schema)
    writer = ix.writer()
    travel_commodity(writer)
    writer.commit()
