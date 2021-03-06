# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.decorators import Completer

from azure.cli.command_modules.resource._client_factory import (
    _resource_policy_client_factory, _resource_client_factory)

from azure.cli.command_modules.profile.custom import _load_subscriptions


@Completer
def get_policy_completion_list(cmd, prefix, namespace, **kwargs):  # pylint: disable=unused-argument
    policy_client = _resource_policy_client_factory(cmd.cli_ctx)
    result = policy_client.policy_definitions.list()
    return [i.name for i in result]


@Completer
def get_policy_set_completion_list(cmd, prefix, namespace, **kwargs):  # pylint: disable=unused-argument
    policy_client = _resource_policy_client_factory(cmd.cli_ctx)
    result = policy_client.policy_set_definitions.list()
    return [i.name for i in result]


@Completer
def get_policy_assignment_completion_list(cmd, prefix, namespace, **kwargs):  # pylint: disable=unused-argument
    policy_client = _resource_policy_client_factory(cmd.cli_ctx)
    result = policy_client.policy_assignments.list()
    return [i.name for i in result]


@Completer
def get_providers_completion_list(cmd, prefix, namespace, **kwargs):  # pylint: disable=unused-argument
    rcf = _resource_client_factory(cmd.cli_ctx)
    result = rcf.providers.list()
    return [r.namespace for r in result]


@Completer
def get_resource_types_completion_list(cmd, prefix, namespace, **kwargs):  # pylint: disable=unused-argument
    rcf = _resource_client_factory(cmd.cli_ctx)
    result = rcf.providers.list()
    types = []
    for p in list(result):
        for r in p.resource_types:
            types.append(p.namespace + '/' + r.resource_type)
    return types


@Completer
def get_subscription_id_list(cmd, prefix, namespace, **kwargs):  # pylint: disable=unused-argument
    subscriptions = _load_subscriptions(cmd.cli_ctx)
    result = []
    for subscription in subscriptions:
        result.append(subscription['id'])
        result.append(subscription['name'])
    return result
