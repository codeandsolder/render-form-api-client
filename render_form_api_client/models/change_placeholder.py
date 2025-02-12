from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.change_placeholder_component_type import ChangePlaceholderComponentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangePlaceholder")


@_attrs_define
class ChangePlaceholder:
    """
    Attributes:
        component_id (Union[Unset, str]):
        component_type (Union[Unset, ChangePlaceholderComponentType]):
        type_ (Union[Unset, str]):
        key (Union[Unset, str]):
        property_ (Union[Unset, str]):
        default_value (Union[Unset, str]):
    """

    component_id: Union[Unset, str] = UNSET
    component_type: Union[Unset, ChangePlaceholderComponentType] = UNSET
    type_: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    property_: Union[Unset, str] = UNSET
    default_value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_id = self.component_id

        component_type: Union[Unset, str] = UNSET
        if not isinstance(self.component_type, Unset):
            component_type = self.component_type.value

        type_ = self.type_

        key = self.key

        property_ = self.property_

        default_value = self.default_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if component_id is not UNSET:
            field_dict["componentId"] = component_id
        if component_type is not UNSET:
            field_dict["componentType"] = component_type
        if type_ is not UNSET:
            field_dict["type"] = type_
        if key is not UNSET:
            field_dict["key"] = key
        if property_ is not UNSET:
            field_dict["property"] = property_
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        component_id = d.pop("componentId", UNSET)

        _component_type = d.pop("componentType", UNSET)
        component_type: Union[Unset, ChangePlaceholderComponentType]
        if isinstance(_component_type, Unset):
            component_type = UNSET
        else:
            component_type = ChangePlaceholderComponentType(_component_type)

        type_ = d.pop("type", UNSET)

        key = d.pop("key", UNSET)

        property_ = d.pop("property", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        change_placeholder = cls(
            component_id=component_id,
            component_type=component_type,
            type_=type_,
            key=key,
            property_=property_,
            default_value=default_value,
        )

        change_placeholder.additional_properties = d
        return change_placeholder

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
