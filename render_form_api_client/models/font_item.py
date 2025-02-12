import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.font_item_source import FontItemSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="FontItem")


@_attrs_define
class FontItem:
    """
    Attributes:
        original_name (Union[Unset, str]):
        family (Union[Unset, str]):
        variants (Union[Unset, list[str]]):
        default_variant (Union[Unset, str]):
        subsets (Union[Unset, list[str]]):
        category (Union[Unset, str]):
        source (Union[Unset, FontItemSource]):
        size (Union[Unset, int]):
        created_at (Union[Unset, datetime.datetime]):
    """

    original_name: Union[Unset, str] = UNSET
    family: Union[Unset, str] = UNSET
    variants: Union[Unset, list[str]] = UNSET
    default_variant: Union[Unset, str] = UNSET
    subsets: Union[Unset, list[str]] = UNSET
    category: Union[Unset, str] = UNSET
    source: Union[Unset, FontItemSource] = UNSET
    size: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        original_name = self.original_name

        family = self.family

        variants: Union[Unset, list[str]] = UNSET
        if not isinstance(self.variants, Unset):
            variants = self.variants

        default_variant = self.default_variant

        subsets: Union[Unset, list[str]] = UNSET
        if not isinstance(self.subsets, Unset):
            subsets = self.subsets

        category = self.category

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        size = self.size

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if original_name is not UNSET:
            field_dict["originalName"] = original_name
        if family is not UNSET:
            field_dict["family"] = family
        if variants is not UNSET:
            field_dict["variants"] = variants
        if default_variant is not UNSET:
            field_dict["defaultVariant"] = default_variant
        if subsets is not UNSET:
            field_dict["subsets"] = subsets
        if category is not UNSET:
            field_dict["category"] = category
        if source is not UNSET:
            field_dict["source"] = source
        if size is not UNSET:
            field_dict["size"] = size
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        original_name = d.pop("originalName", UNSET)

        family = d.pop("family", UNSET)

        variants = cast(list[str], d.pop("variants", UNSET))

        default_variant = d.pop("defaultVariant", UNSET)

        subsets = cast(list[str], d.pop("subsets", UNSET))

        category = d.pop("category", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, FontItemSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = FontItemSource(_source)

        size = d.pop("size", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        font_item = cls(
            original_name=original_name,
            family=family,
            variants=variants,
            default_variant=default_variant,
            subsets=subsets,
            category=category,
            source=source,
            size=size,
            created_at=created_at,
        )

        font_item.additional_properties = d
        return font_item

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
