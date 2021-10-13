from rest_framework import serializers

from dcim.choices import LinkStatusChoices
from dcim.api.serializers import NestedInterfaceSerializer
from ipam.api.serializers import NestedVLANSerializer
from netbox.api import ChoiceField
from netbox.api.serializers import NestedGroupModelSerializer, PrimaryModelSerializer
from wireless.models import *
from .nested_serializers import *

__all__ = (
    'WirelessLANSerializer',
    'WirelessLinkSerializer',
)


class WirelessLANGroupSerializer(NestedGroupModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='wireless-api:wirelesslangroup-detail')
    parent = NestedWirelessLANGroupSerializer(required=False, allow_null=True)
    wirelesslan_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = WirelessLANGroup
        fields = [
            'id', 'url', 'display', 'name', 'slug', 'parent', 'description', 'custom_fields', 'created', 'last_updated',
            'wirelesslan_count', '_depth',
        ]


class WirelessLANSerializer(PrimaryModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='wireless-api:wirelesslan-detail')
    vlan = NestedVLANSerializer(required=False, allow_null=True)

    class Meta:
        model = WirelessLAN
        fields = [
            'id', 'url', 'display', 'ssid', 'description', 'vlan',
        ]


class WirelessLinkSerializer(PrimaryModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='wireless-api:wirelesslink-detail')
    status = ChoiceField(choices=LinkStatusChoices, required=False)
    interface_a = NestedInterfaceSerializer()
    interface_b = NestedInterfaceSerializer()

    class Meta:
        model = WirelessLink
        fields = [
            'id', 'url', 'display', 'interface_a', 'interface_b', 'ssid', 'status', 'description',
        ]
