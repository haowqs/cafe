
# from .models import Customers as csrmodel

from graphql import GraphQLError
from graphene_django import DjangoObjectType
import graphene

from datetime import datetime
from random import choice

from .models import Customers as CSRmodel


# class MatchInfo(graphene.ObjectType):
#     name = graphene.String()
#     image = graphene.String()
#     hobby = graphene.String()
#     life_maxim = graphene.String()


class MatchType(DjangoObjectType):
    # group = graphene.List(MatchInfo)
    class Meta:
        model = CSRmodel


class Query(graphene.ObjectType):
    match = graphene.Field(MatchType, gender=graphene.String(required=True))

    def resolve_match(self, info, gender):
        """随机匹配"""
        print(gender)
        gender_choices = {'男': 'male', '女': 'female'}
        genderen = gender_choices.get(gender)
        XSRObj = CSRmodel.objects.exclude(gender=genderen)
        matchpepole = choice(XSRObj)
        return matchpepole
