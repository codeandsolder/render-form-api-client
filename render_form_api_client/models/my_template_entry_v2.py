from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MyTemplateEntryV2")


@_attrs_define
class MyTemplateEntryV2:
    """
    Attributes:
        identifier (Union[Unset, str]):
        name (Union[Unset, str]):
        preview (Union[Unset, str]):
        scale_factor (Union[Unset, float]):
        output_format (Union[Unset, str]):
        output_extension (Union[Unset, str]):
        quality (Union[Unset, int]):
        is_shared (Union[Unset, bool]):
        is_live_preview_shared (Union[Unset, bool]):
        is_email_notification (Union[Unset, bool]):
        email_notification (Union[Unset, str]):
        width (Union[Unset, int]):
        height (Union[Unset, int]):
        created_by (Union[Unset, str]):
        created_at (Union[Unset, str]):
        editor (Union[Unset, str]):
        catalog (Union[Unset, str]):
    """

    identifier: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    preview: Union[Unset, str] = UNSET
    scale_factor: Union[Unset, float] = UNSET
    output_format: Union[Unset, str] = UNSET
    output_extension: Union[Unset, str] = UNSET
    quality: Union[Unset, int] = UNSET
    is_shared: Union[Unset, bool] = UNSET
    is_live_preview_shared: Union[Unset, bool] = UNSET
    is_email_notification: Union[Unset, bool] = UNSET
    email_notification: Union[Unset, str] = UNSET
    width: Union[Unset, int] = UNSET
    height: Union[Unset, int] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    editor: Union[Unset, str] = UNSET
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

        is_shared = self.is_shared

        is_live_preview_shared = self.is_live_preview_shared

        is_email_notification = self.is_email_notification

        email_notification = self.email_notification

        width = self.width

        height = self.height

        created_by = self.created_by

        created_at = self.created_at

        editor = self.editor

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
        if is_shared is not UNSET:
            field_dict["isShared"] = is_shared
        if is_live_preview_shared is not UNSET:
            field_dict["isLivePreviewShared"] = is_live_preview_shared
        if is_email_notification is not UNSET:
            field_dict["isEmailNotification"] = is_email_notification
        if email_notification is not UNSET:
            field_dict["emailNotification"] = email_notification
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if editor is not UNSET:
            field_dict["editor"] = editor
        if catalog is not UNSET:
            field_dict["catalog"] = catalog

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        identifier = d.pop("identifier", UNSET)

        name = d.pop("name", UNSET)

        preview = d.pop("preview", UNSET)

        scale_factor = d.pop("scaleFactor", UNSET)

        output_format = d.pop("outputFormat", UNSET)

        output_extension = d.pop("outputExtension", UNSET)

        quality = d.pop("quality", UNSET)

        is_shared = d.pop("isShared", UNSET)

        is_live_preview_shared = d.pop("isLivePreviewShared", UNSET)

        is_email_notification = d.pop("isEmailNotification", UNSET)

        email_notification = d.pop("emailNotification", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        created_by = d.pop("createdBy", UNSET)

        created_at = d.pop("createdAt", UNSET)

        editor = d.pop("editor", UNSET)

        catalog = d.pop("catalog", UNSET)

        my_template_entry_v2 = cls(
            identifier=identifier,
            name=name,
            preview=preview,
            scale_factor=scale_factor,
            output_format=output_format,
            output_extension=output_extension,
            quality=quality,
            is_shared=is_shared,
            is_live_preview_shared=is_live_preview_shared,
            is_email_notification=is_email_notification,
            email_notification=email_notification,
            width=width,
            height=height,
            created_by=created_by,
            created_at=created_at,
            editor=editor,
            catalog=catalog,
        )

        my_template_entry_v2.additional_properties = d
        return my_template_entry_v2

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
