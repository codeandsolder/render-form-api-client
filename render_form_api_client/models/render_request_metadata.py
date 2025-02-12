from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.render_request_metadata_additional_property import RenderRequestMetadataAdditionalProperty


T = TypeVar("T", bound="RenderRequestMetadata")


@_attrs_define
class RenderRequestMetadata:
    """Additional metadata to be passed to the webhook

    Example:
        {'my-text.text': 'John'}

    """

    additional_properties: dict[str, "RenderRequestMetadataAdditionalProperty"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.render_request_metadata_additional_property import RenderRequestMetadataAdditionalProperty

        d = src_dict.copy()
        render_request_metadata = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = RenderRequestMetadataAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        render_request_metadata.additional_properties = additional_properties
        return render_request_metadata

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "RenderRequestMetadataAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "RenderRequestMetadataAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
