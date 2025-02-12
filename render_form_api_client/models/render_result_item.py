import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RenderResultItem")


@_attrs_define
class RenderResultItem:
    """
    Attributes:
        identifier (Union[Unset, str]):
        href (Union[Unset, str]):
        width (Union[Unset, int]):
        height (Union[Unset, int]):
        template_name (Union[Unset, str]):
        template_identifier (Union[Unset, str]):
        file_name (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        deleted_at (Union[Unset, datetime.datetime]):
    """

    identifier: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    width: Union[Unset, int] = UNSET
    height: Union[Unset, int] = UNSET
    template_name: Union[Unset, str] = UNSET
    template_identifier: Union[Unset, str] = UNSET
    file_name: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    deleted_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        href = self.href

        width = self.width

        height = self.height

        template_name = self.template_name

        template_identifier = self.template_identifier

        file_name = self.file_name

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        deleted_at: Union[Unset, str] = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if href is not UNSET:
            field_dict["href"] = href
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if template_name is not UNSET:
            field_dict["templateName"] = template_name
        if template_identifier is not UNSET:
            field_dict["templateIdentifier"] = template_identifier
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        identifier = d.pop("identifier", UNSET)

        href = d.pop("href", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        template_name = d.pop("templateName", UNSET)

        template_identifier = d.pop("templateIdentifier", UNSET)

        file_name = d.pop("fileName", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _deleted_at = d.pop("deletedAt", UNSET)
        deleted_at: Union[Unset, datetime.datetime]
        if isinstance(_deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = isoparse(_deleted_at)

        render_result_item = cls(
            identifier=identifier,
            href=href,
            width=width,
            height=height,
            template_name=template_name,
            template_identifier=template_identifier,
            file_name=file_name,
            created_at=created_at,
            deleted_at=deleted_at,
        )

        render_result_item.additional_properties = d
        return render_result_item

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
