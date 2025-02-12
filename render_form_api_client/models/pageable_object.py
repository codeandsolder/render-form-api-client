from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sort_object import SortObject


T = TypeVar("T", bound="PageableObject")


@_attrs_define
class PageableObject:
    """
    Attributes:
        paged (Union[Unset, bool]):
        unpaged (Union[Unset, bool]):
        page_size (Union[Unset, int]):
        page_number (Union[Unset, int]):
        offset (Union[Unset, int]):
        sort (Union[Unset, SortObject]):
    """

    paged: Union[Unset, bool] = UNSET
    unpaged: Union[Unset, bool] = UNSET
    page_size: Union[Unset, int] = UNSET
    page_number: Union[Unset, int] = UNSET
    offset: Union[Unset, int] = UNSET
    sort: Union[Unset, "SortObject"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        paged = self.paged

        unpaged = self.unpaged

        page_size = self.page_size

        page_number = self.page_number

        offset = self.offset

        sort: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if paged is not UNSET:
            field_dict["paged"] = paged
        if unpaged is not UNSET:
            field_dict["unpaged"] = unpaged
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if page_number is not UNSET:
            field_dict["pageNumber"] = page_number
        if offset is not UNSET:
            field_dict["offset"] = offset
        if sort is not UNSET:
            field_dict["sort"] = sort

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.sort_object import SortObject

        d = src_dict.copy()
        paged = d.pop("paged", UNSET)

        unpaged = d.pop("unpaged", UNSET)

        page_size = d.pop("pageSize", UNSET)

        page_number = d.pop("pageNumber", UNSET)

        offset = d.pop("offset", UNSET)

        _sort = d.pop("sort", UNSET)
        sort: Union[Unset, SortObject]
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = SortObject.from_dict(_sort)

        pageable_object = cls(
            paged=paged,
            unpaged=unpaged,
            page_size=page_size,
            page_number=page_number,
            offset=offset,
            sort=sort,
        )

        pageable_object.additional_properties = d
        return pageable_object

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
