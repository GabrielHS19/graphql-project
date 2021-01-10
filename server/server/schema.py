import graphene

import ciudades.schema


class Query(ciudades.schema.Query, graphene.ObjectType):
    pass

class Mutation(ciudades.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
