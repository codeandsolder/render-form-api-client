from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.get_template_basics import GetTemplateBasics
from ...types import Response


def _get_kwargs(
    template_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/my-templates/{template_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiError, GetTemplateBasics]]:
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
        response_200 = GetTemplateBasics.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiError, GetTemplateBasics]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    template_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ApiError, GetTemplateBasics]]:
    """
    Args:
        template_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiError, GetTemplateBasics]]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    template_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ApiError, GetTemplateBasics]]:
    """
    Args:
        template_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiError, GetTemplateBasics]
    """

    return sync_detailed(
        template_id=template_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    template_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ApiError, GetTemplateBasics]]:
    """
    Args:
        template_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiError, GetTemplateBasics]]
    """

    kwargs = _get_kwargs(
        template_id=template_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    template_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ApiError, GetTemplateBasics]]:
    """
    Args:
        template_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiError, GetTemplateBasics]
    """

    return (
        await asyncio_detailed(
            template_id=template_id,
            client=client,
        )
    ).parsed
