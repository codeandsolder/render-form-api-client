from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_screenshot_request import CreateScreenshotRequest


T = TypeVar("T", bound="CreateScreenshotResponse")


@_attrs_define
class CreateScreenshotResponse:
    """
    Attributes:
        request_id (Union[Unset, str]):
        href (Union[Unset, str]):
        request (Union[Unset, CreateScreenshotRequest]):
    """

    request_id: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    request: Union[Unset, "CreateScreenshotRequest"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request_id = self.request_id

        href = self.href

        request: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.request, Unset):
            request = self.request.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if href is not UNSET:
            field_dict["href"] = href
        if request is not UNSET:
            field_dict["request"] = request

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.create_screenshot_request import CreateScreenshotRequest

        d = src_dict.copy()
        request_id = d.pop("requestId", UNSET)

        href = d.pop("href", UNSET)

        _request = d.pop("request", UNSET)
        request: Union[Unset, CreateScreenshotRequest]
        if isinstance(_request, Unset):
            request = UNSET
        else:
            request = CreateScreenshotRequest.from_dict(_request)

        create_screenshot_response = cls(
            request_id=request_id,
            href=href,
            request=request,
        )

        create_screenshot_response.additional_properties = d
        return create_screenshot_response

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
