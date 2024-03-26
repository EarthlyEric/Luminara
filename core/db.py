# -*- coding: UTF-8 -*-
from typing import Any, Sequence, Type
from bson.codec_options import TypeRegistry
import pymongo
from pymongo.client_session import ClientSession

from core.config import config


class DBClient(pymongo.MongoClient):
    def __init__(
        self,
        host: str | Sequence[str] | None = None,
        port: int | None = None,
        document_class: Type[Any] | None = None,
        tz_aware: bool | None = None,
        connect: bool | None = None,
        type_registry: TypeRegistry | None = None,
        **kwargs: Any
    ) -> None:
        if host is None:
            host = config.MongoDBURI 
        super().__init__(
            host=host,
            port=port,
            document_class=document_class,
            tz_aware=tz_aware,
            connect=connect,
            type_registry=type_registry,
            **kwargs
        )

