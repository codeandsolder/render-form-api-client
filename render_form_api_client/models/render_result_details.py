import datetime
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RenderResultDetails")


@_attrs_define
class RenderResultDetails:
    """
    Attributes:
        identifier (Union[Unset, str]):
        href (Union[Unset, str]):
        status (Union[Unset, str]):
        width (Union[Unset, int]):
        height (Union[Unset, int]):
        request_payload (Union[Unset, str]):
        template (Union[Unset, str]):
        template_name (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        deleted_at (Union[Unset, datetime.datetime]):
    """

    identifier: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    width: Union[Unset, int] = UNSET
    height: Union[Unset, int] = UNSET
    request_payload: Union[Unset, str] = UNSET
    template: Union[Unset, str] = UNSET
    template_name: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    deleted_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        href = self.href

        status = self.status

        width = self.width

        height = self.height

        request_payload = self.request_payload

        template = self.template

        template_name = self.template_name

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
        if status is not UNSET:
            field_dict["status"] = status
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if request_payload is not UNSET:
            field_dict["requestPayload"] = request_payload
        if template is not UNSET:
            field_dict["template"] = template
        if template_name is not UNSET:
            field_dict["templateName"] = template_name
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

        status = d.pop("status", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        request_payload = d.pop("requestPayload", UNSET)

        template = d.pop("template", UNSET)

        template_name = d.pop("templateName", UNSET)

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

        render_result_details = cls(
            identifier=identifier,
            href=href,
            status=status,
            width=width,
            height=height,
            request_payload=request_payload,
            template=template,
            template_name=template_name,
            created_at=created_at,
            deleted_at=deleted_at,
        )

        render_result_details.additional_properties = d
        return render_result_details

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
