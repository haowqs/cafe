
import graphene
from graphene_django.debug import DjangoDebug

import pair.schema

class Query(pair.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='_debug')




schema = graphene.Schema(query=Query)