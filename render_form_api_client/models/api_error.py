from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiError")


@_attrs_define
class ApiError:
    """
    Attributes:
        msg (Union[Unset, str]):
        status (Union[Unset, int]):
        errors (Union[Unset, list[str]]):
    """

    msg: Union[Unset, str] = UNSET
    status: Union[Unset, int] = UNSET
    errors: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        msg = self.msg

        status = self.status

        errors: Union[Unset, list[str]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if msg is not UNSET:
            field_dict["msg"] = msg
        if status is not UNSET:
            field_dict["status"] = status
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        msg = d.pop("msg", UNSET)

        status = d.pop("status", UNSET)

        errors = cast(list[str], d.pop("errors", UNSET))

        api_error = cls(
            msg=msg,
            status=status,
            errors=errors,
        )

        api_error.additional_properties = d
        return api_error

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
