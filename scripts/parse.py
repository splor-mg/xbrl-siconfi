import logging
from xbrl.cache import HttpCache
from xbrl.instance import XbrlParser
from pprint import pprint
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

logging.basicConfig(level=logging.INFO)

cache = HttpCache("./cache")
parser = XbrlParser(cache)

inst = parser.parse_instance("data-raw/instancia.xml")

facts = [fact.json() for fact in inst.facts]

def get_total(concept, total=True):
    data = [
    fact for fact in facts 
    if fact["dimensions"]["concept"] == concept and
    fact["dimensions"]["PoderOrgaosAxis"] == "TotalMember"
    ]
    if len(data) == 1:
        return locale.currency(data[0]["value"], grouping=True, symbol=False)
    else:
        raise Exception

get_total("RestosAPagarProcessadosENaoProcessadosLiquidadosInscritosEmExerciciosAnteriores")
get_total("RestosAPagarProcessadosENaoProcessadosLiquidadosInscritosEmExercicioAnterior")
get_total("RestosAPagarProcessadosENaoProcessadosLiquidadosPagos")
get_total("RestosAPagarProcessadosENaoProcessadosLiquidadosCancelados")
get_total("RestosAPagarProcessadosENaoProcessadosLiquidadosAPagar")

get_total("RestosAPagarNaoProcessadosInscritosEmExerciciosAnteriores")
get_total("RestosAPagarNaoProcessadosInscritosEmExercicioAnterior")
get_total("RestosAPagarNaoProcessadosLiquidados")
get_total("RestosAPagarNaoProcessadosPagos")
get_total("RestosAPagarNaoProcessadosCancelados")
get_total("RestosAPagarNaoProcessadosAPagar")
get_total("SaldoTotal")

data = [
fact for fact in facts 
if fact["dimensions"]["concept"] == "SaldoTotalIntra"
]
pprint(data)

get_total("RestosAPagarProcessadosENaoProcessadosLiquidadosInscritosEmExerciciosAnterioresIntra")
get_total("RestosAPagarProcessadosENaoProcessadosLiquidadosInscritosEmExercicioAnteriorIntra")
get_total("RestosAPagarProcessadosENaoProcessadosLiquidadosPagosIntra")
get_total("RestosAPagarProcessadosENaoProcessadosLiquidadosCanceladosIntra")
get_total("RestosAPagarProcessadosENaoProcessadosLiquidadosAPagarIntra")
get_total("RestosAPagarNaoProcessadosInscritosEmExerciciosAnterioresIntra")
get_total("RestosAPagarNaoProcessadosInscritosEmExercicioAnteriorIntra")
get_total("RestosAPagarNaoProcessadosLiquidadosIntra")
get_total("RestosAPagarNaoProcessadosPagosIntra")
get_total("RestosAPagarNaoProcessadosCanceladosIntra")
get_total("RestosAPagarNaoProcessadosAPagarIntra")
get_total("SaldoTotalIntra")


# <siconfi-cor:FonteAnexo7Tabela7.0RREO contextRef="C3247">Nos bimestres de 2021 os valores apresentados diferem da publicação, pois, no saldo de Restos a Pagar Processados são incluídos os Restos a Pagar de origem Não Processada que foram liquidados e não pagos no exercício.</siconfi-cor:FonteAnexo7Tabela7.0RREO>


