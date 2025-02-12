from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.render_request_data import RenderRequestData
    from ..models.render_request_metadata import RenderRequestMetadata


T = TypeVar("T", bound="RenderRequest")


@_attrs_define
class RenderRequest:
    """
    Attributes:
        template (str): Template ID Example: template_1234.
        data (Union[Unset, RenderRequestData]): Data to be merged into the template Example: {'my-text.text': 'John'}.
        file_name (Union[Unset, str]): Name of the file to be returned Example: my-file-name.
        webhook_url (Union[Unset, str]): Webhook URL to be called when the render is done Example: https://my-
            webhook.com.
        version (Union[Unset, str]): Cache key to be used for caching the rendered image Example: my-cache-key.
        metadata (Union[Unset, RenderRequestMetadata]): Additional metadata to be passed to the webhook Example: {'my-
            text.text': 'John'}.
        batch_name (Union[Unset, str]): Batch name to be used for grouping renders Example: my-batch-name.
    """

    template: str
    data: Union[Unset, "RenderRequestData"] = UNSET
    file_name: Union[Unset, str] = UNSET
    webhook_url: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    metadata: Union[Unset, "RenderRequestMetadata"] = UNSET
    batch_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template = self.template

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        file_name = self.file_name

        webhook_url = self.webhook_url

        version = self.version

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        batch_name = self.batch_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "template": template,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if webhook_url is not UNSET:
            field_dict["webhookUrl"] = webhook_url
        if version is not UNSET:
            field_dict["version"] = version
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if batch_name is not UNSET:
            field_dict["batchName"] = batch_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.render_request_data import RenderRequestData
        from ..models.render_request_metadata import RenderRequestMetadata

        d = src_dict.copy()
        template = d.pop("template")

        _data = d.pop("data", UNSET)
        data: Union[Unset, RenderRequestData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = RenderRequestData.from_dict(_data)

        file_name = d.pop("fileName", UNSET)

        webhook_url = d.pop("webhookUrl", UNSET)

        version = d.pop("version", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, RenderRequestMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = RenderRequestMetadata.from_dict(_metadata)

        batch_name = d.pop("batchName", UNSET)

        render_request = cls(
            template=template,
            data=data,
            file_name=file_name,
            webhook_url=webhook_url,
            version=version,
            metadata=metadata,
            batch_name=batch_name,
        )

        render_request.additional_properties = d
        return render_request

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
