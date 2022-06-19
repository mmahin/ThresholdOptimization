from AgreementFunction.PolygonIntersection import PolygonIntersection
from AgreementFunction.PolygonUnion import PolygonUnion
def Agreement(hotspot_list1: list, hotspot_list2: list):
    if len(hotspot_list1) == 0 or len(hotspot_list2)==0:
        return 0
    intersection_area = PolygonIntersection(hotspot_list1, hotspot_list2)
    union_area = PolygonUnion(hotspot_list1, hotspot_list2,intersection_area)

    agreement = intersection_area/union_area

    return agreement