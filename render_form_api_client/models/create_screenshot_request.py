from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateScreenshotRequest")


@_attrs_define
class CreateScreenshotRequest:
    """
    Attributes:
        url (str): URL to capture Example: https://renderform.io.
        width (int): Width of the screenshot in pixels Example: 1920.
        height (int): Height of the screenshot in pixels Example: 1080.
        wait_time (Union[Unset, int]): Wait time in milliseconds before capturing the screenshot Example: 1000.
    """

    url: str
    width: int
    height: int
    wait_time: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        width = self.width

        height = self.height

        wait_time = self.wait_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "width": width,
                "height": height,
            }
        )
        if wait_time is not UNSET:
            field_dict["waitTime"] = wait_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url")

        width = d.pop("width")

        height = d.pop("height")

        wait_time = d.pop("waitTime", UNSET)

        create_screenshot_request = cls(
            url=url,
            width=width,
            height=height,
            wait_time=wait_time,
        )

        create_screenshot_request.additional_properties = d
        return create_screenshot_request

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
