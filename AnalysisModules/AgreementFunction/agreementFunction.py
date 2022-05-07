from AgreementFunction.PolygonIntersection import PolygonIntersection
from AgreementFunction.PolygonUnion import PolygonUnion
def Agreement(hotspot_list1: list, hotspot_list2: list):
    intersection_area = PolygonIntersection(hotspot_list1, hotspot_list2)
    union_area = PolygonUnion(hotspot_list1, hotspot_list2,intersection_area)

    agreement = intersection_area/union_area

    return agreement