from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.my_template_entry_v2 import MyTemplateEntryV2
from ...models.swagger_pageable import SwaggerPageable
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: Union[Unset, str] = UNSET,
    catalog: Union[Unset, str] = "",
    pageable: "SwaggerPageable",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["name"] = name

    params["catalog"] = catalog

    json_pageable = pageable.to_dict()
    params.update(json_pageable)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/my-templates",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiError, list["MyTemplateEntryV2"]]]:
    if response.status_code == 400:
        response_400 = ApiError.from_dict(response.json())

        return response_400
    if response.status_code == 418:
        response_418 = ApiError.from_dict(response.json())

        return response_418
    if response.status_code == 402:
        response_402 = ApiError.from_dict(response.json())

        return response_402
    if response.status_code == 403:
        response_403 = ApiError.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ApiError.from_dict(response.json())

        return response_404
    if response.status_code == 503:
        response_503 = ApiError.from_dict(response.json())

        return response_503
    if response.status_code == 500:
        response_500 = ApiError.from_dict(response.json())

        return response_500
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = MyTemplateEntryV2.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiError, list["MyTemplateEntryV2"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    catalog: Union[Unset, str] = "",
    pageable: "SwaggerPageable",
) -> Response[Union[ApiError, list["MyTemplateEntryV2"]]]:
    """
    Args:
        name (Union[Unset, str]): Filter by template name
        catalog (Union[Unset, str]):  Default: ''.
        pageable (SwaggerPageable): Pageable parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiError, list['MyTemplateEntryV2']]]
    """

    kwargs = _get_kwargs(
        name=name,
        catalog=catalog,
        pageable=pageable,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    catalog: Union[Unset, str] = "",
    pageable: "SwaggerPageable",
) -> Optional[Union[ApiError, list["MyTemplateEntryV2"]]]:
    """
    Args:
        name (Union[Unset, str]): Filter by template name
        catalog (Union[Unset, str]):  Default: ''.
        pageable (SwaggerPageable): Pageable parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiError, list['MyTemplateEntryV2']]
    """

    return sync_detailed(
        client=client,
        name=name,
        catalog=catalog,
        pageable=pageable,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    catalog: Union[Unset, str] = "",
    pageable: "SwaggerPageable",
) -> Response[Union[ApiError, list["MyTemplateEntryV2"]]]:
    """
    Args:
        name (Union[Unset, str]): Filter by template name
        catalog (Union[Unset, str]):  Default: ''.
        pageable (SwaggerPageable): Pageable parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiError, list['MyTemplateEntryV2']]]
    """

    kwargs = _get_kwargs(
        name=name,
        catalog=catalog,
        pageable=pageable,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    catalog: Union[Unset, str] = "",
    pageable: "SwaggerPageable",
) -> Optional[Union[ApiError, list["MyTemplateEntryV2"]]]:
    """
    Args:
        name (Union[Unset, str]): Filter by template name
        catalog (Union[Unset, str]):  Default: ''.
        pageable (SwaggerPageable): Pageable parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiError, list['MyTemplateEntryV2']]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            catalog=catalog,
            pageable=pageable,
        )
    ).parsed
