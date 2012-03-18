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
        writer.add_document(type=u"Commodity",
                            id=unicode(com.id),
                            title=unicode(com.name.lower()),
                            content=unicode(com.des.lower()))


def travel_comment(writer):
    comments = CommodityComment.select()
    for com in comments:
        writer.add_document(type=u"CommodityComment",
                            id=unicode(com.commodity.id),
                            title=unicode(com.commodity.name.lower()),
                            content=unicode(com.comment.lower()))


if __name__ == '__main__':
    schema = Schema(type=TEXT(stored=True),
                    id=ID(stored=True),
                    title=TEXT(stored=True),
                    content=TEXT)
    ix = create_in(app.config.get("INDEX_DIR"), schema)
    writer = ix.writer()
    travel_commodity(writer)
    travel_comment(writer)
    writer.commit()
