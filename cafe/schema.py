
import graphene
from graphene_django.debug import DjangoDebug

# import pair.schema


class Mutations(graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='_debug')


schema = graphene.Schema(mutation=Mutations)