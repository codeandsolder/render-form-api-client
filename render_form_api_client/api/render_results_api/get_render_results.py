from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.page_render_result_item import PageRenderResultItem
from ...models.swagger_pageable import SwaggerPageable
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    template: Union[Unset, str] = UNSET,
    batch: Union[Unset, str] = UNSET,
    pageable: "SwaggerPageable",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["template"] = template

    params["batch"] = batch

    json_pageable = pageable.to_dict()
    params.update(json_pageable)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/results",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiError, PageRenderResultItem]]:
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
        response_200 = PageRenderResultItem.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiError, PageRenderResultItem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    template: Union[Unset, str] = UNSET,
    batch: Union[Unset, str] = UNSET,
    pageable: "SwaggerPageable",
) -> Response[Union[ApiError, PageRenderResultItem]]:
    """
    Args:
        template (Union[Unset, str]): Template identifier
        batch (Union[Unset, str]): Batch identifier for the render request
        pageable (SwaggerPageable): Pageable parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiError, PageRenderResultItem]]
    """

    kwargs = _get_kwargs(
        template=template,
        batch=batch,
        pageable=pageable,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    template: Union[Unset, str] = UNSET,
    batch: Union[Unset, str] = UNSET,
    pageable: "SwaggerPageable",
) -> Optional[Union[ApiError, PageRenderResultItem]]:
    """
    Args:
        template (Union[Unset, str]): Template identifier
        batch (Union[Unset, str]): Batch identifier for the render request
        pageable (SwaggerPageable): Pageable parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiError, PageRenderResultItem]
    """

    return sync_detailed(
        client=client,
        template=template,
        batch=batch,
        pageable=pageable,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    template: Union[Unset, str] = UNSET,
    batch: Union[Unset, str] = UNSET,
    pageable: "SwaggerPageable",
) -> Response[Union[ApiError, PageRenderResultItem]]:
    """
    Args:
        template (Union[Unset, str]): Template identifier
        batch (Union[Unset, str]): Batch identifier for the render request
        pageable (SwaggerPageable): Pageable parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiError, PageRenderResultItem]]
    """

    kwargs = _get_kwargs(
        template=template,
        batch=batch,
        pageable=pageable,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    template: Union[Unset, str] = UNSET,
    batch: Union[Unset, str] = UNSET,
    pageable: "SwaggerPageable",
) -> Optional[Union[ApiError, PageRenderResultItem]]:
    """
    Args:
        template (Union[Unset, str]): Template identifier
        batch (Union[Unset, str]): Batch identifier for the render request
        pageable (SwaggerPageable): Pageable parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiError, PageRenderResultItem]
    """

    return (
        await asyncio_detailed(
            client=client,
            template=template,
            batch=batch,
            pageable=pageable,
        )
    ).parsed
