# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.8.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1StorageClass(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'allow_volume_expansion': 'bool',
        'api_version': 'str',
        'kind': 'str',
        'metadata': 'V1ObjectMeta',
        'mount_options': 'list[str]',
        'parameters': 'dict(str, str)',
        'provisioner': 'str',
        'reclaim_policy': 'str'
    }

    attribute_map = {
        'allow_volume_expansion': 'allowVolumeExpansion',
        'api_version': 'apiVersion',
        'kind': 'kind',
        'metadata': 'metadata',
        'mount_options': 'mountOptions',
        'parameters': 'parameters',
        'provisioner': 'provisioner',
        'reclaim_policy': 'reclaimPolicy'
    }

    def __init__(self, allow_volume_expansion=None, api_version=None, kind=None, metadata=None, mount_options=None, parameters=None, provisioner=None, reclaim_policy=None):
        """
        V1StorageClass - a model defined in Swagger
        """

        self._allow_volume_expansion = None
        self._api_version = None
        self._kind = None
        self._metadata = None
        self._mount_options = None
        self._parameters = None
        self._provisioner = None
        self._reclaim_policy = None
        self.discriminator = None

        if allow_volume_expansion is not None:
          self.allow_volume_expansion = allow_volume_expansion
        if api_version is not None:
          self.api_version = api_version
        if kind is not None:
          self.kind = kind
        if metadata is not None:
          self.metadata = metadata
        if mount_options is not None:
          self.mount_options = mount_options
        if parameters is not None:
          self.parameters = parameters
        self.provisioner = provisioner
        if reclaim_policy is not None:
          self.reclaim_policy = reclaim_policy

    @property
    def allow_volume_expansion(self):
        """
        Gets the allow_volume_expansion of this V1StorageClass.
        AllowVolumeExpansion shows whether the storage class allow volume expand

        :return: The allow_volume_expansion of this V1StorageClass.
        :rtype: bool
        """
        return self._allow_volume_expansion

    @allow_volume_expansion.setter
    def allow_volume_expansion(self, allow_volume_expansion):
        """
        Sets the allow_volume_expansion of this V1StorageClass.
        AllowVolumeExpansion shows whether the storage class allow volume expand

        :param allow_volume_expansion: The allow_volume_expansion of this V1StorageClass.
        :type: bool
        """

        self._allow_volume_expansion = allow_volume_expansion

    @property
    def api_version(self):
        """
        Gets the api_version of this V1StorageClass.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :return: The api_version of this V1StorageClass.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1StorageClass.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1StorageClass.
        :type: str
        """

        self._api_version = api_version

    @property
    def kind(self):
        """
        Gets the kind of this V1StorageClass.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :return: The kind of this V1StorageClass.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1StorageClass.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1StorageClass.
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """
        Gets the metadata of this V1StorageClass.
        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

        :return: The metadata of this V1StorageClass.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1StorageClass.
        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#metadata

        :param metadata: The metadata of this V1StorageClass.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def mount_options(self):
        """
        Gets the mount_options of this V1StorageClass.
        Dynamically provisioned PersistentVolumes of this storage class are created with these mountOptions, e.g. [\"ro\", \"soft\"]. Not validated - mount of the PVs will simply fail if one is invalid.

        :return: The mount_options of this V1StorageClass.
        :rtype: list[str]
        """
        return self._mount_options

    @mount_options.setter
    def mount_options(self, mount_options):
        """
        Sets the mount_options of this V1StorageClass.
        Dynamically provisioned PersistentVolumes of this storage class are created with these mountOptions, e.g. [\"ro\", \"soft\"]. Not validated - mount of the PVs will simply fail if one is invalid.

        :param mount_options: The mount_options of this V1StorageClass.
        :type: list[str]
        """

        self._mount_options = mount_options

    @property
    def parameters(self):
        """
        Gets the parameters of this V1StorageClass.
        Parameters holds the parameters for the provisioner that should create volumes of this storage class.

        :return: The parameters of this V1StorageClass.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this V1StorageClass.
        Parameters holds the parameters for the provisioner that should create volumes of this storage class.

        :param parameters: The parameters of this V1StorageClass.
        :type: dict(str, str)
        """

        self._parameters = parameters

    @property
    def provisioner(self):
        """
        Gets the provisioner of this V1StorageClass.
        Provisioner indicates the type of the provisioner.

        :return: The provisioner of this V1StorageClass.
        :rtype: str
        """
        return self._provisioner

    @provisioner.setter
    def provisioner(self, provisioner):
        """
        Sets the provisioner of this V1StorageClass.
        Provisioner indicates the type of the provisioner.

        :param provisioner: The provisioner of this V1StorageClass.
        :type: str
        """
        if provisioner is None:
            raise ValueError("Invalid value for `provisioner`, must not be `None`")

        self._provisioner = provisioner

    @property
    def reclaim_policy(self):
        """
        Gets the reclaim_policy of this V1StorageClass.
        Dynamically provisioned PersistentVolumes of this storage class are created with this reclaimPolicy. Defaults to Delete.

        :return: The reclaim_policy of this V1StorageClass.
        :rtype: str
        """
        return self._reclaim_policy

    @reclaim_policy.setter
    def reclaim_policy(self, reclaim_policy):
        """
        Sets the reclaim_policy of this V1StorageClass.
        Dynamically provisioned PersistentVolumes of this storage class are created with this reclaimPolicy. Defaults to Delete.

        :param reclaim_policy: The reclaim_policy of this V1StorageClass.
        :type: str
        """

        self._reclaim_policy = reclaim_policy

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1StorageClass):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
