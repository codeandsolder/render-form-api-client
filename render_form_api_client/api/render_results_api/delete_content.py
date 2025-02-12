from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...types import Response


def _get_kwargs(
    identifier: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/api/v2/results/{identifier}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ApiError]]:
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
        response_200 = cast(Any, None)
        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ApiError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    identifier: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ApiError]]:
    """
    Args:
        identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiError]]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    identifier: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ApiError]]:
    """
    Args:
        identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiError]
    """

    return sync_detailed(
        identifier=identifier,
        client=client,
    ).parsed


async def asyncio_detailed(
    identifier: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ApiError]]:
    """
    Args:
        identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiError]]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identifier: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ApiError]]:
    """
    Args:
        identifier (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiError]
    """

    return (
        await asyncio_detailed(
            identifier=identifier,
            client=client,
        )
    ).parsed
