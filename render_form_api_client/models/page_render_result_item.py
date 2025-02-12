from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pageable_object import PageableObject
    from ..models.render_result_item import RenderResultItem
    from ..models.sort_object import SortObject


T = TypeVar("T", bound="PageRenderResultItem")


@_attrs_define
class PageRenderResultItem:
    """
    Attributes:
        total_pages (Union[Unset, int]):
        total_elements (Union[Unset, int]):
        pageable (Union[Unset, PageableObject]):
        number_of_elements (Union[Unset, int]):
        first (Union[Unset, bool]):
        last (Union[Unset, bool]):
        size (Union[Unset, int]):
        content (Union[Unset, list['RenderResultItem']]):
        number (Union[Unset, int]):
        sort (Union[Unset, SortObject]):
        empty (Union[Unset, bool]):
    """

    total_pages: Union[Unset, int] = UNSET
    total_elements: Union[Unset, int] = UNSET
    pageable: Union[Unset, "PageableObject"] = UNSET
    number_of_elements: Union[Unset, int] = UNSET
    first: Union[Unset, bool] = UNSET
    last: Union[Unset, bool] = UNSET
    size: Union[Unset, int] = UNSET
    content: Union[Unset, list["RenderResultItem"]] = UNSET
    number: Union[Unset, int] = UNSET
    sort: Union[Unset, "SortObject"] = UNSET
    empty: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_pages = self.total_pages

        total_elements = self.total_elements

        pageable: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pageable, Unset):
            pageable = self.pageable.to_dict()

        number_of_elements = self.number_of_elements

        first = self.first

        last = self.last

        size = self.size

        content: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.content, Unset):
            content = []
            for content_item_data in self.content:
                content_item = content_item_data.to_dict()
                content.append(content_item)

        number = self.number

        sort: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.to_dict()

        empty = self.empty

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_pages is not UNSET:
            field_dict["totalPages"] = total_pages
        if total_elements is not UNSET:
            field_dict["totalElements"] = total_elements
        if pageable is not UNSET:
            field_dict["pageable"] = pageable
        if number_of_elements is not UNSET:
            field_dict["numberOfElements"] = number_of_elements
        if first is not UNSET:
            field_dict["first"] = first
        if last is not UNSET:
            field_dict["last"] = last
        if size is not UNSET:
            field_dict["size"] = size
        if content is not UNSET:
            field_dict["content"] = content
        if number is not UNSET:
            field_dict["number"] = number
        if sort is not UNSET:
            field_dict["sort"] = sort
        if empty is not UNSET:
            field_dict["empty"] = empty

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.pageable_object import PageableObject
        from ..models.render_result_item import RenderResultItem
        from ..models.sort_object import SortObject

        d = src_dict.copy()
        total_pages = d.pop("totalPages", UNSET)

        total_elements = d.pop("totalElements", UNSET)

        _pageable = d.pop("pageable", UNSET)
        pageable: Union[Unset, PageableObject]
        if isinstance(_pageable, Unset):
            pageable = UNSET
        else:
            pageable = PageableObject.from_dict(_pageable)

        number_of_elements = d.pop("numberOfElements", UNSET)

        first = d.pop("first", UNSET)

        last = d.pop("last", UNSET)

        size = d.pop("size", UNSET)

        content = []
        _content = d.pop("content", UNSET)
        for content_item_data in _content or []:
            content_item = RenderResultItem.from_dict(content_item_data)

            content.append(content_item)

        number = d.pop("number", UNSET)

        _sort = d.pop("sort", UNSET)
        sort: Union[Unset, SortObject]
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = SortObject.from_dict(_sort)

        empty = d.pop("empty", UNSET)

        page_render_result_item = cls(
            total_pages=total_pages,
            total_elements=total_elements,
            pageable=pageable,
            number_of_elements=number_of_elements,
            first=first,
            last=last,
            size=size,
            content=content,
            number=number,
            sort=sort,
            empty=empty,
        )

        page_render_result_item.additional_properties = d
        return page_render_result_item

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
