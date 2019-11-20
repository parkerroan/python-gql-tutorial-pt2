from models.user import UserModel
from models.request import RequestModel

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )


class Request(SQLAlchemyObjectType):
    class Meta:
        model = RequestModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allow only single column sorting
    all_users = SQLAlchemyConnectionField(
        User, sort=User.sort_argument())
    # Disable sorting over this field
    all_requests = SQLAlchemyConnectionField(Request, sort=None)

schema = graphene.Schema(query=Query, types=[User, Request])