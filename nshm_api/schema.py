"""The main API schema."""

import logging

import graphene
from graphene import relay

log = logging.getLogger(__name__)


class QueryRoot(graphene.ObjectType):
    """This is the entry point for solvis graphql query operations"""

    node = relay.Node.Field()
    about = graphene.String(description='About this API ')

    def resolve_about(root, info, **args):
        return "Hello World, I am nshm_api!"


schema_root = graphene.Schema(query=QueryRoot, mutation=None, auto_camelcase=False)
