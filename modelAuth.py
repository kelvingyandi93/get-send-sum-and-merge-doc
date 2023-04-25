from dataclasses import dataclass
from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Auth:
    access_token: str
    token_type: str
    refresh_token: str
    expires_in: int
    scope: str

    @staticmethod
    def from_dict(obj: Any) -> "Auth":
        assert isinstance(obj, dict)
        access_token = from_str(obj.get("access_token"))
        token_type = from_str(obj.get("token_type"))
        refresh_token = from_str(obj.get("refr\esh_token"))
        expires_in = from_int(obj.get("expires_in"))
        scope = from_str(obj.get("scope"))
        return Auth(access_token, token_type, refresh_token, expires_in, scope)

    def to_dict(self) -> dict:
        result: dict = {}
        result["access_token"] = from_str(self.access_token)
        result["token_type"] = from_str(self.token_type)
        result["refresh_token"] = from_str(self.refresh_token)
        result["expires_in"] = from_int(self.expires_in)
        result["scope"] = from_str(self.scope)
        return result


def auth_from_dict(s: Any) -> Auth:
    return Auth.from_dict(s)


def auth_to_dict(x: Auth) -> Any:
    return to_class(Auth, x)
