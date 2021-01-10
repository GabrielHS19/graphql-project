import graphene
from graphene_django import DjangoObjectType

from .models import Ciudad


class LinkType(DjangoObjectType):
    class Meta:
        model = Ciudad


class Query(graphene.ObjectType):
    ciudades = graphene.List(LinkType)

    def resolve_ciudades(self, info, **kwargs):
        return Ciudad.objects.all()

class CreateLink(graphene.Mutation):
    id = graphene.Int()
    ciudad = graphene.String()
    pais = graphene.String()
    codigoPostal = graphene.String()
    numeroAccidentes = graphene.String()

    #2
    class Arguments:
        ciudad = graphene.String()
        pais = graphene.String()
        codigoPostal = graphene.String()
        numeroAccidentes = graphene.String()

    #3
    def mutate(self, info, ciudad, pais, codigoPostal, numeroAccidentes):
        ciudad = Ciudad(ciudad=ciudad, pais=pais, codigoPostal=codigoPostal, numeroAccidentes=numeroAccidentes)
        ciudad.save()

        return CreateLink(
            id=ciudad.id,
            ciudad=ciudad.ciudad,
            pais=ciudad.pais,
            codigoPostal=ciudad.codigoPostal,
            numeroAccidentes=ciudad.numeroAccidentes,
        )


#4
class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()


