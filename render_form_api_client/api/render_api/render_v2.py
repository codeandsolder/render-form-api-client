from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.render_request import RenderRequest
from ...models.render_response import RenderResponse
from ...models.render_v2_output import RenderV2Output
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RenderRequest,
    output: Union[Unset, RenderV2Output] = RenderV2Output.JSON,
    x_api_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["x-api-key"] = x_api_key

    params: dict[str, Any] = {}

    json_output: Union[Unset, str] = UNSET
    if not isinstance(output, Unset):
        json_output = output.value

    params["output"] = json_output

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/render",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApiError, RenderResponse]]:
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
        response_200 = RenderResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ApiError, RenderResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RenderRequest,
    output: Union[Unset, RenderV2Output] = RenderV2Output.JSON,
    x_api_key: str,
) -> Response[Union[ApiError, RenderResponse]]:
    """
    Args:
        output (Union[Unset, RenderV2Output]): Output format Default: RenderV2Output.JSON.
            Example: image.
        x_api_key (str):
        body (RenderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiError, RenderResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        output=output,
        x_api_key=x_api_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: RenderRequest,
    output: Union[Unset, RenderV2Output] = RenderV2Output.JSON,
    x_api_key: str,
) -> Optional[Union[ApiError, RenderResponse]]:
    """
    Args:
        output (Union[Unset, RenderV2Output]): Output format Default: RenderV2Output.JSON.
            Example: image.
        x_api_key (str):
        body (RenderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiError, RenderResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
        output=output,
        x_api_key=x_api_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RenderRequest,
    output: Union[Unset, RenderV2Output] = RenderV2Output.JSON,
    x_api_key: str,
) -> Response[Union[ApiError, RenderResponse]]:
    """
    Args:
        output (Union[Unset, RenderV2Output]): Output format Default: RenderV2Output.JSON.
            Example: image.
        x_api_key (str):
        body (RenderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiError, RenderResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        output=output,
        x_api_key=x_api_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RenderRequest,
    output: Union[Unset, RenderV2Output] = RenderV2Output.JSON,
    x_api_key: str,
) -> Optional[Union[ApiError, RenderResponse]]:
    """
    Args:
        output (Union[Unset, RenderV2Output]): Output format Default: RenderV2Output.JSON.
            Example: image.
        x_api_key (str):
        body (RenderRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiError, RenderResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            output=output,
            x_api_key=x_api_key,
        )
    ).parsed
