from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.change_placeholder import ChangePlaceholder
    from ..models.font_item import FontItem


T = TypeVar("T", bound="GetTemplateBasics")


@_attrs_define
class GetTemplateBasics:
    """
    Attributes:
        identifier (Union[Unset, str]):
        name (Union[Unset, str]):
        preview (Union[Unset, str]):
        scale_factor (Union[Unset, float]):
        output_format (Union[Unset, str]):
        output_extension (Union[Unset, str]):
        quality (Union[Unset, int]):
        width (Union[Unset, int]):
        height (Union[Unset, int]):
        created_by (Union[Unset, str]):
        editor (Union[Unset, str]):
        properties (Union[Unset, list['ChangePlaceholder']]):
        fonts (Union[Unset, list['FontItem']]):
        catalog (Union[Unset, str]):
    """

    identifier: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    preview: Union[Unset, str] = UNSET
    scale_factor: Union[Unset, float] = UNSET
    output_format: Union[Unset, str] = UNSET
    output_extension: Union[Unset, str] = UNSET
    quality: Union[Unset, int] = UNSET
    width: Union[Unset, int] = UNSET
    height: Union[Unset, int] = UNSET
    created_by: Union[Unset, str] = UNSET
    editor: Union[Unset, str] = UNSET
    properties: Union[Unset, list["ChangePlaceholder"]] = UNSET
    fonts: Union[Unset, list["FontItem"]] = UNSET
    catalog: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        name = self.name

        preview = self.preview

        scale_factor = self.scale_factor

        output_format = self.output_format

        output_extension = self.output_extension

        quality = self.quality

        width = self.width

        height = self.height

        created_by = self.created_by

        editor = self.editor

        properties: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        fonts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fonts, Unset):
            fonts = []
            for fonts_item_data in self.fonts:
                fonts_item = fonts_item_data.to_dict()
                fonts.append(fonts_item)

        catalog = self.catalog

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if name is not UNSET:
            field_dict["name"] = name
        if preview is not UNSET:
            field_dict["preview"] = preview
        if scale_factor is not UNSET:
            field_dict["scaleFactor"] = scale_factor
        if output_format is not UNSET:
            field_dict["outputFormat"] = output_format
        if output_extension is not UNSET:
            field_dict["outputExtension"] = output_extension
        if quality is not UNSET:
            field_dict["quality"] = quality
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if editor is not UNSET:
            field_dict["editor"] = editor
        if properties is not UNSET:
            field_dict["properties"] = properties
        if fonts is not UNSET:
            field_dict["fonts"] = fonts
        if catalog is not UNSET:
            field_dict["catalog"] = catalog

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.change_placeholder import ChangePlaceholder
        from ..models.font_item import FontItem

        d = src_dict.copy()
        identifier = d.pop("identifier", UNSET)

        name = d.pop("name", UNSET)

        preview = d.pop("preview", UNSET)

        scale_factor = d.pop("scaleFactor", UNSET)

        output_format = d.pop("outputFormat", UNSET)

        output_extension = d.pop("outputExtension", UNSET)

        quality = d.pop("quality", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        created_by = d.pop("createdBy", UNSET)

        editor = d.pop("editor", UNSET)

        properties = []
        _properties = d.pop("properties", UNSET)
        for properties_item_data in _properties or []:
            properties_item = ChangePlaceholder.from_dict(properties_item_data)

            properties.append(properties_item)

        fonts = []
        _fonts = d.pop("fonts", UNSET)
        for fonts_item_data in _fonts or []:
            fonts_item = FontItem.from_dict(fonts_item_data)

            fonts.append(fonts_item)

        catalog = d.pop("catalog", UNSET)

        get_template_basics = cls(
            identifier=identifier,
            name=name,
            preview=preview,
            scale_factor=scale_factor,
            output_format=output_format,
            output_extension=output_extension,
            quality=quality,
            width=width,
            height=height,
            created_by=created_by,
            editor=editor,
            properties=properties,
            fonts=fonts,
            catalog=catalog,
        )

        get_template_basics.additional_properties = d
        return get_template_basics

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
